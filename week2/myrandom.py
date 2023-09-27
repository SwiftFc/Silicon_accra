import random

#randint
#randrange
#choice
#shuffle

student_name = ["Kristal" "Henry", "Stephen", "Abena", 
                "Precious", 
                "Nehemiah"]

student_name.extend(["Maya",
                     "Caleb"])

#Before Shuffling

for i in student_name:
    print(i)


for name in student_name:
    print("The names of student are:", name)

random.shuffle(student_name)
for name in student_name:
    print("\nThe shuffle names are:", name)

new = random.choice(student_name)

print("The random name is:", new)



