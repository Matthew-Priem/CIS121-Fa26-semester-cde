#write a program that ask the user their name and age
#and then prints the output.



'''
print("start here")

try:
    name = input("enter name: ")
    age = int(input("enter age: "))
    print(f"hello {name}. you are {age} years old.")
except ValueError:
    print("something went wacky!")


    
print("end here")
'''

class No3sError(Exception):
    pass




#let the user pick a number.
#then divide 10 by the user's number
print("start here")

done = False
while not done:
    try:
        user_number = int(input("enter number: "))
        if user_number == 3:
            raise No3sError
        result = 10 / user_number
        print(result)
        done = True
    except ZeroDivisionError:
        print("can't pick 0.")
    except ValueError:
        print("must pick an int")
    except No3sError:
        print("can't pick a 3")
    except Exception:
        print("something went wacky!")


print("end here")