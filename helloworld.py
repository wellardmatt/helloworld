while True:
    user_input = input("Please input your print statement: ")
    print(user_input)
    printmore=input("Would you like to print another statement? Y/N ").upper()
    if printmore=="N":
        exit()