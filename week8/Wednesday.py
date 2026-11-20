def greeting(name, age):
    msg = ""
    msg += f"hello {name}. "

    #if they didn't provide age, skip this line
    if age != "unknown":
        msg += f"It is cool being {age} years old."
    return msg

#print(greeting("Dexter", 9))
#print(greeting(9, "Dexter"))
#print(greeting("Eugene"))

#print(greeting())

#write a function that caluculates the area of a
#square or a rectangle based on parameters.
#if one parameter is passed it is a square, and if
#two parameters are passed it is a rectangle.
#return the area. 


def calc_area(side1, side2 = "missing"):
    if side2 is "missing":
        area = side1 ** 2
    else:
        area = side1 * side2
    return area

#print(calc_area(4)) #16
#print(calc_area(5,6)) #30


def fctn_name(p1, p2, p3, p4, p5 = 'a', p6 = 'b', p7 = 'c'):
    pass


fctn_name(1,2,3,4)

fctn_name(p2=7,p1=3,p4=8,p5=9,p3=10)

word = "cats and     dog & apples and bananas"
word_lyst = word.split(sep = " ", maxsplit = 4)

word_lyst2 = word.split(" ", 4)

word_lyst3 = word.split(maxsplit=4)


print(word_lyst)
print(word_lyst2)
print(word_lyst3)



print("lsdfjdlk", end= " ")

