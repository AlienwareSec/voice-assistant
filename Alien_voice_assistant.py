import subprocess
import wolframalpha
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import smtplib
import ctypes
import time
import requests
import shutil
from ecapture import ecapture as ec
from urllib.request import urlopen

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio=recognizer.listen(source)
            try:
                print(("Recognizing..."))
                data=recognizer.recognize_google(audio,language='en-in')
                return data
            except sr.UnknownValueError:
                speechtx("Sorry, i can't understand")
                print("Sorry, i can't understand")
def speechtx(x):
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail
    server.login('pawann3005@gmail.com', 'Alien@0630')
    server.sendmail('pawann3005@gmail.com', to, content)
    server.close()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speechtx("Good Morning Sir !")
    elif hour>= 12 and hour<18:
        speechtx("Good Afternoon Sir !")
    else:
        speechtx("Good Evening Sir !")
        assname =("alien 1 point o")
        speechtx("I am your Assistant")
        speechtx(assname)
def username():
    speechtx("What should i call you sir")
    uname = sptext()
    speechtx("Welcome Mister")
    speechtx(uname)
    columns = shutil.get_terminal_size().columns
    
    print("Welcome Mr.", uname.center(columns))
    
    speechtx("How can i Help you, Sir")
if __name__=='__main__':
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    username()
    while True:
    #if sptext().lower()=="listen alien": --> if you want your assistant to start only by a specific command.
        query=sptext().lower()
        if "your name" in query:
            name="my name is Alien"
            speechtx(name)
        elif "who created you" in query:
            creator="i am created by pawan gambhir"
            speechtx(creator)
        elif 'wikipedia' in query:
            speechtx("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=1)
            speechtx("According to wikipedia")
            print(results)
            speechtx(results)
        elif 'open youtube' in query:
            speechtx("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speechtx("Here you go to Google\n")
            webbrowser.open("google.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            speechtx(f"Sir, the time is {strTime}")
        elif 'open firefox' in query:
            codePath = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Firefox.lnk"
            os.startfile(codePath)
        elif 'how are you' in query:
                speechtx("I am fine, Thank you")
                speechtx("How are you, Sir")
        elif 'fine' in query or "good" in query:
                speechtx("It's good to know that your fine")
        elif "change my name to" in query:
                query = query.replace("change my name to", "")
                assname = query
        elif "change name" in query:
                speechtx("What would you like to call me, Sir ")
                assname = sptext()
                speechtx("Thanks for naming me")
        elif "what's your name" in query or "What is your name" in query:
                speechtx("My friends call me")
                speechtx(assname)
                print("My master named me", assname)
        elif 'joke' in query:
                speechtx(pyjokes.get_joke())
        elif "calculate" in query:
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speechtx("The answer is " + answer)
        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
        elif "who i am" in query:
            speechtx("If you talk then definitely your human.")
        elif "why you came to world" in query:
            speechtx("Thanks to Pawan. further It's a secret")
        elif 'is love' in query:
            speechtx("It is 7th sense that destroy all other senses")
        elif "who are you" in query:
            speechtx("I am your virtual assistant created by Pawan")
        elif 'reason for you' in query:
            speechtx("I was created as a Minor project by Mister Pawan ")
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,0,"Location of wallpaper",0)
            speechtx("Background changed successfully")
        elif 'lock window' in query:
            speechtx("locking the device")
            ctypes.windll.user32.LockWorkStation()
        elif 'shutdown system' in query:
            speechtx("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speechtx("Recycle Bin Recycled")
        elif "don't listen" in query or "stop listening" in query:
            speechtx("for how much time you want to stop alien from listening commands")
            a = int(sptext())
            time.sleep(a)
            print(a)
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speechtx("User asked to Locate")
            speechtx(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "alien Camera ", "img.jpg")
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
        elif "hibernate" in query or "sleep" in query:
            speechtx("Hibernating")
            subprocess.call("shutdown / h")
        elif "log off" in query or "sign out" in query:
            speechtx("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
            
        elif "write a note" in query:
            speechtx("What should i write, sir")
            note = sptext()
            file = open('alien.txt', 'w')
            speechtx("Sir, Should i include date and time")
            snfm = sptext()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
            
        elif "show note" in query:
            speechtx("Showing Notes")
            file = open("alien.txt", "r")
            print(file.read())
            speechtx(file.read(6))
        elif "weather" in query:
            
            # Google Open weather website
            # to get API of Open weather
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speechtx(" City name ")
            print("City name : ")
            city_name = sptext()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()
            
            if x["code"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
            
            else:
                speechtx(" City Not Found ")

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")
        
        elif "Good Morning" in query:
            speechtx("A warm" +query)
            speechtx("How are you Mister")
            speechtx(assname)
            
        elif "will you be my gf" in query or "will you be my bf" in query:
            speechtx("No sorry, i've a girlfriend.")
        
        elif "how are you" in query:
            speechtx("i'm doing good, how's life treating you?")
            
        elif "i love you" in query:
            speechtx("I love myself too but thanks i appriciate it")
            
        elif "what is" in query or "who is" in query:
            
            # use the same API key
            # that we have generated earlier
            client = wolframalpha.Client("API_ID")
            res = client.query(query)
            
            try:
                print (next(res.results).text)
                speechtx (next(res.results).text)
            except StopIteration:
                print ("No results")
        elif "thank you" in query:
            speechtx("Sayonara")
            exit(0)