
#write a function that takes a lyst of an argument
#and returns the larget number in the list.


def find_largest(lyst):
    largest = lyst[0]
    #look at each number
    for number in lyst:
        #determine if it is the largest.
        if number > largest:
            #update largest to the number
            largest = number
    return largest

#write a funtion that takes a lyst of words
#and returns the longest length word. 
def find_largest_word(lyst):
    largest_word = lyst[0]
    for word in lyst:
        if len(word) > len(largest_word):
            largest_word = word
    return largest_word


number_lyst = [2,5,1,7,8,10,2,4,3]

largest = find_largest(number_lyst)
#print(largest)


#To define a dictionary in python we use {}
# to put intial values in the dictionary we 
#use : to seperate key and value
#and a , to seperate key-value pairs.

food_dict = {"apples" : 4, "bananas" : 3}
#print(food_dict)


#to insert a key-value pair into a dictionary, we use
#dictionary_name[key] = value

food_dict["melons"] = 7

#print(food_dict)

#dictionary_name[key] produces the value
food_value = food_dict["bananas"]
#print(food_value)



#for key in food_dict:
#    print(key)

#for key in food_dict:
#    print(food_dict[key])


food_dict = {"apples" : 4, "bananas" : 3}

food_dict["melons"] = 7

food_dict['kiwi'] = 2



#for key in food_dict:
#    print(key, food_dict[key])


#which fruit is there the most of in the basket?

most_common_food = ""
largest_qty = -1

for key in food_dict:
    if food_dict[key] > largest_qty:
        largest_qty = food_dict[key]
        most_common_food = key

print(f'the most common food is {most_common_food}')

