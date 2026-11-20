'''
grades_file = open("FakeGrades.csv", 'w')

import random

grades_file.write("first_name,last_name,grade,tech_id,year\n")

for count in range(700):
    grade = random.randint(60,100)
    year = random.randint(2018,2026)
    grades_file.write(f"name,???,{grade},???,{year}\n")


grades_file.close()
'''

'''
#what is the largest number in the Numbers.txt file?

number_file = open("Numbers.txt", 'r')

data = number_file.readlines()

#data ['831', '646', '2044',...]

largest = -1
for line in data:
    num = int(line)
    if num > largest:
        largest = num

print(largest)
'''
'''
family_file = open("Family.csv",'w')

family_file.write("first_name,last_name,age,favorite_color\n")
done = False
while not done:
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = int(input("enter age: "))
    fav_color = input("Favorite color: ")

    family_file.write(f"{first_name},{last_name},{age},{fav_color}\n")

    proceed = input("Enter another? (y/n): ")
    if proceed == 'n':
        done = True
'''
"""
family_file = open("Family.csv",'r')

data = family_file.readlines()[1:]
#print(data)

total = 0
numbers_seen = 0

for line in data:
    line_data = line.split(",")
    ##print(line_data)
    #first_name = line_data[0]
    #last_name = line_data[1]
    age = int(line_data[2])
    #fav_color = line_data[3]

    total += age
    numbers_seen += 1
avg = total / numbers_seen
print(avg)
"""

my_file = open("FakeGrades.csv", 'r')

data = my_file.readlines()[1:]

student_count_before_AI = 0
student_count_after_AI = 0
total_points_before_AI = 0
total_points_after_AI = 0

for line in data:
    line_data = line.split(",")
    year = int(line_data[4])
    points = int(line_data[2])

    if year >= 2022:
        total_points_after_AI += points
        student_count_after_AI += 1
    else:
        total_points_before_AI += points
        student_count_before_AI += 1

avg_before_AI = total_points_before_AI / student_count_before_AI
avg_after_AI = total_points_after_AI / student_count_after_AI

print(f"{avg_after_AI=}")
print(f"{avg_before_AI=}")