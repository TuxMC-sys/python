print("Which length do you need for the right triangle")

while True:
    userInput: str = input(
        "Hit H for the height(opposite, W for the width(adjacent) A for the angled edge(hypotenuse) or Q to "
        "exit: ").upper()

    if userInput == "H":
        angle = input("What is the angled edge for your shape: ")
        width = input("What is the width for your shape: ")
        hOut = float(width)/float(angle)
        print(hOut)
    elif userInput == "W":
        height = input("What is the height for your shape:")
        angle = input("What is the angled edge for your shape: ")
        wOut = float(height)/float(angle)
        print(wOut)
    elif userInput == "A":
        height = input("What is the height for your shape:")
        width = input("What is the width for your shape: ")
        aOut = float(height)/float(width)
        print(aOut)
    elif userInput == "Q":
        break
    else:
        print("Check your input")
