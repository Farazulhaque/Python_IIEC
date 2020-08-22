import pyttsx3
import os


print()

print("                   Hello!! I am your technical assistant.                               ")
pyttsx3.speak("Hello!! I am your technical assistant.")
print("                   --------------------------------------                               ")
print("|______________________________________________________________________________________|")
print("|                                                                                      |")
print("|I will do the following things for you -->                                            |")
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
name = input("    Can you please tell me your name?  ")
print("    ------------------------------------------")
print("    Welcome to technical assistant ",name)
print("    ------------------------------------------")
print()
while True:
    print("    Hi "+name + ", How can I help you? ", end='')
    p = input()

    if (("run" in p.lower()) or ("execute" in p.lower()) or ("open" in p.lower())) and (("chrome" in p.lower()) or ("browser" in p.lower())):
        if (("don't" in p.lower()) or ("do not" in p.lower())):
            print("    Ok")
        else:
            print("    Opening Chrome Browser.....")
            os.system("chrome")
    elif (("run" in p.lower()) or ("execute" in p.lower()) or ("open" in p.lower())) and (("notepad" in p.lower()) or ("editor" in p.lower())):
        if (("don't" in p.lower()) or ("do not" in p.lower())):
            print("    Ok")
        else:
            print("    Opening Notepad.....")
            os.system("notepad")
    elif (("run" in p.lower()) or ("execute" in p.lower()) or ("open" in p.lower())) and ("sublime" in p.lower()):
        if (("don't" in p.lower()) or ("do not" in p.lower())):
            print("    Ok")
        else:
            print("    Opening Sublime Text Editor.....")
            os.system("sublime_text")
    elif (("run" in p.lower()) or ("execute" in p.lower()) or ("open" in p.lower())) and (("vs " in p.lower()) or ("code" in p.lower())):
        if (("don't" in p.lower()) or ("do not" in p.lower())):
            print("    Ok")
        else:
            print("    Opening Visual Studio Code Editor.....")
            os.system("code")
    elif (("run" in p.lower()) or ("execute" in p.lower()) or ("open" in p.lower())) and (("vlc" in p.lower()) and ("media" in p.lower()) and ("player" in p.lower())) :
        if (("don't" in p.lower()) or ("do not" in p.lower())):
            print("    Ok")
        else:
            print("    Opening VLC Media Player.....")
            os.system("vlc")
    elif (("run" in p.lower()) or ("execute" in p.lower()) or ("open" in p.lower())) and (("window" in p.lower()) or ("media" in p.lower()) or ("player" in p.lower())):
        if (("don't" in p.lower()) or ("do not" in p.lower())):
            print("    Ok")
        else:
            print("    Opening Windows Media Player.....")
            os.system("wmplayer")
    elif (("run" in p.lower()) or ("execute" in p.lower()) or ("open" in p.lower())) and (("virtualbox" in p.lower()) or ("virtual" in p.lower())):
        if (("don't" in p.lower()) or ("do not" in p.lower())):
            print("    Ok")
        else:
            print("    Opening Oracle Virtual Box.....")
            os.system("VirtualBox")
    elif (("sum" in p.lower()) or ("add" in p.lower())) and (("show" in p.lower()) or ("print" in p.lower())) and ("code" in p.lower()):
        if (("don't" in p.lower()) or ("do not" in p.lower())):
            print("    Ok")
        else:
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
    elif ("sum" in p.lower()) or ("add" in p.lower()):
        if (("don't" in p.lower()) or ("do not" in p.lower())):
            print("    Ok")
        else:
            numbers = input("    Enter numbers separated by space ")
            numberList = numbers.split()

            # Calculating the sum of all user entered numbers
            sum = 0
            for num in numberList:
                sum += int(num)
            print("    Sum of all entered numbers = ", sum)
    elif (("difference" in p.lower()) or ("subtract" in p.lower()) or("sub" in p.lower())) and (("show" in p.lower()) or ("p.lower()rint" in p.lower())) and ("code" in p.lower()):
        if (("don't" in p.lower()) or ("do not" in p.lower())):
            print("    Ok")
        else:
            print("    ------------------------------------------------------")
            print("    numbers = input(\"Enter only two numbers separated by space \")")
            print("    numberList = numbers.split()")
            print()
            print("    # Calculating the difference of two numbers")
            print()
            print("    diff = int(max(numberList)) - int(min(numberList))")
            print("    print(\"Difference between the two numbers = \", diff)")
            print("    ------------------------------------------------------")
    elif ("subtract" in p.lower()) or ("difference" in p.lower()) or ("diff" in p.lower()):
        if (("don't" in p.lower()) or ("do not" in p.lower())):
            print("    Ok")
        else:
            numbers = input("    Enter only two numbers separated by space ")
            numberList = numbers.split()

            # Calculating the diff of two numbers
            
            diff = int(max(numberList)) - int(min (numberList))
            print("    Difference between the two numbers = ", diff)
    elif (("product" in p.lower()) or ("multiply" in p.lower())) and (("show" in p.lower()) or ("print" in p.lower())) and ("code" in p.lower()):
        if (("don't" in p.lower()) or ("do not" in p.lower())):
            print("    Ok")
        else:
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
    elif ("product" in p.lower()) or ("multiply" in p.lower()):
        if (("don't" in p.lower()) or ("do not" in p.lower())):
            print("    Ok")
        else:
            numbers = input("    Enter numbers separated by space ")
            numberList = numbers.split()

            # Calculating the sum of all user entered numbers
            product = 1
            for num in numberList:
                product *= int(num)
            print("    Product of all entered numbers = ", product)
    elif (("division" in p.lower()) or ("divide" in p.lower())) and (("show" in p.lower()) or ("print" in p.lower())) and ("code" in p.lower()):
        if (("don't" in p.lower()) or ("do not" in p.lower())):
            print("    Ok")
        else:
            print("    ------------------------------------------------------")
            print("    numbers = input(\"Enter only two numbers separated by space \")")
            print("    numberList = numbers.split()")
            print()
            print("    # Calculating the division of two numbers")
            print()
            print("    div = int(max(numberList)) / int(min(numberList))")
            print("    print(\"Division of two numbers = \", div)")
            print("    ------------------------------------------------------")
    elif ("division" in p.lower()) or ("divide" in p.lower()):
        if (("don't" in p.lower()) or ("do not" in p.lower())):
            print("    Ok")
        else:
            numbers = input("    Enter only two numbers separated by space ")
            numberList = numbers.split()

            # Calculating the division of two numbers
            
            div = int(max(numberList)) / int(min (numberList))
            print("    Division of two numbers = ", div)
    elif ("exit" in p.lower()) or ("shutdown" in p.lower()) or ("quit" in p.lower()):
        print("    Closing App.....")
        break
    else:
        print("    Please write proper command")
