import random
from datetime import datetime

BOT_NAME = "Astra"

quotes = ["Success comes to those who never stop learning.","Dream big and work hard.","Believe in yourself.","Practice makes perfect."]

jokes = ["Why do programmers love Python? Because it's easy to understand!","Why did the computer get cold? It forgot to close Windows.","Debugging is like being a detective in your own code."]

def welcome():
    print("=" * 50)
    print("      ASTRA - RULE BASED CHATBOT")
    print("=" * 50)
    print("Welcome! I am Astra. ")
    print()
    


def menu():
    print("\n------ MENU ------")
    print("1. Hello")
    print("2. About")
    print("3. Date")
    print("4. Time")
    print("5. Calculator")
    print("6. Quote")
    print("7. Joke")
    print("8. Help")
    print("9. Exit")


def about():
    print("\nI am a Rule-Based Chatbot.")
    print("I was developed using Python.")
    print("This project was created for the CODSOFT AI Internship Task 1.")


def show_date():
    today = datetime.now()
    print("\nToday's Date:", today.strftime("%d-%m-%Y"))


def show_time():
    now = datetime.now()
    print("\nCurrent Time:", now.strftime("%I:%M:%S %p"))


def calculator():
    print("\nSimple Calculator")
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+ - * /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            print("Result =", num1 + num2)

        elif operator == "-":
            print("Result =", num1 - num2)

        elif operator == "*":
            print("Result =", num1 * num2)

        elif operator == "/":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print("Result =", num1 / num2)

        else:
            print("Invalid operator.")

    except:
        print("Invalid Input")


def show_quote():
    print("\nQuote:")
    print(random.choice(quotes))


def show_joke():
    print("\nJoke:")
    print(random.choice(jokes))


def help_menu():
    print("\nYou can use the following options:")
    print("Hello - Greeting")
    print("About - About the chatbot")
    print("Date - Shows current date")
    print("Time - Shows current time")
    print("Calculator - Performs calculations")
    print("Quote - Displays a motivational quote")
    print("Joke - Displays a programming joke")
    print("Exit - Closes the chatbot")


# Main Program Starts Here

welcome()

name = input("Enter your name: ").title()

print(f"\nHello {name}! Nice to meet you.")
menu()

while True:

    choice = input("\nEnter your choice: ").strip().lower()

    if choice == "1" or choice == "hello":
        print(f"\n{BOT_NAME}: Hello {name}! How can I help you today?")

    elif choice == "2" or choice == "about":
        about()

    elif choice == "3" or choice == "date":
        show_date()

    elif choice == "4" or choice == "time":
        show_time()

    elif choice == "5" or choice == "calculator":
        calculator()

    elif choice == "6" or choice == "quote":
        show_quote()

    elif choice == "7" or choice == "joke":
        show_joke()

    elif choice == "8" or choice == "help":
        help_menu()

    elif choice == "9" or choice == "exit":
        print("\nThank you for using SmartBot.")
        print("Have a great day!")
        break

    elif choice == "hi":
        print(f"\n{BOT_NAME}: Hi {name}! Nice to see you.")

    elif choice == "how are you":
        print(f"\n{BOT_NAME}: I'm doing great. Thanks for asking!")

    elif choice == "thanks" or choice == "thank you":
        print(f"\n{BOT_NAME}: You're welcome!")

    else:
        print(f"\n{BOT_NAME}: Sorry, I didn't understand that command.")
        print("Type 'help' or '8' to see the available commands.")
