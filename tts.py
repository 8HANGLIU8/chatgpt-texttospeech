from kaepyi import OPENAI_API_KEY


from pathlib import Path
from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)
speech_file_path = Path(__file__).parent / "sound.mp3"

with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="echo",
    input="Hello, welcome to the future of AI!",
    instructions="Speak with excitement and energy.",
) as response:
    response.stream_to_file(speech_file_path)