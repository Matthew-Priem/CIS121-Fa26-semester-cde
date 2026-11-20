'''
my_number = 3
import random

#.txt   .csv
#my_file = open("file_name.ext", "r/w")
my_file = open("Numbers.txt", "w")

#add stuff to it.

#let's add 100 random numbers to the file
#with those numbers between 10 and 1500
for count in range(100):
    random_number = random.randint(10,1500)
    my_file.write(str(random_number) + "\n")

my_file.close()
'''


my_numbers = [4,5,1,8,14]

#write code to find the avg of my_numbers

total = 0
numbers_seen = 0

for number in my_numbers:
    total += number
    numbers_seen += 1

avg = total / numbers_seen

#my_file = open("Numbers.txt", "r")

#read gets the entire file contents
#and returns it as a sting
#data = my_file.read()
#print(data)

#data = "1337\n1389\n251\n..."

#readline() gets the next line of
#the file and returns it as a str
#data = my_file.readline()
#print(data)

#readlines() gets the entire files
#content and returns a list of lines
#seperated by \n
#data = my_file.readlines()
#print(data)


my_file = open("Numbers.txt", "r")

data = my_file.readlines()

for line in data:
    line_data = line.split(",")

class Chair:
    def split():
        pass

total = 0
numbers_seen = 0

for number in data:
    total += int(number)
    numbers_seen += 1

avg = total / numbers_seen
print(avg)

my_file.close()




