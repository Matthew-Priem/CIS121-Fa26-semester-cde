'''
#what is the largest number in the Numbers.txt file?
my_file = open("Numbers.txt", 'r')

data_as_lyst = my_file.readlines()


data_as_lyst = [3,4,12,4,23,5,1]

largest = -1
for number in data_as_lyst:
    number = int(number)
    if number > largest:
        largest = number


print(f"{largest=}")

my_file.close()
'''


'''
family_file = open("Family.csv", "w")

family_file.write("First_name,Last_name,Age,Fav_color\n")
print("tell me about your family.")

done = False
while not done:
    first_name = input("what's their first name: ")
    last_name = input("what is their last name: ")
    age = int(input("how old are they: "))
    color = input("what is their fav color: ")
    #family_file.write(first_name + " " + last_name+ " " + str(age)+ " " + color +"\n")
    family_file.write(f"{first_name},{last_name},{age},{color}\n")
    
    proceed = input("add another member (y/n): ")
    if proceed == "n":
        done = True
'''
'''
#what is the avg age of a person in this family???
family_file = open("Family.csv", 'r')

data = family_file.readlines()[1:]

total = 0
numbers_seen = 0

for line in data:
    line_data = line.split(",")
    #first_name = line_data[0]
    #last_name = line_data[1]
    age = int(line_data[2])
    #fav_color = line_data[3]

    total += age
    numbers_seen += 1

avg = total / numbers_seen
print(avg)
'''

family_file = open("Family.csv", 'r')

data = family_file.readlines()[1:]

student_count_before_AI = 0
student_count_after_AI = 0
total_points_before_AI = 0
total_points_after_AI = 0

for line in data:
    line_data = line.split(",")
    year = int(line_data[5])
    points = int(line_data[4])

    if year >= 2022:
        student_count_after_AI += 1
        total_points_after_AI += points
    else:
        student_count_before_AI += 1
        total_points_before_AI += points

avg_before_AI = total_points_before_AI/student_count_before_AI
avg_after_AI = total_points_after_AI / student_count_after_AI

print(f"{avg_before_AI=}")
print(f"{avg_after_AI=}")