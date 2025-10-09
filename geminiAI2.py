import os
import google.generativeai as genai
import threading
import pyttsx3
from groq import Groq
from gtts import gTTS
import pygame
import io

# SEARCH YT ON HOW TO GET API KEY!!!
# SEARCH YT ON HOW TO GET API KEY!!!
# SEARCH YT ON HOW TO GET API KEY!!!
# SEARCH YT ON HOW TO GET API KEY!!!
# Delete groq if it not work
# Delete groq if it not work

# You can put ur key here or through embemded into system
# os.environ["GEMINI_API_KEY"] = ""
# os.environ["GROQ_API_KEY"] = ""

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 128,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-8b",
  generation_config=generation_config,
    system_instruction="Think like a human. Turn these into words in English USING ONLY THOSE WORD OR CHARACTER, DO NOT ADD MORE, the grammar HAS TO BE CORRECT, change '-' into a " ", there maybe abbreviations made from characters and you MAY or MAY NOT change it into words or phrase base on the meaning of it, the output should ONLY BE THE SETENCE WITH NO EXPLAINATION: {text}. I will give you the text input next",
)

chat_session = model.start_chat(
  history=[
  ]
)

def IntoAI (text):
  try:
    response = chat_session.send_message(text)
    return response.text
  except genai.types.generation_types.StopCandidateException as e:
        print("Change model cause of gemini violence rules")
        chat_completion = client.chat.completions.create(
          messages=[
              {
                  "role": "user",
                  "content": f"Think like a human. Turn these into words in English USING ONLY THOSE WORD OR CHARACTER, DO NOT ADD MORE, the grammar HAS TO BE CORRECT, change '-' into a " ", there maybe abbreviations made from characters and you MAY or MAY NOT change it into words or phrase base on the meaning of it, the output should ONLY BE THE SETENCE WITH NO EXPLAINATION: {text}. I will give you the text input next",
              }
          ],
          model="mixtral-8x7b-32768",
        )
        return chat_completion.choices[0].message.content


def play_voice_google(text):
    # Sử dụng io.BytesIO thay vì lưu vào file MP3
    tts = gTTS(text=text, lang="en")
    
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    
    pygame.mixer.init()
    
    voice_channel = pygame.mixer.Channel(2) 
    voice_channel.play(pygame.mixer.Sound(mp3_fp))

    # Chờ cho đến khi âm thanh phát xong
    while voice_channel.get_busy():
        pygame.time.Clock().tick(10)
    voice_channel.stop()
    
def play_voice(text):
    engine = pyttsx3.init() 
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Select MALE/FEMALE
    engine.setProperty('rate', 130)  # SPEECH RATE
    engine.setProperty('volume', 1.0) #VOLUME FROM MIN - MAX (0-1)

    engine.say(text)
    engine.runAndWait()

isSpeaking = False  # Biến trạng thái để kiểm tra

def IntoVoice(string):
    global isSpeaking
    if isSpeaking:
        return  # Nếu đang phát giọng nói, không làm gì cả
    isSpeaking = True
    
    def process_AI():
        text = IntoAI(string)
        play_voice_google(text)
        global isSpeaking
        isSpeaking = False
        
    threading.Thread(target=process_AI).start()

# WHY THREADING?? BC WHEN YOU RUN ANOTHER PROGRAM AND THEN RUN THIS AI VOICE, THE CAMERA OF OPEN CV WILL STOP!! SO RUN IN ANOTHER THREAD
# WHY THREADING?? BC WHEN YOU RUN ANOTHER PROGRAM AND THEN RUN THIS AI VOICE, THE CAMERA OF OPEN CV WILL STOP!! SO RUN IN ANOTHER THREAD
# WHY THREADING?? BC WHEN YOU RUN ANOTHER PROGRAM AND THEN RUN THIS AI VOICE, THE CAMERA OF OPEN CV WILL STOP!! SO RUN IN ANOTHER THREAD

# IntoVoice(IntoAI("HELLO-NICE-TO-MEET-U-BUT-I-GTG"))
# print(IntoAI("GG-IT-A-VERY-GOOD-GAME-TBH"))
# print(IntoAI("I-CANT-BELIEVE-YOU-FINISHED-THE-GAME-IN-5-MINS-LOL"))
# print(IntoAI("APPLE"))