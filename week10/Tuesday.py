def fctn_name(parameters):
    #logic of fctn
    pass
    #this is in the fctn
#this is not in the fctn



class NameOfClass:
    #logic of class
    def method1():
        #logic of method
        pass
    def method2():
        #logic of method
        pass
    #this is in the class
#this is not in the class

class Chair:
    def __init__(self,the_color,the_height):
        self.color = the_color
        self.height = the_height
        self.occupied = False

    def get_color(self): #<- chair2 is self
        return self.color
    def get_height(self):
        return self.height

    def set_color(self, new_color):
        self.color = new_color



    def method2(self):
        pass

chair1 = Chair("blue", 15)
chair2 = Chair("green", 23)



#print(chair1.get_color())

#chair1.set_color("yellow")

#print(chair1.get_color())

print(chair1)


#print(chair2.get_color())

#print(chair1.get_height())
#print(chair2.get_height())


x = 3
y = 4

lyst1 = ['a','b','c']
word = "xyz"
lyst1.append("w")
abs(-3)






chair1 # I want a function to tell me
#The color of the chiar