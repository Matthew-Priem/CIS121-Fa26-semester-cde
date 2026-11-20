def greeting(name, age = "unknown"):
    msg = ""
    msg += f"hello {name}. "

    #if they didn't provide age, skip this line
    if age != "unknown":
        msg += f"It is cool being {age} years old."
    #elif age == "unknown":
    #    pass
    return msg

"""
def greeting(name, age):
    msg = f"Hello {name}. It is cool being {age} years old."
    return msg

def greeting (name):
    msg = f"hello {name}."
    return msg


print(greeting("Dexter", 9))
print(greeting(7, "Eugene"))

print(greeting("Cameron"))
"""

#write a function that caluculates the area of a
#square or a rectangle based on parameters.
#if one parameter is passed it is a square, and if
#two parameters are passed it is a rectangle.
#return the area. 

def calc_area(side1, side2 = "missing"):
    if side2 == "missing":
        area = side1 * side1
    else:
        area = side1 * side2
    return area

#print(calc_area(4))     #16
#print(calc_area(5,6))   #30

# Write a function that calculates the volume of a
# cube or a rectangular prism based on parameters.
# If one parameter is passed, it is a cube.
# If three parameters are passed, it is a rectangular prism.
# Return the volume.




def fctn_name(p1, p2, p3, p4, p5 = 'a', p6 = 'b', p7 = 'c'):
    pass

fctn_name(1,2,3,4,5)

fctn_name(p2=8,p1=7,p6=5,p3=10,p4=17)


#print("hello world", end=" ")

#print


#for i in range(1,10):
#    for j in range(1,5):
#        print(i*j, end="&")
#    print()

print("apple", "banana", "watermelon", "kiwi",sep=",", end="&")
print("apple", "banana", "watermelon", "kiwi")




def greeting(name:str, age:int = -1):
    """This function produces a friendly greeting"""
    msg = ""
    msg += f"hello {name}. "

    #if they didn't provide age, skip this line
    if age < 0:
        msg += f"It is cool being {age} years old."
    #elif age == "unknown":
    #    pass
    return msg




