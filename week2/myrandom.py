#Take the list of students in Silicon Accra Class
#print out the total number of students
#shuffle the list of students
#pick a random student out of the list
#add a 2 new student to the list

import random
student_name = ["Kristal",
                "Henry",
                "Abena",
                "Stanley",
                "Nehemiah",
                "Precious",
                "Stephen",
                "praiz",
                "Stanley"]

for name in student_name:
    print(name)

x = student_name.index("Abena")
print("\n", x)

random.shuffle(student_name)
for name in student_name:
    print("\nThe shuflle list is:", name)

new = random.choice(student_name)

print("\nThe random choice is:", new)
