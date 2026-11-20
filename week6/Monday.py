'''
#print each word in the sentance. 

sentance = """Sunshine warms the garden as a cheerful puppy chases a bright yellow butterfly across the grass."""

word = ""

for letter in sentance:
    if letter == " ":
        print(word)
        word = ""
    elif letter == '.':
        print(word)
        word = ""
    else:
        word = word + letter
'''

#to initialize a list we use [] with the data we want inside
#seperated by ,


lyst = ["apple", 4, "bana!a", 3.1, True, "lunch time"]

x = "3"

y = int(x)

#print(  lyst[2:5]   )

#print(lyst)

#for element in lyst:
#    print(element)

x = lyst[2]

x[4]


#print( lyst[2][4] )




sentance = """Sunshine warms the garden as a cheerful puppy chases a bright yellow butterfly across the grass."""

word = ""
word_list = []

for letter in sentance:
    if letter == " ":
        word_list.append(word)
        word = ""
    elif letter == '.':
        word_list.append(word)
        word = ""
    else:
        word = word + letter

#print(word_list)


#store in a list all the even number between 
#10 and 33 inclusively 


number_list = []


#for number in range(10, 33+1):
#    if number % 2 == 0:
#        number_list.append(number)

number = 10
while number <= 33:
    if number % 2 == 0:
        number_list.append(number)
    
    number += 1

print(number_list)





