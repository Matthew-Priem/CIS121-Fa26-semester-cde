def add_to_lyst(lyst, lower_bound, upper_bound):
    for number in range(lower_bound, upper_bound + 1):
        lyst.append(number)

def other_adder(lyst, lower_bound, upper_bound):
    other_lyst = lyst
    for number in range(lower_bound, upper_bound + 1):
        other_lyst.append(number)
    return other_lyst


numbers = []

#add_to_lyst(numbers, 1, 10)
#print(numbers)

new_lyst = other_adder(numbers, 1, 10)
#print(numbers)
#print(new_lyst)


#add_to_lyst(numbers, 4,8)
#print(numbers)

def find_large_value(cust_dict):
    high_spenders = cust_dict
    for customer in high_spenders:
        if cust_dict[customer] < 10:
            high_spenders[customer] = 0
    return high_spenders


customers = {"matt": 50, "ashley": 5}
high_spenders = find_large_value(customers)

#print(customers)
#print(high_spenders)


def add_to_word(word):
    word += "!"
    return word

#x = "cat"
#x = x + "!"
#y = add_to_word(x)

#print(x)
#print(y)

'''
word = "azples"
print(word)
word[1] = 'p'
print(word)
'''

#lyst = ['apples', 'bannnnnanas', 'kiwi']
#print(lyst)

#lyst[1] = 'bananas'
#print(lyst)

#a tuple is like a list, but immutable.
#a tuple is created with () and initial values are assigned
#by putting them in the () seperated by ,
days_of_the_week = ("M", "T", "W", "TH", "F", "Sa","Su")
#days_of_the_week[1] = "video game day"
#days_of_the_week.append("video game day")

#print(days_of_the_week)

#wacky = print

#wacky("hello world")



def add_three(x):
    y = x + 3
    return y

var0 = 7
var1 = add_three(var0)

print(y)


