#write a function that takes a list 
#as an argument and returns a new
#list that contains all the names 
#who has more than 5 letters in their name


names_lyst = ['matt', 'ashley', 'dexter', 'gene', 'cameron']
other_names = ['Mike', "rushit", "mansi", "ashwin"]


def name_filter(old_list):
    new_list = []
    #write to find words > 5

    #start by looking at each name in the list
    for name in old_list:
        #check if the length of the name is > 5.
        if len(name) > 5:
            #add name to the new_list
            new_list.append(name)
    return new_list


#print(name_filter(names_lyst))
#print(name_filter(other_names))



lyst1 = ['a','b','c']
lyst2 = lyst1

lyst3 = []
for element in lyst1:
    lyst3.append(element)



lyst4 = []
index = 0
while index < len(lyst1):
    element = lyst1[index]
    lyst4.append(element)
    index += 1


print(lyst1)
print(lyst2)
print(lyst3)
print(lyst4)

lyst2[1] = 'd'


print("\n ---------- \n")

print(lyst1)
print(lyst2)
print(lyst3)
print(lyst4)
