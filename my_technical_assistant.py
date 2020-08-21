import pyttsx3
import os

# pyttsx3.speak("Welcome to my app")
print()
print("                   Hello!! I am your technical assistant.                               ")
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

    if (("run" in p) or ("execute" in p) or ("open" in p)) and (("chrome" in p) or ("browser" in p)):
        if (("don't" in p) or ("do not" in p)):
            print("    Ok")
        else:
            print("    Opening Chrome Browser.....")
            os.system("chrome")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and (("notepad" in p) or ("editor" in p)):
        if (("don't" in p) or ("do not" in p)):
            print("    Ok")
        else:
            print("    Opening Notepad.....")
            os.system("notepad")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("sublime" in p):
        if (("don't" in p) or ("do not" in p)):
            print("    Ok")
        else:
            print("    Opening Sublime Text Editor.....")
            os.system("sublime_text")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and (("vs " in p) or ("code" in p)):
        if (("don't" in p) or ("do not" in p)):
            print("    Ok")
        else:
            print("    Opening Visual Studio Code Editor.....")
            os.system("code")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and (("vlc" in p) and ("media" in p) and ("player" in p)) :
        if (("don't" in p) or ("do not" in p)):
            print("    Ok")
        else:
            print("    Opening VLC Media Player.....")
            os.system("vlc")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and (("window" in p) or ("media" in p) or ("player" in p)):
        if (("don't" in p) or ("do not" in p)):
            print("    Ok")
        else:
            print("    Opening Windows Media Player.....")
            os.system("wmplayer")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and (("virtualbox" in p) or ("virtual" in p)):
        if (("don't" in p) or ("do not" in p)):
            print("    Ok")
        else:
            print("    Opening Oracle Virtual Box.....")
            os.system("VirtualBox")
    elif (("sum" in p) or ("add" in p)) and (("show" in p) or ("print" in p)) and ("code" in p):
        if (("don't" in p) or ("do not" in p)):
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
    elif ("sum" in p) or ("add" in p):
        if (("don't" in p) or ("do not" in p)):
            print("    Ok")
        else:
            numbers = input("    Enter numbers separated by space ")
            numberList = numbers.split()

            # Calculating the sum of all user entered numbers
            sum = 0
            for num in numberList:
                sum += int(num)
            print("    Sum of all entered numbers = ", sum)
    elif (("difference" in p) or ("subtract" in p) or("sub" in p)) and (("show" in p) or ("print" in p)) and ("code" in p):
        if (("don't" in p) or ("do not" in p)):
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
    elif ("subtract" in p) or ("difference" in p) or ("diff" in p):
        if (("don't" in p) or ("do not" in p)):
            print("    Ok")
        else:
            numbers = input("    Enter only two numbers separated by space ")
            numberList = numbers.split()

            # Calculating the diff of two numbers
            
            diff = int(max(numberList)) - int(min (numberList))
            print("    Difference between the two numbers = ", diff)
    elif (("product" in p) or ("multiply" in p)) and (("show" in p) or ("print" in p)) and ("code" in p):
        if (("don't" in p) or ("do not" in p)):
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
    elif ("product" in p) or ("multiply" in p):
        if (("don't" in p) or ("do not" in p)):
            print("    Ok")
        else:
            numbers = input("    Enter numbers separated by space ")
            numberList = numbers.split()

            # Calculating the sum of all user entered numbers
            product = 1
            for num in numberList:
                product *= int(num)
            print("    Product of all entered numbers = ", product)
    elif (("division" in p) or ("divide" in p)) and (("show" in p) or ("print" in p)) and ("code" in p):
        if (("don't" in p) or ("do not" in p)):
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
    elif ("division" in p) or ("divide" in p):
        if (("don't" in p) or ("do not" in p)):
            print("    Ok")
        else:
            numbers = input("    Enter only two numbers separated by space ")
            numberList = numbers.split()

            # Calculating the division of two numbers
            
            div = int(max(numberList)) / int(min (numberList))
            print("    Division of two numbers = ", div)
    elif ("exit" in p) or ("shutdown" in p) or ("quit" in p):
        print("    Closing App.....")
        break
    else:
        print("    Please write proper command")
