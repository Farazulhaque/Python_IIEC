import pyttsx3
import os
import getpass
from playsound import playsound
import speech_recognition as sr

engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                      # printing current voice rate
engine.setProperty('rate', 180)     # setting up new voice rate

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


print()
print("\t\tHello!! I am your technical assistant.")
pyttsx3.speak("Hello!! I am your technical assistant.")
print("\t\t--------------------------------------")
print()
print("\t\t--------------------------------------")
pyttsx3.speak("Can you please tell me your name?")
name = input("\t\tCan you please tell me your name? ")
print("\t\t------------------------------------------")
pyttsx3.speak("Please type your password : ")
pwd = getpass.getpass("\t\tPlease type your password : ")
print("\t\t------------------------------------------")
if name == "Faraz":
    if pwd == "abc123":
        print("\t\tWelcome to technical assistant ", name)
        print("\t\t------------------------------------------")
        pyttsx3.speak(f"Welcome to technical assistant {name}")

        print()
        print("\t\t________________________________________________________________________________________")
        print("\t\t|                                                                                      |")
        print("\t\t|I will do the following things for you -->                                            |")
        pyttsx3.speak("I will do the following things for you")
        print("\t\t|-----------------------------------------------------                                 |")
        print("\t\t|I can show u -->                                                                      |")
        print("\t\t|                 Current Time                                                         |")
        print("\t\t|                 Today's date                                                         |")
        print("\t\t|-----------------------------------------------------                                 |")
        print("\t\t|I can open -->                                                                        |")
        print("\t\t|               GMail                                                                  |")
        print("\t\t|               GitHub                                                                 |")
        print("\t\t|               YouTube                                                                |")
        print("\t\t|               Facebook                                                               |")
        print("\t\t|               LinkedIn                                                               |")
        print("\t\t|               Instagram                                                              |")
        print("\t\t|               Calculator                                                             |")
        print("\t\t|               Chome Browser                                                          |")
        print("\t\t|               Notepad editor                                                         |")
        print("\t\t|               VLC Media Player                                                       |")
        print("\t\t|               Oracle Virtual Box                                                     |")
        print("\t\t|               Sublime Text Editor                                                    |")
        print("\t\t|               Windows Media Player                                                   |")
        print("\t\t|               Visual Studio Code Editor                                              |")
        print("\t\t|-----------------------------------------------------                                 |")
        print("\t\t|I can do arithmetic operations -->                                                    |")
        print("\t\t|                                   Addition                                           |")
        print("\t\t|                                   Subtraction                                        |")
        print("\t\t|                                   Multiplication                                     |")
        print("\t\t|                                   Division                                           |")
        print("\t\t|-----------------------------------------------------                                 |")
        print("\t\t|I can show u the code for doing Arithmetic Operations for -->                         |")
        print("\t\t|                                                              Addition                |")
        print("\t\t|                                                              Subtraction             |")
        print("\t\t|                                                              Multiplication          |")
        print("\t\t|                                                              Division                |")
        print("\t\t|______________________________________________________________________________________|")
        print()
        pyttsx3.speak(f"Hi {name}, How can I help you? ")

        while True:

            print("\t\tHi "+name + ", How can I help you? ", end='')
            p = input()
            q = p.lower()
            if (("date" in q) and ("today" in q)):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak("Okay. I will not show u today's date")
                    print("\t\tOkay. I will not show u today's date")
                    print()
                else:
                    pyttsx3.speak("Today's date is")
                    print("\t\tToday's date is : ")
                    os.system("date /T")
                    print()
            elif (("time" in q) or ("tym" in q)):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak("Okay. I will not show u current time")
                    print("\t\tOkay. I will not show u current time")
                    print()
                else:
                    pyttsx3.speak("Current time is")
                    print("\t\tCurrent time is : ")
                    os.system("time /T")
                    print()
            elif (("calc" in q) or ("calculator" in q)):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak("Okay. I will not open calculator")
                    print("\t\tOkay. I will not open calculator")
                    print()
                else:
                    pyttsx3.speak("Opening Calculator")
                    print("\t\tOpening Calculator ")
                    os.system("calc")
                    print()

            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("chrome" in q) or ("browser" in q)):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak("Okay. I will not open chrome browser")
                    print("\t\tOkay. I will not open chrome browser")
                    print()
                else:
                    pyttsx3.speak("Opening Chrome Browser")
                    print("\t\tOpening Chrome Browser.....")
                    os.system("chrome")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("facebook" in q) or ("fb" in q)):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak("Okay. I will not open Facebook")
                    print("\t\tOkay. I will not open facebook")
                    print()
                else:
                    pyttsx3.speak("Opening facebook")
                    print("\t\tOpening Facebook.....")
                    os.system("chrome facebook.com")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("instagram" in q) or ("insta" in q)):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak("Okay. I will not open Instagram")
                    print("\t\tOkay. I will not open Instagram")
                    print()
                else:
                    pyttsx3.speak("Opening Instagram")
                    print("\t\tOpening Instagram.....")
                    os.system("chrome instagram.com")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("linkedin" in q) or ("linked" in q)):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak("Okay. I will not open LinkedIn")
                    print("\t\tOkay. I will not open LinkedIn")
                    print()
                else:
                    pyttsx3.speak("Opening LinkedIn")
                    print("\t\tOpening LinkedIn.....")
                    os.system("chrome linkedin.com")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and ("youtube" in q):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak("Okay. I will not open YouTube")
                    print("\t\tOkay. I will not open YouTube")
                    print()
                else:
                    pyttsx3.speak("Opening YouTube")
                    print("\t\tOpening YouTube.....")
                    os.system("chrome youtube.com")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and ("gmail" in q):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak("Okay. I will not open GMail")
                    print("\t\tOkay. I will not open GMail")
                    print()
                else:
                    pyttsx3.speak("Opening GMail")
                    print("\t\tOpening GMail.....")
                    os.system("chrome gmail.com")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("github" in q) or ("git" in q)):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak("Okay. I will not open GitHub")
                    print("\t\tOkay. I will not open github")
                    print()
                else:
                    pyttsx3.speak("Opening GitHub")
                    print("\t\tOpening GitHub.....")
                    os.system("GitHubDesktop")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("notepad" in q) or ("editor" in q)):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak("Okay. I will not open Notepad Editor")
                    print("\t\tOkay. I will not open Notepad Editor")
                    print()
                else:
                    pyttsx3.speak("Opening Notepad")
                    print("\t\tOpening Notepad.....")
                    os.system("notepad")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and ("sublime" in q):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak("Okay. I will not open Sublime Text Editor")
                    print("\t\tOkay. I will not open Sublime Text Editor")
                    print()
                else:
                    pyttsx3.speak("Opening Sublime Text Editor")
                    print("\t\tOpening Sublime Text Editor.....")
                    os.system("sublime_text")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("vs " in q) or ("code" in q)):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak(
                        "Okay. I will not open Visual Studio Code Editor")
                    print("\t\tOkay. I will not open Visual Studio Code Editor")
                    print()
                else:
                    pyttsx3.speak("Opening Visual Studio Code Editor")
                    print("\t\tOpening Visual Studio Code Editor.....")
                    os.system("code")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and ("vlc" in q):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak("Okay. I will not open VLC Media Player")
                    print("\t\tOkay. I will not open VLC Media Player")
                    print()
                else:
                    pyttsx3.speak("Opening VLC Media Player")
                    print("\t\tOpening VLC Media Player.....")
                    os.system("vlc")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("window" in q) or ("media" in q) or ("player" in q)):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak("Okay. I will not open Windows Media Player")
                    print("\t\tOkay. I will not open Windows Media Player")
                    print()
                else:
                    pyttsx3.speak("Opening Windows Media Player")
                    print("\t\tOpening Windows Media Player.....")
                    os.system("wmplayer")
                    print()
            elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("virtualbox" in q) or ("virtual" in q)):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak("Okay. I will not open Oracle Virtual Box")
                    print("\t\tOkay. I will not open Oracle Virtual Box")
                    print()
                else:
                    pyttsx3.speak("Opening Oracle Virtual Box")
                    print("\t\tOpening Oracle Virtual Box.....")
                    os.system("VirtualBox")
                    print()
            elif (("sum" in q) or ("add" in q)) and (("show" in q) or ("print" in q)) and ("code" in q):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak(
                        "Okay. I will not show you the code for addition")
                    print("\t\tOkay. I will not show you the code for addition")
                    print()
                else:
                    pyttsx3.speak("showing code for addition")
                    print("\t\t------------------------------------------------------")
                    print("\t\tnumbers = input(\"Enter numbers separated by space \")")
                    print("\t\tnumberList = numbers.split()")
                    print()
                    print("\t\t# Calculating the sum of all user entered numbers")
                    print("\t\tsum = 0")
                    print("\t\tfor num in numberList:")
                    print("\t\tsum += int(num)")
                    print("\t\tprint(\"Sum of all entered numbers = \", sum)")
                    print("\t\t------------------------------------------------------")
                    print()
            elif ("sum" in q) or ("add" in q):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak("Okay. I will not do the addition")
                    print("\t\tOk")
                    print()
                else:
                    pyttsx3.speak("Enter numbers separated by space")
                    numbers = input("\t\tEnter numbers separated by space ")
                    numberList = numbers.split()

                    # Calculating the sum of all user entered numbers
                    sum = 0
                    for num in numberList:
                        sum += int(num)
                    print("\t\tSum of all entered numbers = ", sum)
                    print()
            elif (("difference" in q) or ("subtract" in q) or ("sub" in q)) and (("show" in q) or ("print" in q)) and ("code" in q):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak(
                        "Okay. I will not show you the code for subtraction")
                    print("\t\tOkay. I will not show you the code for subtraction")
                    print()
                else:
                    pyttsx3.speak("showing code for subtraction")
                    print("\t\t------------------------------------------------------")
                    print(
                        "numbers = input(\"Enter only two numbers separated by space \")")
                    print("\t\tnumberList = numbers.split()")
                    print()
                    print("\t\t# Calculating the difference of two numbers")
                    print()
                    print("\t\tdiff = int(max(numberList)) - int(min(numberList))")
                    print("\t\tprint(\"Difference between the two numbers = \", diff)")
                    print("\t\t------------------------------------------------------")
                    print()
            elif ("subtract" in q) or ("difference" in q) or ("diff" in q):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak("Okay. I will not do the subtraction")
                    print("\t\tOkay. I will not do the subtraction")
                    print()
                else:
                    pyttsx3.speak("Enter only two numbers separated by space")
                    numbers = input(
                        "Enter only two numbers separated by space ")
                    numberList = numbers.split()

                    # Calculating the diff of two numbers

                    diff = int(max(numberList)) - int(min(numberList))
                    print("\t\tDifference between the two numbers = ", diff)
                    print()
            elif (("product" in q) or ("multiply" in q)) and (("show" in q) or ("print" in q)) and ("code" in q):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak(
                        "Okay. I will not show you the code for multiplication")
                    print("\t\tOk")
                    print()
                else:
                    pyttsx3.speak("showing code for multiplication")
                    print("\t\t------------------------------------------------------")
                    print("\t\tnumbers = input(\"Enter numbers separated by space \")")
                    print("\t\tnumberList = numbers.split()")
                    print()
                    print("\t\t# Calculating the product of all user entered numbers")
                    print("\t\tproduct = 1")
                    print("\t\tfor num in numberList:")
                    print("\t\tproduct *= int(num)")
                    print("\t\tprint(\"Product of all entered numbers = \", product)")
                    print("\t\t------------------------------------------------------")
                    print()
            elif ("product" in q) or ("multiply" in q):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak("Okay. I will not do the multiplication")
                    print("\t\tOkay. I will not do the multiplication")
                    print()
                else:
                    pyttsx3.speak("Enter numbers separated by space")
                    numbers = input("\t\tEnter numbers separated by space ")
                    numberList = numbers.split()

                    # Calculating the sum of all user entered numbers
                    product = 1
                    for num in numberList:
                        product *= int(num)
                    print("\t\tProduct of all entered numbers = ", product)
                    print()
            elif (("division" in q) or ("divide" in q)) and (("show" in q) or ("print" in q)) and ("code" in q):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak(
                        "Okay. I will not show you the code for division")
                    print("\t\tOkay. I will not show you the code for division")
                    print()
                else:
                    pyttsx3.speak("showing code for Division")
                    print("\t\t------------------------------------------------------")
                    print(
                        "numbers = input(\"Enter only two numbers separated by space \")")
                    print("\t\tnumberList = numbers.split()")
                    print()
                    print("\t\t# Calculating the division of two numbers")
                    print()
                    print("\t\tdiv = int(max(numberList)) / int(min(numberList))")
                    print("\t\tprint(\"Division of two numbers = \", div)")
                    print("\t\t------------------------------------------------------")
                    print()
            elif ("division" in q) or ("divide" in q):
                if (("don't" in q) or ("do not" in q)):
                    pyttsx3.speak("Okay. I will not do the division")
                    print("\t\tOkay. I will not do the division")
                    print()
                else:
                    pyttsx3.speak("Enter only two numbers separated by space")
                    numbers = input(
                        "Enter only two numbers separated by space ")
                    numberList = numbers.split()

                    # Calculating the division of two numbers

                    div = int(max(numberList)) / int(min(numberList))
                    print("\t\tDivision of two numbers = ", div)
                    print()
            elif (("play" in q) and (("music" in q) or ("song" in q))):
                pyttsx3.speak("Playing Bella Ciao")
                print("\t\tPlaying Bella Ciao...")
                playsound('songs/BellaCiao (1).mp3')
                print()
            elif ("exit" in q) or ("shutdown" in q) or ("quit" in q):
                pyttsx3.speak("Okay closing app...")
                print("\t\tClosing App.....")
                pyttsx3.speak("Have a nice day.")
                print("\t\tHave a nice day.")
                print()
                break
            else:
                pyttsx3.speak("Please write proper command")
                print("\t\tPlease write proper command")
                print()
    else:
        pyttsx3.speak("Your password is incorrect")
        print("\t\tYour password is incorrect")
else:
    pyttsx3.speak("Your user name is incorrect")
    print("\t\tYour user name is incorrect")
