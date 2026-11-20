#store a list of words consisting of all words 
# with 2 or more vowels.
def string_to_list_with_vowels(word):
    words = []
    #collect a word
    built_word = ''
    vowel_count = 0
    for letter in word: #for index in range(len(word))
        if letter == ' ': #if word[index] == " " or index == len(word) - 1
            #if >= 2 vowels add in word
            if vowel_count >= 2:
                words.append(built_word)
            #either way reset the word.
            built_word = ''
            vowel_count = 0
        else:
            built_word += letter
            #ask it letter is a vowel
            if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
                vowel_count += 1

    if vowel_count >= 2:
        words.append(built_word)
    
    return words 


my_word = 'peter piper picked a peck of pickled peppers'
print(string_to_list_with_vowels(my_word))