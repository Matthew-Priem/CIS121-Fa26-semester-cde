#using a for loop, print the number 1..10

#number = 1
#while number <= 10:
#    print(number)
#    number = number + 1

#for number in range(1,10+1):
#    print(number)

#for number in range(1,11):
#    print(number)


#lower_bound = int(input("enter lower bound: "))
#upper_bound = int(input("enter upper bound: "))

#for number in range(lower_bound, upper_bound + 1):
#    print(number)


#print the odd numbers between 4 and 37 (inlusively).
#for number in range(4,37+1):
#    if number % 2 == 1:
#        print(number)

#for number in range(5,37+1,2):
#    print(number)

#for number in range(10):
#    print(number)

#word = "apple"

#print( word[123]  )


#print(f"the length of {word} is {len(word)}.")

#for index in range(len(word)+1):
#    print()


word = 'apples and bananas are good.'

x = word[5]
y = word[10]
z = word[14]

#print(f'{x=}, {y=}, {z=}')

#print(word[0:5])

'''
letter = '?'

if letter == 'a':
    print(letter)
elif letter == 'e':
    print(letter)
elif letter == 'i':
    print(letter)
elif letter == 'o':
    print(letter)
elif letter == 'u':
    print(letter)


word = "apple"

for letter in word:
    print(letter)

print("---------")

for index in range(len(word)):
    print(index)

print("---------")

for index in range(len(word)):
    print(word[index])



word = "apples and bananas"

count = 0

for letter in word:
    if letter == 'a':
        print(letter)
    elif letter == 'e':
        print(letter)
    elif letter == 'i':
        print(letter)
    elif letter == 'o':
        print(letter)
    elif letter == 'u':
        print(letter)
'''
'''
word = "apples and bananas"

count = 0

for letter in word:
    if letter == 'a':
        count = count + 1
    elif letter == 'e':
        count += 1
    elif letter == 'i':
        count += 1
    elif letter == 'o':
        count += 1
    elif letter == 'u':
        count += 1

print(f"there are {count} vowel in the word '{word}'.")


vowels = ['a','e','i','o','u']
vowels = 'aeiou'

for letter in word:
    if letter in word:
        print(letter)


for letter in word:
    for vowel in vowels:
        if letter == vowel:
            print(letter)
'''

for number in range(4,15):
    print(f"{number:2.2f}")

for i in range(1,10):
    for j in range(1,10):
        print(f"({i:.1f},{j})", end= " ")
    print("")




word = "apple"

for letter in word:
    print(letter)

print("---------")

for index in range(len(word)):
    print(index)

print("---------")

for index in range(len(word)):
    print(word[index])


index = 0
while index < len(word):
    print(word[index])
    index += 1


