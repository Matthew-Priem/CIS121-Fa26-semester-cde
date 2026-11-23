#write a program that ask the user their name and age
#and then prints the output.

'''
print("start here")

name = input("enter name: ")

done = False
while not done:
    try:
        age = int(input("enter age: "))
        print(f"hello {name}. You are {age} years old.")
        done = True
    except ValueError:
        print("please write response as an int.")
    except TypeError:
        print("something is funky. Type error.")
    except NameError:
        print("something is funky. Name error.")

print("end here")
'''

class No3sError(Exception):
    pass


#write a program that asks the user for a number
#then print 10 divided by their number.
#new rule. Don't let the user divide by 3.
print("start")

done = False
while not done:
    try:
        user_number = int(input("enter number: "))
        if user_number == 3:
            #start panicing!!!
            raise No3sError

        result = 10 / user_number
        print(result)
        done = True
    except ValueError:
        print("You must type an int")
    except ZeroDivisionError:
        print("you can't pick 0.")
    except No3sError:
        print("you can't pick 3.")
    except Exception:
        print("Something went wacky! Unknown error.")


print("end")
#ValueError
#ZeroDivisionError



