# adding name

a = input("What's your name? ")

# adding year of birth
b = input("Enter a birth year? ")

# adding message
c = input("Enter personalized message ")

# adding senders name
d = input("Enter senders name ")

# import datetime
from datetime import date


# defining the for calculating the age, the function takes day
def calculate_age(day, month, year):
    # we are getting the current date using the today()
    today = date.today()
    # converting year, month and day into birthdate
    birthdate = date(year, month, day)
    # calculating the age
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    # return the age value
    return age


# the try/except block
try:
    # we are getting day, month, and year using input() function
    day = input("Enter day: ")
    month = input("Enter month: ")
    year = input("Enter year: ")
    # creating a variable called age_result and we are also calling the calculate_age function
    age = calculate_age(int(day), int(month), int(year))
    print(f"You are {age} years old ")
# the except will catch all errors
except:
    print(f'Failed to calculate age, either day or month or year is invalid')

print("Hi " + a)

print("let's celebrate your " + str(age))

print("years of awesomeness!")

print("Wishing you a day filled with joy and laughter as you turn " + str(age))

print(c)

print("With love and best wishes,")

print(d)
