'''
#print each word in the sentance. 

sentance = """Sunshine warms the garden as a cheerful puppy chases a 
bright yellow butterfly across the grass."""

word = ""
for letter in sentance:
    if letter == " ":        
        print(word)
        word = ""
    elif letter == ".":        
        print(word)
        word = ""
    else:
        word += letter


#to initialize a list we use [] with the data we want inside
#seperated by ,

sentance = """Sunshine warms the garden as a cheerful puppy chases a 
bright yellow butterfly across the grass."""

data = ['apple', 5, 'banana', True, 2.3, """Sunshine warms the garden as a cheerful puppy chases a 
bright yellow butterfly across the grass."""]

#print(data)

#for info in data:
#	print(info)

#index = 0
#while index < len(data):
#	print(data[index])
#	index += 1

word = ""    
for letter in data[5]:
    if letter == " ":        
        print(word)
        word = ""
    elif letter == ".":        
        print(word)
        word = ""
    else:
        word += letter

word = ""
for letter in sentance:
    if letter == " ":        
        print(word)
        word = ""
    elif letter == ".":        
        print(word)
        word = ""
    else:
        word += letter
'''


sentance = """Sunshine warms the garden as a cheerful puppy chases a bright yellow butterfly across the grass."""

lyst = []

word = ""
for letter in sentance:
    if letter == " " or letter == ".":        
        lyst.append(word)
        word = ""
    else:
        word += letter

print(lyst)

print(sentance.split())



