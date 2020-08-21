import pyttsx3
import os

# pyttsx3.speak("Welcome to my app")

print()
print("Press 1: to open chrome browser")
print("Press 2: to open notepad")
print("Press 3: to open media player")
print()

print("Enter your choice : ", end='')
p = int(input())

if p == 1:
    os.system("chrome")
elif p == 2:
    os.system("notepad")
elif p == 3:
    os.system("wmplayer")
else:
    print("Please write valid number")
