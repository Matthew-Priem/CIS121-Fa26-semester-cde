num1 = 3
#f(x) = ((3x-1) / 2 )^3

num1 = num1 * 3
num1 = num1 - 1
num1 = num1 / 2
num1 = num1 ** 3
#print(x)


#print("hello")
#print("hello", "world")


#to make a custom function we write
def name_of_function(zero_or_more_parameters):
    #do stuff
    pass


def math_fctn(number):
    number = number * 3
    number = number + 1
    number = number / 2
    number = number ** 3
    print(number)
    
#math_fctn(3)
#math_fctn(-2)
#math_fctn(10)

#write a function that take a number and 
#prints EVEN if the number is even, and 
#prints ODD if the number is odd. 
#name the fuction even_or_odd
#test it by invoking your function by passing in 
#the numbers, 2,7,-3,10,0

def even_or_odd(number):
    if number % 2 == 0:
        print("EVEN")
    else:
        print("ODD")


#even_or_odd(2)
#even_or_odd(7)
#even_or_odd(-3)
#even_or_odd(10)
#even_or_odd(0)


def make_bigger(num1, num2):
    if num1 < num2:
        num1 += 1
    else:
        num2 += 1
    print(f'{num1=}, {num2=}')


num1 = 3
num2 = 7

#make_bigger(num1,num2)
#print(f'{num1=}, {num2=}')


#print True is letter is a vowel

word = "apple"

#the way to get information from a function is with the
#keyword return
def is_vowel(letter_that_is_cool):
    if letter_that_is_cool == 'a':
        return True
    elif letter_that_is_cool == 'e':
        return True
    elif letter_that_is_cool == 'i':
        return True
    elif letter_that_is_cool == 'o':
        return True
    elif letter_that_is_cool == 'u':
        return True

def vowel_counter(word):
    count = 0
    for letter in word:
        if is_vowel(letter):
            count += 1
    print(count)

word1 = 'apple'
word2 = 'banana'
word3 = 'watermelon'

vowel_counter(word1)
vowel_counter(word2)
vowel_counter(word3)