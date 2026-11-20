'''
a movie theater charges seats by in the following way
3 and under are free
youth (less than 18) are $12
senior discount: (65 and up) $15
regular 18+ $20
military: $10
write a program that asks the user for their info 
    and outputs the ticket price


military = input("Have you served in the military? (y/n): ")

if military == "y":
    price = 10
else:
    age = int(input("enter your age: "))
    if age <= 3:
        price = 0
    elif age < 18:
        price = 12
    elif age >= 65:
        price = 15
    else:
        price = 20

print(f"ticket price is {price}.")
'''

'''
number = int(input("Please enter your favorite number < 10: "))



if number < 10:
    print(f"{number} is a cool number.")
else:
    print("you didn't follow the instructions. please pick a number < 10.")
'''


#print all the numbers between 1 and 10000000 inclusively. 

#number = 1
#while number <= 100000:
#    print(number)
#    number = number + 1

#number = 0
#while number < 10:
#    number = number + 1
#    print(number)
    


#print all of the even numbers between 5 and 32.

#lower_bound = int(input("enter lower bound: "))
#upper_bound = int(input("enter upper bound: "))

'''
number = 5
while number <= 32:
    if number % 2 == 0:
        print(number)
    number = number + 1

print("end of program.")
'''


