class Chair:
    def __init__(self, a_color, a_height = 10):
        self.color = a_color
        self.height = a_height

    def get_color(self):
        return self.color
    def get_height(self):
        return self.height

    def set_color(self, new_color):
        self.color = new_color
    def set_height(self, new_height):
        self.height = new_height

    def do_stuff_with_color(self, other):
        self.color = other
        return self.color

    def __str__(self):
        msg = ""
        #whatever you want for the message
        msg += f"This is a {self.get_color()} chair of height {self.get_height()}."
        return msg
    


chair1 = Chair("blue", 15)
#chair1 = Chair.__init__("blue", 15)
chair2 = Chair("green", 28)
chair3 = Chair("purple")
print(chair3)


#print(chair1)
#print(chair1.__str__())

#x = 3
#print(x)
#print(x.__str__())

#print(chair1.get_color())
#print(chair2.get_color())
chair1.set_color("red")
#print(chair1.get_color())
#print(chair1.get_height())
chair1.set_height(30)
#print(chair1.get_height())

#print(chair1)


