word = 'apples and bananas'

#x[index] produces the letter in the index position
#print(word[3])

#x[start:stop] this is called slicing and will produces a substring based on those
#positions
#print(word[1:4])

#print(word[4])
#print(word[10])
#print(word[14])


#len will return the number of letters in a word. 
#ie the length of the word
#print( len(word) )

#word = "apple"




'''
for letter in word:
    print(letter)

print("----------")

for index in range(len(word)):
    print(index)

print("----------")

for index in range(len(word)):
    print(word[index])
'''



word = """adskfjhlasdfh ;asdfhaosdfhaosdfhnlaosdfh;asdlfhlaksdfh
            joa;siefj[pejanv;lasehopiuha;ljknvpaioruwvna;lsihg;a
            sodlfhl;sad]"""

word = "apple"

count = 0

for letter in word:
    if letter == 'a':
        print(letter)
        count += 1
    elif letter == 'e':
        print(letter)
        count += 1
    elif letter == 'i':
        count += 1
        print(letter)
    elif letter == 'o':
        count += 1
        print(letter)
    elif letter == 'u':
        print(letter)
        count += 1

print(count)



x = x + 1
x += 1
