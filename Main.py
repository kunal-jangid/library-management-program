import Return
import ListSplit
import dt
import Borrow

def start():
    while(True):
        print("------------------------------------------------------")
        print("        Welcome to the Liibrary Management System     ")
        print("------------------------------------------------------")
        print("Choose '1' to display the Books List")
        print("Choose '2' to borrow a book")
        print("Choose '3' to return a book")
        print("Choose '4' to exit")
        try:
            a=int(input("Select a choice from 1-4: "))
            print()
            if(a==1):
                with open("stock.txt","r") as f:
                    lines=f.read()
                    print(lines)
                    print ()
   
            elif(a==2):
                ListSplit.listSplit()
                Borrow.borrowBook()
            elif(a==3):
                ListSplit.listSplit()
                Return.returnBook()
            elif(a==4):
                print("Thank you for using library management system")
                break
            else:
                print("Please enter a valid choice from 1-4")
        except ValueError:
            print("Please input as suggested.")
start()
