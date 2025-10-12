import speech_recognition as sr

import webbrowser
import pyttsx3
import musicLibrary
import requests
# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "0c442bf944e34baeacb0980f41bfcbce"
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
     if "open google" in c.lower():
          webbrowser.open("https://google.com")
     elif "open instagram" in c.lower():
          webbrowser.open("https://instagram.com")   
     elif "open youtube" in c.lower():
          webbrowser.open("https://youtube.com")   
     elif "open linkedin" in c.lower():
          webbrowser.open("https://linkedin.com")   
     elif "open leetcode" in c.lower():
          webbrowser.open("https://leetcode.com")
     elif c.lower().startswith("play"):
          song = c.lower().split(" ")[1]
          link = musicLibrary.music[f"play {song}"]
          webbrowser.open(link)
     elif "news" in c.lower():
          
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
    
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])

        if articles:
            # Print the headlines
            for article in articles:
                speak(article['title'])  # assuming you have a 'speak' function defined
        else:
            speak("Sorry, I couldn't find any news articles at the moment.")
     else:
          #let openAi handle the request
        pass

if __name__ == "__main__":
    speak("initializing Jarvis....")
    while True:
        #Listen for the wake word "Jarvis"
        #obtain audio from the microphone 
        r = sr.Recognizer()

        print("reconizing... ")
        #recognize speech using google
        try:
            with sr.Microphone() as source:
                    print("Listning...")
                    audio = r.listen(source, timeout=2, phrase_time_limit=1 )

            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                 speak("Yes faisal")
                 #listen for command
                 with sr.Microphone() as source:
                    print("jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))