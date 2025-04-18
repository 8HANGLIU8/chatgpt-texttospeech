from kaepyi import OPENAI_API_KEY
from pathlib import Path
from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)
speech_file_path = Path(__file__).parent / "sound.mp3"
 
#USER INPUT SECTION
#----------------------------------------------#

INPUT = "Hello how are you. My name is Hang" 
INSTRUCTIONS = "speak with excitement and energy"
VOICE = "echo"
MODEL = "gpt-4o-mini-tts"

#----------------------------------------------#

with client.audio.speech.with_streaming_response.create(
    model=MODEL,
    voice=VOICE,
    input=INPUT,
    instructions=INSTRUCTIONS,
) as response:
    response.stream_to_file(speech_file_path)


#----------------------------------------------#

import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("sound.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

pygame.quit()