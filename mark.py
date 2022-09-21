import time as T
import pyttsx3
import speech_recognition as sr
import datetime
from datetime import date
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import pyautogui
import requests
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from markUi import Ui_Mark
import operator
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import os
from twilio.rest import Client
import MyAlarm
import subprocess
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 180)
# convert speak to textc


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# national news


def nationalNews():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=44ee15fb72134e9ab8e5133b5e1ce777"
    pages = requests.get(url).json()
    articles = pages["articles"]
    # print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eighth", "ninth", "tenth"]
    for i in articles:
        head.append(i["title"])
    for i in range(len(day)):
        speak(f"Headline {day[i]} news is {head[i]}")

    # hello

    # international news


def wish():
    hour = int(datetime.datetime.now().hour)
    time = datetime.datetime.now()
    time = datetime.datetime.strftime(time, "%H:%M")

    if (hour >= 0 and hour <= 12):
        speak("Good Morning")
        speak(f"It is {time}")

    elif (hour > 12 and hour < 18):
        speak("Good Afternoon")
        speak(f"It is {time}")
    else:
        speak("Good Evening")
        speak(f"It is {time}")
    speak("I am project 3200 , please tell me how can i help you")
# send mail


def getDate():
    # print("entering to date time module")
    today = datetime.date.today()
    # print(today)
    d2 = today.strftime("%B %d, %Y")
    # print(d2)
    speak(f"Today is {d2}")


def sendEmail(target, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("mottaki567@gmail.com", "objgvshskmnczgbd")
    server.sendmail(
        "mottaki567@gmail.com", target, content)
    server.close()

    # driver function of jervis


# def calculate():


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening ...")
            r.pause_threshold = 1
            # audio = r.listen(source, timeout=1, phrase_time_limit=6)
            audio = r.listen(source, phrase_time_limit=6)
            try:
                print("Recognizing ...")
                self.query = r.recognize_google(audio, language='en-in')
                print(f"User said: {self.query}")

            except Exception as a:
                return "none"
            return self.query

    def run(self):

        self.TaskExecution()

        while True:
            self.query = self.takecommand().lower()
            if "wake" in self.query:
                self.TaskExecution()

            elif "sleep" in self.query:
                self.query = self.takecommand().lower()\

            elif "break" in self.query or "stop" in self.query or "exit" in self.query or "goodbye" in self.query:
                speak("Thank you very much, wake me up at any time")
                sys.exit()
                return
                break

    # take voice from user

    def TaskExecution(self):
        wish()
        error = "There is an error, Please try again later"
        while 1:
            self.query = self.takecommand().lower()
            while self.query == "none":
                speak("Pleas say that again")
                self.query = self.takecommand().lower()
            print(self.query)
            # logic building for task

            if "open notepad" in self.query:
                try:

                    npath = "C:\\Windows\\System32\\notepad.exe"
                    os.startfile(npath)
                    pass
                except Execution as a:
                    print(error)
                    speak(error)
                    pass
            elif "good" in self.query or "great" in self.query:
                speak("Thats great sir,how can i help you?")

            elif "list commands" in self.query:
                try:

                    npath = "D://CSE 3200//commands.txt"
                    os.startfile(npath)
                except Exception as a:

                    print(errror)
                    speak(error)
                    pass

            elif "how are you" in self.query:
                try:
                    speak("I am fine sir,how are you?")
                    pass
                except Execution as a:
                    print(error)
                    speak(error)
                    pass

            elif "do some calculation" in self.query or "can you calculate" in self.query or "calculation" in self.query or "calculator" in self.query:

                try:

                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        speak("Say what you want to calculate, example: 3 plus 3")
                        print("listening ...")
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                        my_string = r.recognize_google(audio)
                        print(my_string)

                    def get_operator_fn(op):
                        return {
                            '+': operator.add,
                            "-": operator.sub,
                            "*": operator.mul,
                            "/": operator.__truediv__,
                        }[op]

                    def eval_binary_expr(op1, oper, op2):
                        op1, op2 = int(op1), int(op2)
                        return get_operator_fn(oper)(op1, op2)
                    speak("Your result is ")
                    speak(eval_binary_expr(*(my_string.split())))
                except Exception as a:
                    speak("There is an error")
                    pass

            elif "close" in self.query:
                name = self.query.split(" ")[1]
                speak(f"Closing {name}")
                name = str(name)+".exe"
                print(name)
                try:

                    app = f"taskkill /f /im { name}"
                    print(app)
                    os.system(app)
                except Exception as a:
                    print(error)
                    speak(error)
                    pass

            elif "set alarm" in self.query:
                try:
                    speak(
                        f"Sir please tell me when to set alarm.For example, set alarm to 2:20 pm")
                    time = self.takecommand().lower()
                    time = time.replace("set alarm to", "")
                    time = time.replace(".", "")
                    time = time.upper()
                    time = time.strip()
                    print(time)
                    MyAlarm.alarm(time)

                except Exception as a:
                    print(error)
                    speak(error)
                    pass

            elif "open command prompt" in self.query:
                try:
                    npath = "C:\\Windows\\System32\\cmd.exe"
                    os.startfile(npath)
                except Exception as a:
                    print(error)
                    speak(error)
                    pass

            elif "open camera" in self.query:
                try:

                    cap = cv2.VideoCapture(0)
                    while True:
                        ret, img = cap.read()
                        cv2.imshow("webcam", img)
                        k = cv2.waitKey(50)
                        if k == 27:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    speak("command for open camera")
                except Exception as a:
                    print(error)
                    speak(error)
                    passprint(error)
                    speak(error)
                    pass

            elif "play music" in self.query:
                try:
                    music_dir = "D:\\CSE 3200\\music"
                    songs = os.listdir(music_dir)
                    for song in songs:
                        if song.endswith(".mp3"):
                            os.startfile(os.path.join(music_dir, song))
                except Exception as a:
                    print(error)
                    speak(error)
                    pass

            elif "ip address" in self.query:
                try:

                    ip = get("https://api.ipify.org").text
                    speak(f"Your ip address is {ip}")

                except Exception as a:
                    print(error)
                    speak(error)
                    pass

            elif "who is" in self.query or "wikipedia" in self.query or "what is" in self.query or "tell me something about" in self.query:
                try:

                    if ("who is" in self.query):
                        self.query = self.query.replace("who is", "")
                    elif ("wikipedia" in self.query):
                        self.query = self.query.replace("wikipedia", "")
                    elif ("what is" in self.query):
                        self.query = self.query.replace("what is", "")
                    elif ("tell me something about" in self.query):
                        self.query = self.query.replace(
                            "tell me something about", "")
                    speak(f"Getting result for {self.query}")
                    print(self.query)

                    result = wikipedia.summary(self.query, sentences=2)
                    print(result)
                    speak(result)
                except Exception as a:
                    print(a)
                    print(error)
                    speak(error)
                    pass

            elif "how to" in self.query:
                try:

                    speak("searching for results")
                    max_res = 1
                    how_to = search_wikihow(self.query, max_res)
                    assert len(how_to) == 1
                    how_to[0].print()
                    speak(how_to[0].summary)
                except Exception as a:
                    print(error)
                    speak(error)
                    pass

            elif "open youtube" in self.query:
                try:

                    speak("what to play")
                    play = self.takecommand().lower()
                    print(play)
                    kit.playonyt(f"{play}")
                except Exception as a:
                    print(error)
                    speak(error)
                    pass

            elif "set alarm" in self.query:
                try:
                    nn = int(datetime.datetime.now().hour)
                    if nn == 22:
                        music_dir = "D:\\CSE 3200\\alarm"
                        songs = os.listdir(music_dir)
                        os.startfile(os.path.join(music_dir, songs[0]))
                except Exception as a:
                    print(error)
                    speak(error)
                    pass

            elif "send mail" in self.query:
                try:
                    speak("which one to send")
                    target = "mottaki1503028@gmail.com"
                    speak("what to say")
                    content = self.takecommand().lower()
                    sendEmail(target, content)
                    speak(f"Email has been sent to {target} ")

                except Exception as a:
                    print(a)
                    speak("Sorry, There is an error")

            elif "send message" in self.query:

                try:
                    speak("which one to send")
                    target = "+8801910982274"
                    speak("what to say")
                    text = self.takecommand().lower()
                    if (text == "none"):
                        text = "Its a demo message"
                    account_sid = 'AC10e6a8fc941c23a1774b7462a0b3d5a4'
                    auth_token = '5e19bbdb367db956f398f05cb14177b7'
                    client = Client(account_sid, auth_token)

                    message = client.messages \
                                    .create(
                                        body=text,

                                        from_='+16187624548',
                                        to='+8801910982274'
                                    )

                    print(message.sid)
                    speak(f"Email has been sent to {target} ")

                except Exception as a:
                    print(a)
                    speak("Sorry, There is an error")

            elif "open google" in self.query:
                try:

                    speak("what to search in google")
                    self.query = self.takecommand().lower()
                    webbrowser.open(f"{self.query}")
                except Exception as a:
                    print(error)
                    speak(error)
                    pass

            elif "open facebook" in self.query:
                try:

                    webbrowser.open("http://www.facebook.com")
                except Exception as a:
                    print(error)
                    speak(error)
                    pass

            elif "open github" in self.query:
                try:

                    webbrowser.open("http://www.github.com")
                except Exception as a:
                    print(error)
                    speak(error)
                    pass

            elif "open twitter" in self.query:
                try:

                    webbrowser.open("http://www.twitter.com")
                except Exception as a:
                    print(error)
                    speak(error)
                    pass

            elif "open stack overflow" in self.query:
                try:

                    webbrowser.open("http://www.stackoverflow.com")
                except Exception as a:
                    print(error)
                    speak(error)
                    pass

            elif "news update" in self.query:
                try:

                    speak("Getting news")
                    nationalNews()
                except Exception as a:
                    print(error)
                    speak(error)
                    pass

            elif "date" in self.query or "what date is today" in self.query or "todays date" in self.query:
                try:
                    getDate()
                except Exception as a:
                    print(error)
                    speak(error)
                    pass

            elif "tell me a joke" in self.query:
                try:

                    joke = pyjokes.get_joke()
                    speak(joke)
                except Exception as a:
                    print(error)
                    speak(error)
                    pass
            elif "shutdown the system" in self.query:
                try:

                    os.system("shutdown /s /t 5")
                except Exception as a:
                    print(error)
                    speak(error)
                    pass
            elif "restart the system" in self.query:
                try:

                    os.system("shutdown/ r/ t 5")
                except Exception as a:
                    print(error)
                    speak(error)
                    pass

            elif "sleep mode" in self.query or "rest" in self.query or "take a nap" in self.query or "sleep" in self.query:
                speak("Thank you very much, wake me up at any time")
                break

            elif "break" in self.query or "stop" in self.query or "exit" in self.query or "goodbye" in self.query:
                speak("Thank you very much, have a good day")
                sys.exit()
                return
                break

            elif "switch window" in self.query:
                try:
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    pyautogui.keyUp("alt")
                except Exception as a:
                    print(error)
                    speak(error)
                    pass
            elif "show commands" in self.query:
                try:
                    command_dir = "D:\\CSE 3200\\command.txt"
                    songs = os.listdir(command_dir)
                    os.startfile(os.path.join(command_dir))

                except Exception as a:
                    print(error)
                    speak(error)
                    pass

            elif "weather forecast" in self.query:
                api_id = "6b8d55b7789caaa56adb65f3fa52f1c7"
                try:
                    search = "temperature of rajshahi, bangladesh"
                    speak("Getting weather update for rajshahi, bangladesh")
                    url = f"https://api.openweathermap.org/data/2.5/weather?q=Rajshahi,Bangladesh&appid={api_id}"

                    r = requests.get(url)
                    data = r.json()
                    t = data["main"]
                    # print(temp)
                    temp = t["temp"]
                    feels_like = t["feels_like"]
                    humidity = t["humidity"]

                    wind = data["wind"]
                    speed = wind["speed"]
                    angle = wind["speed"]
                    gust = wind["gust"]
                    speak(
                        f"Current temperature of rajshahi, bangladesh is {' % .2f' % round(temp-273, 2)}, Feels like {' % .2f' % round(feels_like-273, 2)}, humidity {humidity} , air {speed} per hour , air  angle is {angle}")
                except Exception as a:
                    print(error)
                    speak(error)
                    pass

            elif "open" in self.query:
                from application import app_path

                try:
                    name = self.query.split(" ")[1]
                    print(name)
                    if name in app_path.keys():
                        path = app_path[name]
                        print(path)
                        os.startfile(path)
                except Exception as a:
                    print(error)
                    speak(error)
                    pass

            elif "tell me location" in self.query:
                speak("Let me check the location")
                try:
                    ipAdd = requests.get("https://api.ipify.org").text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)

                    geo_data = geo_requests.json()
                    print(geo_data)
                    city = geo_data["city"]
                    country = geo_data["country"]
                    speak(
                        f"sir i am not sure , but i think you are in {city}of country {country}")

                except Exception as a:
                    speak("sorry there is an error, please try again later")
                    pass

            else:
                speak("command not found")

                if "self.query" != "none":
                    speak("would you like to add command")
                    T.sleep(2)
                    speak("sorry command set mode is not set yet")
                    T.sleep(1)
                    speak("list commands to access all command")

                speak("sir do you have any query?")


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Mark()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.close)
        self.ui.pushButton_2.clicked.connect(self.startTask)

    def startTask(self):
        self.ui.movie = QtGui.QMovie(
            "D:/CSE 3200/ruet3.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
mark = Main()
mark.show()
exit(app.exec_())
