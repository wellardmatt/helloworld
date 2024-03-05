user=input("Please input your name: ")

with open("printstatements.txt",'a') as file:
    file.write(f'{user}\n')
    while True:
        user_input = input("Please input your print statement: ")
        print(user_input)
        file.write(f'\t{user_input}\n')
        printmore=input("Would you like to print another statement? Y/N ").upper()
        if printmore=="N":
            file.write('\n')
            exit()
    