#write a function that takes a string as an arguments and returns a list
#of all the individual words in the string


word1 = "apples and bananas"
word2 = " lsdfj kldfjalk asdlkfj adslkfj"


def word_parser(sentence):
    words = []
    word = ""
    for letter in sentence:
        if letter == " ":
            words.append(word)
            word = ""
        else:
            word += letter
    words.append(word)
    return words

print(word_parser(word1))

#write a function that takes a list of words and returns a new list of words
#which have more than one vowel. 


def multi_vowel_words(lyst):
    new_lyst = []
    for word in lyst:
        vowel_count = 0
        for letter in word:
            if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
                vowel_count += 1
        if vowel_count > 1:
            new_lyst.append(word)
    return new_lyst

word_lyst = word_parser(word1)
x = multi_vowel_words(word_lyst)
print(x)


print(multi_vowel_words(word_parser(word1)))



