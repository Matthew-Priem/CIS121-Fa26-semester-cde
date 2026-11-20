#store in a list all the even number between 
#10 and 33 inclusively 




#for number in range(10, 33+1):
#    if number % 2 == 0:
#        number_list.append(number)

def report_evens(lower_bound, upper_bound):
    number_list = []
    number = lower_bound
    while number <= upper_bound:
        if number % 2 == 0:
            number_list.append(number)
        number += 1

    return number_list


#print(report_evens(10,33))
#print(report_evens(1,3))



lyst1 = ['a','b','c']
lyst2 = lyst1
lyst3 = []
for element in lyst1:
    lyst3.append(element)

lyst4 = []

index = 0
while index < len(lyst1):
    lyst4.append(lyst1[index])
    index += 1


#print(lyst1)
#print(lyst2)
#print(lyst3)
#print(lyst4)

lyst2[1] = 'd'

#print("\n  ------------ \n")

#print(lyst1)
#print(lyst2)
#print(lyst3)


#create a list that includes the names
#of every person at your table and
#include me in the list.

#write a function that takes a list 
# as an argument
# and returns a new
#list that contains all the names 
#who have more than 5 letters in their
#name



def name_filter(old_lyst):
    new_list = []
    for name in name_lyst:
        if len(name) >= 5:
            new_list.append(name)
    return new_list

name_lyst = ['matthew', 'ivan']
print(name_filter(name_lyst))