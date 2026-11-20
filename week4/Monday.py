#print the numbers 1..1000 (inclusively)
'''
number = 1
while number <= 10:    
    print(number)
    number = number + 1

number = 0
while number < 10:
    number = number + 1
    print(number)
    


print("end of program")


#print all the even numbers between 3 and 54 (inclusively)

number = 3
while number <= 54:
    print(number)
    number = number + 2


lower_bound = int(input("pick a lower bound: "))
upper_bound = int(input("pick a upper bound: "))

number = lower_bound
while number <= upper_bound:
    #if number is even:
    #if the reminder is 0:
    if number % 2 == 0:
        print(number)
    number = number + 1

print("end of program")
'''


#print then number 1..10 (inclusively)
'''
for number in range(1,10+1):
    print(number)
for number in range(1,11):
    print(number)

lower_bound = int(input("pick a lower bound: "))
upper_bound = int(input("pick a upper bound: "))

for number in range(lower_bound, upper_bound + 1):
    print(number)
'''
for number in range(10):
    print(number)