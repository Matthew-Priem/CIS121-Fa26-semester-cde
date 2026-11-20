class Point:
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
    def get_x(self):
        return self.x_coordinate
    def get_y(self):
        return self.y_coordinate

    def __str__(self):
        msg = ""
        msg += f"({self.get_x()},{self.get_y()})"
        return msg
    
    def __add__(self, other_point):
        new_x = self.get_x() + other_point.get_x()
        new_y = self.get_y() + other_point.get_y()
        return Point(new_x, new_y)
        #return f"({new_x},{new_y})"
    def __eq__(self, other_point):
        if self.get_x() == other_point.get_x() and self.get_y() == other_point.get_y():
            return True
        else:
            return False
    def distance(self, other_point):
        #number = #plug in distance formula. If needed look it up on google.
        #return number
        pass

p1 = Point(3,4)
p2 = Point(2,7)
p6 = Point(3,4)

print(p1 == p2)
print(p1 == p6)


#print(p1)
#print(p1.__str__())

p3 = p1 + p2  #(5,11)
#p3 = p1.__add__(p2)

#print(p3)


p4 = Point(1,-4)

p5 = p4 + p3
#print(p5)




class Chair:
    def __init__(self, a_color = "gray", a_height = 10):
        self.color = a_color
        self.height = a_height
        self.occupied = False

    def put_person_in_chair(self):
        self.occupied = True

    def remove_person_from_chair(self):
        self.occupied = False

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
        for chair in self.chairs:
            new_table.add_chair(chair)
        for chair in other_table.get_all_chairs():
            new_table.add_chair(chair)
        return new_table


table1 = Table()
table2 = Table()


new_table = table1 + table2

new_table.show_chairs()


