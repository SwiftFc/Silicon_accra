import random

"""
main - A program where a computer generates
a random number and a user has to guess the number
"""

"""
Keywords - random, number,
user input, guess,
for loop, 
conditions, 
range
"""
print("Hello Silicon Accra\n")
print("Welcome to the Number Guessing Game!!!\n")

print("Hello Silicon Accra\n")
print("Welcome to the Number Guessing Game!!!\n")

input("Enter Your Name to get started: ")
print("\nGuess any Number from 1 to 20")

user = int(input("Guess any Number from 1 to 5: "))


x = [1,2,3,4,5]

a = input("Guess the Number: ")

a = int(a)

x = (1, 20)
guess = 0
x = random.randint(1, 20)
for i in range(3):
    if a == x:
        print("Successful Guess!")
        break

else:   
    print("Incorrect Guess")
    guess += 1

if guess == 3:
    print("Correct Number is", x)
if user == x:
	print("Successful Guess")

else:
	print(f"The computerised random number is:", x)
