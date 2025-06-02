import pyttsx3
import psutil
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import getpass
import pyjokes
import pyautogui
import cv2
import platform
import geocoder
import requests
import json


g = geocoder.ip('me')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# print(voices[0].id)


def speak(audio):
    try:
        engine.say(audio)
        engine.runAndWait()
    except TypeError as e:
        print(f"Error in speak: {e}")


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)
def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)


def joke():
    for _ in range(5):
        try:
            speak(pyjokes.get_joke())
        except Exception as e:
            print("Error in joke:", e)


def wishMe():
    speak("Hey MAGESHWARI Welcome Back!")
    time()
    date()
    weather()
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning MAGESHWARI")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon MAGESHWARI")

    else:
        speak('Good Evening MAGESHWARI')

    speak("NOAH at your service,what do you want me to do?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"     
    return query
def screenshot():
    img = pyautogui.screenshot()
    img.save('screenshot.png')
def webcamsnap():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        cv2.imwrite("NewPicture.jpg",frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("Here goes your email", "your password")
    server.sendmail('your email', to, content)
    server.close()
    
def weather():
    try:
       
        system_has_weather_data = False  

        if system_has_weather_data:
            # Mock sensor data
            lat = 12.97
            lon = 77.59
            location = "Local Sensor Location"
            country = "IN"
            temp = 26
            humidity = 65
            wind_speed = 3.2
            weather_type = "Clear"

            speak(f'{lat} latitude and {lon} longitude')
            speak(f'Current location is {location}, {country}')
            speak(f'Weather type: {weather_type}')
            speak(f'Wind speed is {wind_speed} metre per second')
            speak(f'Temperature: {temp} degree Celsius')
            speak(f'Humidity is {humidity} percent')
        else:
            speak("Couldn't fetch weather data from the system.")
    except Exception as e:
        print(f"Error accessing system weather data: {e}")
        speak("Sorry, I couldn't retrieve the weather information.")



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            speak("the current time is")
            time()
        elif 'date' in query:
            speak("today's date is")
            date()
        elif 'what is the weather' in query or 'weather' in query:
            speak("the weather now is")
            weather()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'turn on bluetooth' in query:
            speak("Turning on Bluetooth")
            os.system('powershell "Get-PnpDevice -FriendlyName \'Bluetooth*\' | Enable-PnpDevice -Confirm:$false"')

        elif 'turn off bluetooth' in query:
            speak("Turning off Bluetooth")
            os.system('powershell "Get-PnpDevice -FriendlyName \'Bluetooth*\' | Disable-PnpDevice -Confirm:$false"')


        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = 'recepient email' #receiver email 
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("unable to send the email")
        elif 'search in chrome' in query:
            speak('What should I search?')
            search = takeCommand().lower()
            url = f"https://www.google.com/search?q={search}"
            speak(f"Searching for {search} on Google")
            wb.open_new_tab(url)

        elif 'shutdown' in query:
            os.system("shutown /s /t 1") 
        elif 'restart' in query or 'restat' in query:
            os.system('shutdown /r /t 1')
        elif 'logout' in query or 'log out' in query:
            os.system('shutdown -1')
        elif 'NOAH are you there' in query:
            speak("Yes Sir, at your service")
        elif 'goodbye' in query or 'good boy' in query or 'goodboy' in query:                          
            speak("Goodbye MAGESHWARI NOAH is powering off in 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 Bye")
            break
        elif 'thanks' in query or 'tanks' in query or 'thank' in query or 'thank you' in query:
            speak('You are wellcome no problem')
        elif 'who developed you' in query:
            if platform == "win32" or "darwin":
                speak('MAGESHWARI is my master. she created me on 11th jan 2025')
            elif platform == "linux" or platform == "linux2":
                name = getpass.getuser()
                speak(name, 'is my master. she is running me right now')
        elif 'what is your name' in query:
            speak('My name is NOAH')

        elif 'NOAH stands for' in query:
            speak('NOAH stands for Hacker who can get into your data without knowing to you')
        elif 'shutdown' in query:
            speak('good night')
            os.system('Shutdown.exe -s -t 00')

        elif 'restart' in query:
            speak("restarting")
            os.system("Shutdown.exe -r -t 00") 

        elif "open whatsapp" in query or "whats hub" in query:
            speak("opening whats app")
            wb.open_new_tab("https://web.whatsapp.com")

        elif "open instagram" in query:
            speak("Opening instagram")
            wb.open_new_tab("https://instagram.com")

        elif "open facebook" in query:
            speak("Opening facebook")
            wb.open_new_tab("https://facebook.com")
        elif 'play songs' in query:
            songs_dir = '' #songs directory
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()
        elif 'snapshot' in query or 'snapchat' in query:
            speak("taking webcam picture")
            webcamsnap()
        elif 'remember that' in query:
            speak("what should i remember?")
            data = takeCommand()
            speak("you said me to remember that"+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        elif 'cpu' in query:
            speak("Loading...")
            cpu()
        elif 'jokes' in query or 'joke' in query:
            speak("here is a joke")
            joke()

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" +remember.read())
        elif 'offline' in query:
            quit()   

