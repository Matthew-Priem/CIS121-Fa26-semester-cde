class Point:
    def __init__(self,x,y):
        self.x_coordinate = x
        self.y_coordinate = y

    def get_x(self):
        return self.x_coordinate
    def get_y(self):
        return self.y_coordinate

    def __str__(self):
        msg = ""
        msg += f"({self.get_x()},{self.get_y()})"      #(x,y)
        return msg

    def __add__(self, other_point):
        x_new = self.get_x() + other_point.get_x()
        y_new = self.get_y() + other_point.get_y()
        return Point(x_new, y_new)
        #return f"({x_new},{y_new})"

    def __eq__(self, other_point):
        if self.get_x() == other_point.get_x() and self.get_y() == other_point.get_y():
            return True
        else:
            return False


p1 = Point(3,4)
p2 = Point(2,7)
p6 = Point(3,4)

p3 = p1 + p2
print(p3)       # (5,11)

p4 = Point(1,1)

p5 = p3 + p4
p5 = p3.__add__(p4)

p5 = p4 + p3
p5 = p4.__add__(p3)

#is p1 equal to p2
print(p1 == p2) #False

#is p1 equal to p6
print(p1 == p6) #True






class Chair:
    def __init__(self, a_color, a_height):
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



class Table:
    def __init__(self):
        self.chairs = []
        self.number_of_chairs = 0

    def add_chair(self, new_chair):
        self.chairs.append(new_chair)
        self.number_of_chairs += 1

    def show_chairs(self):
        for chair in self.chairs:
            print(chair)

    def get_all_chairs(self):
        return self.chairs

    def find_chair(self, look_up_color):
        for chair in self.chairs:
            if chair.get_color() == look_up_color:
                return chair

    def change_chair_color(self, old_color, new_color):
        chair = self.find_chair(old_color)
        chair.set_color(new_color)    

    #alt solution
    def change_chair_color_alt(self, old_color, new_color):
        for chair in self.chairs:
            if chair.get_color() == old_color:
                chair.set_color(new_color)

    def __add__(self, other_table):
        new_table = Table()
        for chair in self.get_all_chairs():
                    new_table.add_chair(chair)
        for chair in other_table.get_all_chairs():
            new_table.add_chair(chair)
        return new_table                            

table1 = Table()

table1.add_chair( Chair("Blue", 15) )
table1.add_chair( Chair("Green", 15) )


table2 = Table()

table2.add_chair( Chair("Red", 15) )
table2.add_chair( Chair("Yellow", 15) )

table3 = table1 + table2


table3.show_chairs() #this should show Blue, Green, Red, Yellow chair















#print(p5)
'''


print(p1)
print(p1.__str__())


a = 3
b = 4

c = a + b
c = a.__add__(b)

lyst = []

lyst.append('a')
'''