"""
Birthday Weekday Finder

The program will ask the user for their birthdate and the year. The program will then calculate the day of the week that the date falls on and display the result.

By Matthew Larsen
Created on 3/9/2026
"""

from datetime import date

# get birthday from user with input validation
def get_birthday():

    valid = False

    while valid == False:

        year = int(input("Enter birth year: "))
        month = int(input("Enter birth month (1-12): "))
        day = int(input("Enter birth day: "))

        if month >= 1 and month <= 12 and day >= 1 and day <= 31:
            valid = True
        else:
            print("Invalid date. Please try again.")

    birthday = date(year, month, day)

    return birthday


# calculate next birthday
def next_birthday(birthday):

    today = date.today()

    next_bday = date(today.year, birthday.month, birthday.day)

    if next_bday < today:
        next_bday = date(today.year + 1, birthday.month, birthday.day)

    days_until = (next_bday - today).days

    return days_until


# save history
def save_history(text):

    file = open("history.txt", "a")

    file.write(text)
    file.write("\n")

    file.close()


# show history
def show_history():

    file = open("history.txt", "a")
    file.close()

    file = open("history.txt", "r")

    print("\nPrevious Searches:")

    for line in file:
        print(line)

    file.close()


running = True

while running:

    print("\nBirthday Program")
    print("1. Check birthday")
    print("2. View previous searches")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        birthday = get_birthday()

        days_until = next_birthday(birthday)

        weekday_number = birthday.weekday()

        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        weekday_name = days[weekday_number]

        print("Your birthday is:", birthday)
        print("You were born on a:", weekday_name)
        print("Your next birthday will happen in", days_until, "days.")

        save_history(str(birthday) + " - " + weekday_name + " - " + str(days_until) + " days")

    elif choice == "2":

        show_history()

    elif choice == "3":

        running = False
        print("Goodbye.")

    else:

        print("Invalid choice.")