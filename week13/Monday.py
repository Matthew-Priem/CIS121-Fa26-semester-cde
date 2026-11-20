'''
for voter in lyst:
    if voter.age < 20 and voter.age > 40:
        young_count += 1
'''

import random
#.txt OR .csv

#my_file = open("file_name.ext","r/w")
my_file = open("Numbers.txt", "w")


#let's add 100 random numbers to this file between 10,560
for index in range(10000):
    rand = random.randint(10,2560)

    
    my_file.write( str(rand) + "\n" )


my_file.close()
#more code to do...

"""
number_lyst = [3,5, 123, 6, 8]

total = 0
numbers_seen = 0

for number in number_lyst:
    total += number
    numbers_seen += 1

avg = total / numbers_seen
"""

#my_file = open("Numbers.txt", 'r')

#read gets the entire file contents
#and returns it as a sting
#data = my_file.read()
#print(data)
#data = "165\n107\n99\n344..."

#readline() gets the next line of
#the file and returns it as a str
#data = my_file.readline()
#print(data)

#readlines() gets the entire file
#content and returns a list of lines
#seperated by \n
#data = my_file.readlines()
#print(data)


#what is the avg value of the numbers in Numbers.txt file?
'''
my_file = open("Numbers.txt", 'r')

data_as_lyst = my_file.readlines()

total = 0
numbers_seen = 0

for number in data_as_lyst:
    total += int(number)
    numbers_seen += 1

avg = total / numbers_seen

print(avg)

my_file.close()
'''

    