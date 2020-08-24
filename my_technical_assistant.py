import pyttsx3
import os
from playsound import playsound
import speech_recognition as sr

engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                      # printing current voice rate
engine.setProperty('rate', 180)     # setting up new voice rate

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


print()
print("                   Hello!! I am your technical assistant.                               ")
print("                   --------------------------------------                               ")
print()
pyttsx3.speak("Hello!! I am your technical assistant.")
pyttsx3.speak("Can you please tell me your name?")
name = input("                   Can you please tell me your name? ")
print("                  ------------------------------------------")
print("                   Welcome to technical assistant ", name)
print("                  ------------------------------------------")
pyttsx3.speak(f"Welcome to technical assistant {name}")

print()
print(" ______________________________________________________________________________________ ")
print("|______________________________________________________________________________________|")
print("|                                                                                      |")
print("|I will do the following things for you -->                                            |")
pyttsx3.speak("I will do the following things for you")
print("|-----------------------------------------------------                                 |")
print("|I can open -->                                                                        |")
print("|               Chome Browser                                                          |")
print("|               Notepad editor                                                         |")
print("|               VLC Media Player                                                       |")
print("|               Oracle Virtual Box                                                     |")
print("|               Sublime Text Editor                                                    |")
print("|               Windows Media Player                                                   |")
print("|               Visual Studio Code Editor                                              |")
print("|-----------------------------------------------------                                 |")
print("|I can do arithmetic operations -->                                                    |")
print("|                                   Addition                                           |")
print("|                                   Subtraction                                        |")
print("|                                   Multiplication                                     |")
print("|                                   Division                                           |")
print("|-----------------------------------------------------                                 |")
print("|I can show u the code for doing Arithmetic Operations for -->                         |")
print("|                                                              Addition                |")
print("|                                                              Subtraction             |")
print("|                                                              Multiplication          |")
print("|                                                              Division                |")
print("|______________________________________________________________________________________|")
print()
pyttsx3.speak(f"Hi {name}, How can I help you? ")

while True:

    print("    Hi "+name + ", How can I help you? ", end='')
    p = input()
    q = p.lower()
    if (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("chrome" in q) or ("browser" in q)):
        if (("don't" in q) or ("do not" in q)):
            pyttsx3.speak("Okay. I will not open chrome browser")
            print("    Okay. I will not open chrome browser")
            print()
        else:
            pyttsx3.speak("Opening Chrome Browser")
            print("    Opening Chrome Browser.....")
            os.system("chrome")
            print()
    elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("notepad" in q) or ("editor" in q)):
        if (("don't" in q) or ("do not" in q)):
            pyttsx3.speak("Okay. I will not open Notepad Editor")
            print("    Okay. I will not open Notepad Editor")
            print()
        else:
            pyttsx3.speak("Opening Notepad")
            print("    Opening Notepad.....")
            os.system("notepad")
            print()
    elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and ("sublime" in q):
        if (("don't" in q) or ("do not" in q)):
            pyttsx3.speak("Okay. I will not open Sublime Text Editor")
            print("    Okay. I will not open Sublime Text Editor")
            print()
        else:
            pyttsx3.speak("Opening Sublime Text Editor")
            print("    Opening Sublime Text Editor.....")
            os.system("sublime_text")
            print()
    elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("vs " in q) or ("code" in q)):
        if (("don't" in q) or ("do not" in q)):
            pyttsx3.speak(
                "Okay. I will not open Visual Studio Code Editor")
            print("    Okay. I will not open Visual Studio Code Editor")
            print()
        else:
            pyttsx3.speak("Opening Visual Studio Code Editor")
            print("    Opening Visual Studio Code Editor.....")
            os.system("code")
            print()
    elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("vlc" in q) and ("media" in q) and ("player" in q)):
        if (("don't" in q) or ("do not" in q)):
            pyttsx3.speak("Okay. I will not open VLC Media Player")
            print("    Okay. I will not open VLC Media Player")
            print()
        else:
            pyttsx3.speak("Opening VLC Media Player")
            print("    Opening VLC Media Player.....")
            os.system("vlc")
            print()
    elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("window" in q) or ("media" in q) or ("player" in q)):
        if (("don't" in q) or ("do not" in q)):
            pyttsx3.speak("Okay. I will not open Windows Media Player")
            print("    Okay. I will not open Windows Media Player")
            print()
        else:
            pyttsx3.speak("Opening Windows Media Player")
            print("    Opening Windows Media Player.....")
            os.system("wmplayer")
            print()
    elif (("run" in q) or ("execute" in q) or ("open" in q) or ("start" in q)) and (("virtualbox" in q) or ("virtual" in q)):
        if (("don't" in q) or ("do not" in q)):
            pyttsx3.speak("Okay. I will not open Oracle Virtual Box")
            print("    Okay. I will not open Oracle Virtual Box")
            print()
        else:
            pyttsx3.speak("Opening Oracle Virtual Box")
            print("    Opening Oracle Virtual Box.....")
            os.system("VirtualBox")
            print()
    elif (("sum" in q) or ("add" in q)) and (("show" in q) or ("print" in q)) and ("code" in q):
        if (("don't" in q) or ("do not" in q)):
            pyttsx3.speak(
                "Okay. I will not show you the code for addition")
            print("    Okay. I will not show you the code for addition")
            print()
        else:
            pyttsx3.speak("showing code for addition")
            print("    ------------------------------------------------------")
            print("    numbers = input(\"Enter numbers separated by space \")")
            print("    numberList = numbers.split()")
            print()
            print("    # Calculating the sum of all user entered numbers")
            print("    sum = 0")
            print("    for num in numberList:")
            print("        sum += int(num)")
            print("    print(\"Sum of all entered numbers = \", sum)")
            print("    ------------------------------------------------------")
            print()
    elif ("sum" in q) or ("add" in q):
        if (("don't" in q) or ("do not" in q)):
            pyttsx3.speak("Okay. I will not do the addition")
            print("    Ok")
            print()
        else:
            pyttsx3.speak("Enter numbers separated by space")
            numbers = input("    Enter numbers separated by space ")
            numberList = numbers.split()

            # Calculating the sum of all user entered numbers
            sum = 0
            for num in numberList:
                sum += int(num)
            print("    Sum of all entered numbers = ", sum)
            print()
    elif (("difference" in q) or ("subtract" in q) or ("sub" in q)) and (("show" in q) or ("print" in q)) and ("code" in q):
        if (("don't" in q) or ("do not" in q)):
            pyttsx3.speak(
                "Okay. I will not show you the code for subtraction")
            print("    Okay. I will not show you the code for subtraction")
            print()
        else:
            pyttsx3.speak("showing code for subtraction")
            print("    ------------------------------------------------------")
            print(
                "    numbers = input(\"Enter only two numbers separated by space \")")
            print("    numberList = numbers.split()")
            print()
            print("    # Calculating the difference of two numbers")
            print()
            print("    diff = int(max(numberList)) - int(min(numberList))")
            print("    print(\"Difference between the two numbers = \", diff)")
            print("    ------------------------------------------------------")
            print()
    elif ("subtract" in q) or ("difference" in q) or ("diff" in q):
        if (("don't" in q) or ("do not" in q)):
            pyttsx3.speak("Okay. I will not do the subtraction")
            print("    Okay. I will not do the subtraction")
            print()
        else:
            pyttsx3.speak("Enter only two numbers separated by space")
            numbers = input(
                "    Enter only two numbers separated by space ")
            numberList = numbers.split()

            # Calculating the diff of two numbers

            diff = int(max(numberList)) - int(min(numberList))
            print("    Difference between the two numbers = ", diff)
            print()
    elif (("product" in q) or ("multiply" in q)) and (("show" in q) or ("print" in q)) and ("code" in q):
        if (("don't" in q) or ("do not" in q)):
            pyttsx3.speak(
                "Okay. I will not show you the code for multiplication")
            print("    Ok")
            print()
        else:
            pyttsx3.speak("showing code for multiplication")
            print("    ------------------------------------------------------")
            print("    numbers = input(\"Enter numbers separated by space \")")
            print("    numberList = numbers.split()")
            print()
            print("    # Calculating the product of all user entered numbers")
            print("    product = 1")
            print("    for num in numberList:")
            print("        product *= int(num)")
            print("    print(\"Product of all entered numbers = \", product)")
            print("    ------------------------------------------------------")
            print()
    elif ("product" in q) or ("multiply" in q):
        if (("don't" in q) or ("do not" in q)):
            pyttsx3.speak("Okay. I will not do the multiplication")
            print("    Okay. I will not do the multiplication")
            print()
        else:
            pyttsx3.speak("Enter numbers separated by space")
            numbers = input("    Enter numbers separated by space ")
            numberList = numbers.split()

            # Calculating the sum of all user entered numbers
            product = 1
            for num in numberList:
                product *= int(num)
            print("    Product of all entered numbers = ", product)
            print()
    elif (("division" in q) or ("divide" in q)) and (("show" in q) or ("print" in q)) and ("code" in q):
        if (("don't" in q) or ("do not" in q)):
            pyttsx3.speak(
                "Okay. I will not show you the code for division")
            print("    Okay. I will not show you the code for division")
            print()
        else:
            pyttsx3.speak("showing code for Division")
            print("    ------------------------------------------------------")
            print(
                "    numbers = input(\"Enter only two numbers separated by space \")")
            print("    numberList = numbers.split()")
            print()
            print("    # Calculating the division of two numbers")
            print()
            print("    div = int(max(numberList)) / int(min(numberList))")
            print("    print(\"Division of two numbers = \", div)")
            print("    ------------------------------------------------------")
            print()
    elif ("division" in q) or ("divide" in q):
        if (("don't" in q) or ("do not" in q)):
            pyttsx3.speak("Okay. I will not do the division")
            print("    Okay. I will not do the division")
            print()
        else:
            pyttsx3.speak("Enter only two numbers separated by space")
            numbers = input(
                "    Enter only two numbers separated by space ")
            numberList = numbers.split()

            # Calculating the division of two numbers

            div = int(max(numberList)) / int(min(numberList))
            print("    Division of two numbers = ", div)
            print()
    elif (("play" in q) and (("music" in q) or ("song" in q))):
        pyttsx3.speak("Playing Bella Ciao")
        print("    Playing Bella Ciao...")
        playsound('songs/BellaCiao (1).mp3')
        print()
    elif ("exit" in q) or ("shutdown" in q) or ("quit" in q):
        pyttsx3.speak("Okay closing app...")
        print("    Closing App.....")
        pyttsx3.speak("Have a nice day.")
        print("    Have a nice day.")
        print()
        break
    else:
        pyttsx3.speak("Please write proper command")
        print("    Please write proper command")
        print()
