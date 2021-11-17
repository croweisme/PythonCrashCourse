#I want to make a symple program using loops and lists that lets me choose between 
#Printing the list
#and appending a new item to the list 

#So how am I gonna structure this?
#I could use my notes from the bagels game

#functions I need:
#Main menu
#Viewing the list
#Appending the list 
list = ['one','two','three','four']
def main():
    #print all the menu options here
    print("MAIN MENU:")
    print("Print List: 1\nAdd to List: 2\nStop Program: 3")
    response = input()
    while True:
        if response == '1':
            print("Youve chosen option 1")
            printList()
            break
        if response == '2':
            appendList()
            break
        if response == '3':
            print("You've chosen to stop the program")
            break
        else:
            print("Youve entered an invalid option")
            main()
            break
        break

def printList():
    print(list)
    print("Would you like to return to the main menu? (Y/N")
    goback = input('')
    while True:

        if goback.lower() == 'y':
            main()
            break
        else:
            print("You've chosen to stop the program")
            break

def appendList():
    #create program to append list here
    while True:
        list.append(input("Enter new item: "))
        print(list)
        print("Would you like to return to the main menu? (Y/N")
        goback = input('')
        while True:

            if goback.lower() == 'y':
                main()
                break
            else:
                print("You've chosen to stop the program")
                break
        break

    
main()

