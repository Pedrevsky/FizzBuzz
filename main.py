from printing_service import view_rules, view_information
from game import play

CHOICE = """
Welcome to FizzBuzz game!
What would you do?
- p) to play
- i) to see information 
- r) to see rules
- q) to quit

Write your choice here: """


def menu():
    choice = input(CHOICE).lower()
    while choice != "q":
        if choice == "i":
            view_information()
        
        elif choice == "r":
            view_rules()

        elif choice == "p":
            play()

        else:
            print("Something went wrong, you made a wrong choice")

        choice = input(CHOICE).lower()


menu()
