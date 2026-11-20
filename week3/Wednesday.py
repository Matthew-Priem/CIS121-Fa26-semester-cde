'''
user_number = int(input("enter a number: "))


if user_number < 10:
    print("you picked a number less than 10.")
else:
    print("you picked a number >= 10.")


if user_number < 10:
    print("you picked a number less than 10.")

print("end of program.")
'''

#prompt the user for a number.
#a small number is less than 25
#a large number is greater or equal to 25 and less than 100.
#a huge number is greater or equal to than 100 and < 500
#a gigantic number is >= 500.
#inform the user if they picked a large or small number. user_number = int(input("enter a number: "))

user_number = int(input("Enter a number: "))

'''
if user_number < 25:
    print("you picked a small number.")
else:
    print("you picked a large number.")
'''
'''
if user_number < 25:
    print("you picked a small number.")
if user_number >= 25 and user_number < 100:
    print("you picked a large number.")


if user_number < 25:
    print("you picked a small number.")
else: #everywhere in this block of code, user_number >= 25
    if user_number < 100:
        print("you picked a large number.")
    else:#everywhere in this block of code, user_number>=100
        if user_number < 500:
            print("you picked a huge number")
        else:
            print("you picked a gigantic number")


if user_number < 25:
    print("you picked a small number.")
elif user_number < 100:
    print("you picked a large number.")
elif user_number < 500:
    print("you picked a huge number.")
else:
    print("you picked a gigantic number.")



print("end of program.")
'''

'''
a movie theater charges seats by in the following way
3 and under are free
youth (less than 18) are $12
senior discount: (65 and up) $15
regular 18+ $20
military: $10
write a program that asks the user for their info 
    and outputs the ticket price
'''

military = input("Did you serve in the milatary? (y/n): ")

if military == "y" or military == "yes":
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

print(f'your ticket price is {price}')
