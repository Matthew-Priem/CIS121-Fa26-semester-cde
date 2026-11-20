
#write a function that takes a lyst of an argument
#and returns the larget number in the list.

#your code here

def find_largest(lyst):
    largest  = lyst[0]
    #looks at each number
    for current_number in lyst:
        #compare current to largest
        if current_number > largest:
            #update the largest to the current
            largest = current_number
    #give back largest 
    return largest

#write a funtion that takes a lyst of words
#and returns the longest length word. 

def find_largest_word(lyst):
    largest_word = lyst[0]
    for current_word in lyst:
        if len(current_word) > len(largest_word):
            largest_word = current_word
    return largest_word

word_lyst = ["apples", "bananas", "watermelon", "kiwi"]


number_lyst = [2,5,1,7,8,10,2,4,3]

largest = find_largest(number_lyst)
#print(largest)


#cart = ["apples", "bananas", "watermelon", "kiwi"]


#To define a dictionary in python we use {}
# to put intial values in the dictionary we 
#use : to seperate key and value
#and a , to seperate key-value pairs.

food_dict = {"apples" : 4, "bananas" : 3}
#print(food_dict)

#dictionary_name[key] produces the value
food_value = food_dict["bananas"]
#print(food_value)

#to add to a dictionary, we use
#dictionary_name[key] = value
food_dict["watermelon"] = 1

#add 2 kiwi
food_dict["kiwi"] = 2

#food_dict["bananas"] = #look up the old number + 4
food_dict["bananas"] = food_dict["bananas"] + 4

#print(food_dict)


#for key in food_dict:
#    print(key)

#for current_key in food_dict:
#    value = food_dict[current_key]
#    print(value)

for current_key in food_dict:
    print(current_key, food_dict[current_key])


def find_most_abundent_food(gorcery_dict):
    largest_qty = -1
    most_abundent_food = ""
    #your code here

    return most_abundent_food

x = find_most_abundent_food(food_dict)
print(x)
