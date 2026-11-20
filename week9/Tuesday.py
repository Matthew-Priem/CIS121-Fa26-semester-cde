#store a list of words consisting of all words 
# with 2 or more vowels.
def string_to_list_with_vowels(sentence):
    words = []
    #collect a word
    built_word = ''
    vowel_count = 0
    for letter in sentence: #for index in range(len(sentence))
        if letter == ' ': # if sentence[index] == ' ' or index == (len(sentence) - 1)
            if vowel_count >= 2:
                words.append(built_word)
            built_word = ''
            vowel_count = 0
        else:
            built_word += letter
            if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
                vowel_count += 1
    
    if vowel_count >= 2:
        words.append(built_word)
    
    return words 


name = 'matt'
print(nam)



my_word = 'peter piper picked a peck of pickled peppers'
print(string_to_list_with_vowels(my_word))