def add_lysts(lyst1, lyst2):
    #the logic of the fctn.
    #write code that adds the corresponding elements
    #of each list together and add them to a new
    #list. Then return the new list.
    index = 0
    new_list = []
    #we arbitrarly pick lyst1 becuase the problem
    #said len(lyst1) = len(lyst2)
    while index < len(lyst1):
        total = lyst1[index] + lyst2[index]
        new_list.append(total)
        index += 1
    return new_list

#x = [1,8,5,0,-7]
#y = [0,-7,4,2,-6]

#z = add_lysts(x,y)
#print(z)










'''
size = int(input("size: "))
inside_count = 0
outside_count = 0

for row in range(size):

    for col in range(size):
        if inside_count == outside_count:
            print("X", end="")
        else:
            print("O", end = "")
        inside_count += 1
    outside_count += 1
    print()
'''




size = int(input("size: "))
inside_count = 0
outside_count = 0

for row in range(size):
    #inside_count = 0
    for col in range(size):
        if inside_count == outside_count:
            print("X", end="")
        else:
            print("O", end = "")
        inside_count += 1
    outside_count += 1 + size
    print()


ary = [1,0,0,0,1,0,0,3,4]
m = [ [1,0,0],[0,1,0],[0,3,4]]

m = [ [1,0,0],
      [0,1,0],
      [0,3,4]
    ]