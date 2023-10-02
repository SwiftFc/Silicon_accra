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

user = int(input("Guess any Number from 1 to 5: "))


x = [1,2,3,4,5]

x = random.choice(x)

if user == x:
	print("Successful Guess")

else:
	print(f"The computerised random number is:", x)
