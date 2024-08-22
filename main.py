import win32com.client
import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime


def ai(prompt):
    # Set the OpenAI API key
    openai.api_key = apikey

    # Make the API call to generate completions
    response = openai.Completion.create(
        model="gpt-3.5-turbo-1106",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print the API response
    print(response[0]["text"])

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def speak(text):
    speaker.Speak(text)

#while 1:
    #print("Enter the word to speak")
    #s= input()
   # speaker.Speak(s)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
           query = r.recognize_google(audio, language ="en-in")
           print(f" User said: {query}")
           return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"


if __name__ =="__main__" :
    print('PyCharm')
    speak("Hello ! I am Jarvis AI")
    while True:
       print("Listening....")
       query = takeCommand()
       sites =[[ "youtube", "https://www.youtube.com"], ["wikipedia","https://www.wikipedia.com"], ["Google", "https://www.Google,com"],]
       for site in sites:
           if f"Open {site[0]}".lower() in query.lower():
               speak(f"opening {site[0]} Maam.... ")
               webbrowser.open(site[1])

       if "open music" in query:
           musicPath = "https://pixabay.com/music/"
           speaker.speak(f" Open {musicPath}")

       if "the time" in query:
           strfTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"Maam the time is...{strfTime}")

       if "open Camera".lower() in query.lower():
           os.system(f"open \Public\Desktop\PyCharm Community Edition 2024.1.4.lnk")
       #speak(query)
