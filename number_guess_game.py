import random

"""
main - A program where a computer generates
a random number and a user has to guess the number
"""
"""
Keywords - random, number,
user input, guess,
while loop, 
conditions, 
range
"""

print("Hello Silicon Accra\n")
print("Welcome to the Number Guessing Game!!!\n")

while True:
    user_name = input("Enter Your Name to get started: ")

    if user_name.isalpha() != True:
        print("\nInvalid ***  Expecting Characters only")
    else:
        print("Login Successful")
        break


print("\nGuess any Number from 1 to 10")

guess = 0
max_guess = 8

computer_num = random.randint(1, 10)
while guess < max_guess:
    try:
        user = input("Guess any Number from 1 to 10: ")
        guess_num = int(user)
        if guess_num == computer_num:
            print("Successful Guess!!!")
            break
        elif guess_num < computer_num:
            print("Guess a Higher number")
        else:
            print("Guess a lower number")

        guess += 1

    except ValueError:
        print("Invalid")

if guess_num != computer_num:
    print("\nSorry, Max Guessses Reached")
    print("\n\n*********EXIT**************")
