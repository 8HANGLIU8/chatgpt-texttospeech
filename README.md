# chatgpt-texttospeech
text to speech using chatgpt


Documentary : https://platform.openai.com/docs/guides/text-to-speech

Streaming real time audio

1. Create a file called 'kaepyi.py' and insert: 

#api-key

OPENAI_API_KEY='your-api-key-here'

2. Create an environment if you didn't install Python Library: 

python3 -m venv tts 
source tts/bin/activate
python3 tts.py

3. create a .gitignore file where you'll write 'kaepyi.py'

4. Install packages

python3 -m venv tts 
source tts/bin/activate
pip install pygame 
pip install openai 

5. When you'll run, they'll be a sound file called sound.mp3 that will pop in your folder and a pycache is there is.

6. Some modification can be made in tts.py such as the model, the voice, the input and instructions for chatgpt
