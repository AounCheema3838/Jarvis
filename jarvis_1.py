import pyttsx3
import speech_recognition as sr
import webbrowser 
import datetime
import pyjokes
import os


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing....")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understanding")
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate",120)
    engine.say(x)
    engine.runAndWait()


if __name__ == "__main__":
    
    
    #if sptext().lower() in "hey honey":
       
       data1=sptext().lower()
       if "your name" in data1:
            name = "my name is honey"
            speechtx(name)
                  
       elif "old are you" in data1:
            age = "i am two years old"
            speechtx(age)
       elif "time" in data1:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speechtx(current_time)
       elif "youtube" in data1:
            webbrowser.open("https://www.youtube.com/" )    
             
            
       elif "fibre" in data1:
            webbrowser.open("https://www.fiverr.com/?source=top_nav" )
       elif "job" in data1:                                                               
            joke_1 = pyjokes.get_joke(language="en" , category = "neutral")
            speechtx(joke_1)
            print (joke_1)
       elif "play song"in data1:
            add = "E:\song"
            listsong = os.listdir(add)
            print(listsong)
            os.startfile(os.path.join(add,listsong[0]))
            
    #else:
    #    print("thanks")	
	        
		                  

	

	
            
            
	
  
