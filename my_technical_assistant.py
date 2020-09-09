import datetime
import getpass
import os
import smtplib
import webbrowser
from datetime import date

import pyttsx3
import speech_recognition as sr
import wikipedia
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    name = "Faraz"
    speak("hii sir, i am  your assistant")
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour < 12):
        speak(f"Good Morning {name}!")
    elif (hour >= 12 and hour < 18):
        speak(f"Good Afternoon {name}!")
    else:
        speak(f"Good Evening {name}!")
    speak("Please tell me how i can help you?")
    print("\t\t _____________________________________________________________________________________________ ")
    print("\t\t|\t                                                                                      |")
    print("\t\t|\tI will do the following things for you -->                                            |")
    speak("I will do the following things for you")
    print("\t\t|\t-----------------------------------------------------                                 |")
    print("\t\t|\tI can show u -->                                                                      |")
    print("\t\t|\t                 Current Time                                                         |")
    print("\t\t|\t                 Today's date                                                         |")
    print("\t\t|\t-----------------------------------------------------                                 |")
    print("\t\t|\tI can open -->                                                                        |")
    print("\t\t|\t               GMail                                                                  |")
    print("\t\t|\t               GitHub                                                                 |")
    print("\t\t|\t               YouTube                                                                |")
    print("\t\t|\t               Facebook                                                               |")
    print("\t\t|\t               LinkedIn                                                               |")
    print("\t\t|\t               Instagram                                                              |")
    print("\t\t|\t               Calculator                                                             |")
    print("\t\t|\t               Chome Browser                                                          |")
    print("\t\t|\t               Notepad editor                                                         |")
    print("\t\t|\t               VLC Media Player                                                       |")
    print("\t\t|\t               Oracle Virtual Box                                                     |")
    print("\t\t|\t               Sublime Text Editor                                                    |")
    print("\t\t|\t               Windows Media Player                                                   |")
    print("\t\t|\t               Visual Studio Code Editor                                              |")
    print("\t\t|\t-----------------------------------------------------                                 |")
    print("\t\t|\tI can search for you in -->                                                           |")
    print("\t\t|\t                           Google                                                     |")
    print("\t\t|\t                           YouTube                                                    |")
    print("\t\t|\t                           Wikipedia                                                  |")
    print("\t\t|\t-----------------------------------------------------                                 |")
    print("\t\t|\tI can do arithmetic operations -->                                                    |")
    print("\t\t|\t                                   Addition                                           |")
    print("\t\t|\t                                   Subtraction                                        |")
    print("\t\t|\t                                   Multiplication                                     |")
    print("\t\t|\t                                   Division                                           |")
    print("\t\t|\t-----------------------------------------------------                                 |")
    print("\t\t|\tI can show u the code for doing Arithmetic Operations for -->                         |")
    print("\t\t|\t                                                              Addition                |")
    print("\t\t|\t                                                              Subtraction             |")
    print("\t\t|\t                                                              Multiplication          |")
    print("\t\t|\t                                                              Division                |")
    print("\t\t|\t-----------------------------------------------------                                 |")
    print("\t\t|\tI can send E-mail for you.                                                            |")
    print("\t\t|\t-----------------------------------------------------                                 |")
    print("\t\t|\tI can play music for you.                                                             |")
    print("\t\t|_____________________________________________________________________________________________|")
    print()


if __name__ == "__main__":
    wishme()
    password = "abc123"
    speak("Please type password to begin!")
    pswd = getpass.getpass("Please type password to begin! ")
    count = 5
    while True:

        if pswd == password:

            def takeCommand():
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("Order me sir, what to do")
                    print("Listening...")
                    r.adjust_for_ambient_noise(source)
                    r.pause_threshold = 1
                    audio = r.listen(source)
                try:
                    print("Recognizing your voice...")
                    q = r.recognize_google(audio, language='en-in')
                    print(f"User said: {q}\n")
                except Exception as e:
                    print("Say again please...")
                    return "None"
                return q

            def sendEmail(to, content):
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                speak("Enter password of your email id : ")
                pwd = getpass.getpass("Enter password of your email id : ")
                server.login('farazulhaque26@gmail.com', pwd)
                server.sendmail('farazulhaque26@gmail.com', to, content)
                server.close()

            q = takeCommand().lower()

            if (("date" in q) and ("today" in q)):
                if (("don't" in q) or ("do not" in q)):
                    speak("Okay. I will not show u today's date")
                    print("Okay. I will not show u today's date")
                    print()
                else:
                    today = date.today()
                    speak(f"Today's date is : {today}")
                    print("Today's date:", today)
                    print()
            elif (("time" in q) or ("tym" in q)):
                if (("don't" in q) or ("do not" in q)):
                    speak("Okay. I will not show u current time")
                    print("Okay. I will not show u current time")
                    print()
                else:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the current time is {strTime}")
                    print(f"Sir, the current time is {strTime}")
                    print()
            elif (("calc" in q) or ("calculator" in q)):
                if (("don't" in q) or ("do not" in q)):
                    speak("Okay. I will not open calculator")
                    print("Okay. I will not open calculator")
                    print()
                else:
                    speak("Opening Calculator")
                    print("Opening Calculator ")
                    os.system("calc")
                    print()

            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("chrome" in q) or ("browser" in q)):
                if (("don't" in q) or ("do not" in q)):
                    speak("Okay. I will not open chrome browser")
                    print("Okay. I will not open chrome browser")
                    print()
                else:
                    speak("Opening Chrome Browser")
                    print("Opening Chrome Browser.....")
                    os.system("chrome")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("facebook" in q) or ("fb" in q)):
                if (("don't" in q) or ("do not" in q)):
                    speak("Okay. I will not open Facebook")
                    print("Okay. I will not open facebook")
                    print()
                else:
                    speak("Opening facebook")
                    print("Opening Facebook.....")
                    webbrowser.open("www.facebook.com")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("instagram" in q) or ("insta" in q)):
                if (("don't" in q) or ("do not" in q)):
                    speak("Okay. I will not open Instagram")
                    print("Okay. I will not open Instagram")
                    print()
                else:
                    speak("Opening Instagram")
                    print("Opening Instagram.....")
                    webbrowser.open("www.instagram.com")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("linkedin" in q) or ("linked" in q)):
                if (("don't" in q) or ("do not" in q)):
                    speak("Okay. I will not open LinkedIn")
                    print("Okay. I will not open LinkedIn")
                    print()
                else:
                    speak("Opening LinkedIn")
                    print("Opening LinkedIn.....")
                    webbrowser.open("www.linkedin.com")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and ("youtube" in q):
                if (("don't" in q) or ("do not" in q)):
                    speak("Okay. I will not open YouTube")
                    print("Okay. I will not open YouTube")
                    print()
                else:
                    speak("What you want to see in YouTube")
                    ysearch = takeCommand()
                    print("Searching YouTube.....")
                    kit.playonyt(ysearch)
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and ("google" in q):
                if (("don't" in q) or ("do not" in q)):
                    speak("Okay. I will not open Google")
                    print("Okay. I will not open Google")
                    print()
                else:
                    speak("What you want to see in Google")
                    gsearch = takeCommand()
                    print("Searching Google.....")
                    kit.search(gsearch)
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and ("gmail" in q):
                if (("don't" in q) or ("do not" in q)):
                    speak("Okay. I will not open GMail")
                    print("Okay. I will not open GMail")
                    print()
                else:
                    speak("Opening GMail")
                    print("Opening GMail.....")
                    webbrowser.open("www.gmail.com")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("github" in q) or ("git" in q)):
                if (("don't" in q) or ("do not" in q)):
                    speak("Okay. I will not open GitHub")
                    print("Okay. I will not open github")
                    print()
                else:
                    speak("Opening GitHub")
                    print("Opening GitHub.....")
                    os.system("GitHubDesktop")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("notepad" in q) or ("editor" in q)):
                if (("don't" in q) or ("do not" in q)):
                    speak("Okay. I will not open Notepad Editor")
                    print("Okay. I will not open Notepad Editor")
                    print()
                else:
                    speak("Opening Notepad")
                    print("Opening Notepad.....")
                    os.system("notepad")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and ("sublime" in q):
                if (("don't" in q) or ("do not" in q)):
                    speak(
                        "Okay. I will not open Sublime Text Editor")
                    print("Okay. I will not open Sublime Text Editor")
                    print()
                else:
                    speak("Opening Sublime Text Editor")
                    print("Opening Sublime Text Editor.....")
                    os.system("sublime_text")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("vs " in q) or ("code" in q)):
                if (("don't" in q) or ("do not" in q)):
                    speak(
                        "Okay. I will not open Visual Studio Code Editor")
                    print("Okay. I will not open Visual Studio Code Editor")
                    print()
                else:
                    speak("Opening Visual Studio Code Editor")
                    print("Opening Visual Studio Code Editor.....")
                    os.system("code")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and ("vlc" in q):
                if (("don't" in q) or ("do not" in q)):
                    speak("Okay. I will not open VLC Media Player")
                    print("Okay. I will not open VLC Media Player")
                    print()
                else:
                    speak("Opening VLC Media Player")
                    print("Opening VLC Media Player.....")
                    os.system("vlc")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("window" in q) or ("media" in q) or ("player" in q)):
                if (("don't" in q) or ("do not" in q)):
                    speak(
                        "Okay. I will not open Windows Media Player")
                    print("Okay. I will not open Windows Media Player")
                    print()
                else:
                    speak("Opening Windows Media Player")
                    print("Opening Windows Media Player.....")
                    os.system("wmplayer")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("virtualbox" in q) or ("virtual" in q)):
                if (("don't" in q) or ("do not" in q)):
                    speak(
                        "Okay. I will not open Oracle Virtual Box")
                    print("Okay. I will not open Oracle Virtual Box")
                    print()
                else:
                    speak("Opening Oracle Virtual Box")
                    print("Opening Oracle Virtual Box.....")
                    os.system("VirtualBox")
                    print()
            elif (("sum" in q) or ("add" in q)) and (("show" in q) or ("print" in q)) and ("code" in q):
                if (("don't" in q) or ("do not" in q)):
                    speak(
                        "Okay. I will not show you the code for addition")
                    print("Okay. I will not show you the code for addition")
                    print()
                else:
                    speak("showing code for addition")
                    print(
                        "------------------------------------------------------")
                    print(
                        "numbers = input(\"Enter numbers separated by space \")")
                    print("numberList = numbers.split()")
                    print()
                    print("# Calculating the sum of all user entered numbers")
                    print("sum = 0")
                    print("for num in numberList:")
                    print("sum += int(num)")
                    print("print(\"Sum of all entered numbers = \", sum)")
                    print(
                        "------------------------------------------------------")
                    print()
            elif ("sum" in q) or ("add" in q):
                if (("don't" in q) or ("do not" in q)):
                    speak("Okay. I will not do the addition")
                    print("Ok")
                    print()
                else:
                    speak("Enter numbers separated by space")
                    numbers = input(
                        "Enter numbers separated by space ")
                    numberList = numbers.split()

                    # Calculating the sum of all user entered numbers
                    sum = 0
                    for num in numberList:
                        sum += int(num)
                    print("Sum of all entered numbers = ", sum)
                    print()
            elif (("difference" in q) or ("subtract" in q) or ("sub" in q)) and (("show" in q) or ("print" in q)) and ("code" in q):
                if (("don't" in q) or ("do not" in q)):
                    speak(
                        "Okay. I will not show you the code for subtraction")
                    print(
                        "Okay. I will not show you the code for subtraction")
                    print()
                else:
                    speak("showing code for subtraction")
                    print(
                        "------------------------------------------------------")
                    print(
                        "numbers = input(\"Enter only two numbers separated by space \")")
                    print("numberList = numbers.split()")
                    print()
                    print("# Calculating the difference of two numbers")
                    print()
                    print("diff = int(max(numberList)) - int(min(numberList))")
                    print("print(\"Difference between the two numbers = \", diff)")
                    print(
                        "------------------------------------------------------")
                    print()
            elif ("subtract" in q) or ("difference" in q) or ("diff" in q):
                if (("don't" in q) or ("do not" in q)):
                    speak("Okay. I will not do the subtraction")
                    print("Okay. I will not do the subtraction")
                    print()
                else:
                    speak("Enter only two numbers separated by space")
                    numbers = input(
                        "Enter only two numbers separated by space ")
                    numberList = numbers.split()

                    # Calculating the diff of two numbers

                    diff = int(max(numberList)) - int(min(numberList))
                    print("Difference between the two numbers = ", diff)
                    print()
            elif (("product" in q) or ("multiply" in q)) and (("show" in q) or ("print" in q)) and ("code" in q):
                if (("don't" in q) or ("do not" in q)):
                    speak(
                        "Okay. I will not show you the code for multiplication")
                    print("Ok")
                    print()
                else:
                    speak("showing code for multiplication")
                    print(
                        "------------------------------------------------------")
                    print(
                        "numbers = input(\"Enter numbers separated by space \")")
                    print("numberList = numbers.split()")
                    print()
                    print(
                        "# Calculating the product of all user entered numbers")
                    print("product = 1")
                    print("for num in numberList:")
                    print("product *= int(num)")
                    print(
                        "print(\"Product of all entered numbers = \", product)")
                    print(
                        "------------------------------------------------------")
                    print()
            elif ("product" in q) or ("multiply" in q):
                if (("don't" in q) or ("do not" in q)):
                    speak("Okay. I will not do the multiplication")
                    print("Okay. I will not do the multiplication")
                    print()
                else:
                    speak("Enter numbers separated by space")
                    numbers = input(
                        "Enter numbers separated by space ")
                    numberList = numbers.split()

                    # Calculating the sum of all user entered numbers
                    product = 1
                    for num in numberList:
                        product *= int(num)
                    print("Product of all entered numbers = ", product)
                    print()
            elif (("division" in q) or ("divide" in q)) and (("show" in q) or ("print" in q)) and ("code" in q):
                if (("don't" in q) or ("do not" in q)):
                    speak(
                        "Okay. I will not show you the code for division")
                    print("Okay. I will not show you the code for division")
                    print()
                else:
                    speak("showing code for Division")
                    print(
                        "------------------------------------------------------")
                    print(
                        "numbers = input(\"Enter only two numbers separated by space \")")
                    print("numberList = numbers.split()")
                    print()
                    print("# Calculating the division of two numbers")
                    print()
                    print("div = int(max(numberList)) / int(min(numberList))")
                    print("print(\"Division of two numbers = \", div)")
                    print(
                        "------------------------------------------------------")
                    print()
            elif ("division" in q) or ("divide" in q):
                if (("don't" in q) or ("do not" in q)):
                    speak("Okay. I will not do the division")
                    print("Okay. I will not do the division")
                    print()
                else:
                    speak(
                        "Enter only two numbers separated by space")
                    numbers = input(
                        "Enter only two numbers separated by space ")
                    numberList = numbers.split()

                    # Calculating the division of two numbers

                    div = int(max(numberList)) / int(min(numberList))
                    print("Division of two numbers = ", div)
                    print()
            elif (("play" in q) and (("music" in q) or ("song" in q))):
                speak("Playing Bella Ciao")
                print("Playing Bella Ciao...")
                playsound('songs/BellaCiao (1).mp3')
                print()
            elif 'wikipedia' in q:
                speak('Searching Wikipedia...')
                q = q.replace("wikipedia", "")
                results = wikipedia.summary(q, sentences=2)
                speak('According to wikipedia...')
                print(results)
                speak(results)
            elif 'email ' in q:
                try:
                    speak("Where you want to send email?")
                    to = input("Where you want to send email?")
                    speak("What should I say?")
                    content = takeCommand()
                    sendEmail(to, content)
                    speak("Email has been sent!")
                    print("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak(
                        "Sorry. I am not able to send this email")
            elif ("exit" in q) or ("shutdown" in q) or ("quit" in q) or ("close" in q):
                speak("Okay closing app...")
                print("Closing App.....")
                speak("Have a nice day.")
                print("Have a nice day.")
                print()
                break
            else:
                speak("Please say again")
                print("Please say again!!! ")
                print()

        else:
            if count == 0:
                speak("Non audible")
                speak("You have exceed the permissible limit please try again!")
                speak("I am quitting!")
                break
            else:
                count = count - 1
                print(f"{count} attempt is remaining...")
                speak("Please type your password!")
                pswd = getpass.getpass("Please type password to begin! ")
