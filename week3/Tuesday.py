#a small number is < 10.
#a large number is >= 10 and < 100
#a huge number is >= 100
#a gigantic number is > 345






'''
user_number = int(input("Enter a number: "))

if user_number < 10:
    print("you picked a small number")

if user_number >= 10 and user_number < 100:
    print("you picked a large number")


print("end of program")
'''


user_number = int(input("Enter a number: "))

if user_number < 10:
    print("you picked a small number")
else: # everything in this block is greater than or equal to 10.
    if user_number < 100:
        print("you picked a large number")
    else: # everthing in this block is greater than or equal to 100
        if user_number <= 345:
            print("you picked a huge number")
        else:
            print("you picked a gigantic number")


if user_number < 10:
    print("you picked a small number")
elif user_number < 100:
    print("you picked a large number")
elif user_number <= 345:
    print("you picked a huge number")
else:
    print("you picked a gigantic number")







'''
produces the wrong answer.
if user_number < 10:
    print("you picked a small number")
if user_number < 100:
    print("you picked a large number")
if user_number <= 345:
    print("you picked a huge number")
else:
    print("you picked a gigantic number")
'''









print("end of program")