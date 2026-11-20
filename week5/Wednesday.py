#cos_id = 1
#user_name = input("Enter name: ")
#user_name += str(f"id = {cos_id}")

x = 3
#f(x) = ((3x+1) / 2 )^3


def name(variable):
    #do stuff
    #everything you want must be at this
    #indentation level
    pass

def math_fctn(number):
    number *= 3
    number += 1
    number /= 2
    number = number**3
    print(number)
    
def salary_calc(sales, salary):
    if sales < 1000000:
        return salary * 1.03
    else:
        return salary * 1.03 + 10000

#math_fctn(3)
#math_fctn(-2)
#math_fctn(10)

#write a function named even_or_odd
#that takes an integer number and prints
#EVEN if the number is even and
#ODD if the number is odd.
#test it with the number 3, 6, 10, -2, and 0.

def even_or_odd(number):
    if number % 2 == 0:
        print("EVEN")
    else:
        print("ODD")

#even_or_odd(10)
#even_or_odd(2)
#even_or_odd(3)
#even_or_odd(-1)


def bigger_number(num1, num2):
    if num1 < num2:
        num1 += 1
    else:
        num2 += 1
    print(f"{num1=}, {num2=}")

num1 = 3
num2 = 7

#bigger_number(num1, num2)
#print(f"{num1=}, {num2=}")


def is_vowel(letter):
    #this should print true or false
    if letter == 'a':
        return True
    elif letter == 'e':
        return True
    elif letter == 'i':
        return True
    elif letter == 'o':
        return True
    elif letter == 'u':
        return True


#to give information back from a function,
#we use the keyword return. 

word1 = "banana"
word2 = "apple"
word3 = "watermelon"

def vowel_counter(some_word):

    count = 0
    for letter in some_word:
        #if letter is a vowel
        if is_vowel(letter):
            count += 1

    print(f"there are {count} many vowels in {some_word}")


done = False
while not done:
    vowel_counter(input("pick a word: "))
    user_input = input("do you want to pick another word (y/n): ")
    if user_input == 'n':
        done = True

vowel_counter(word2)
vowel_counter(word3)