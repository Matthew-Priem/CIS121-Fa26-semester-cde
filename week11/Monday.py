import math


class Planet:
    def __init__(self, a_name:str, a_radius:int, a_mass, a_distance):
        self.name = a_name
        self.radius = a_radius
        self.mass = a_mass
        self.dist = a_distance

    #getters
    def get_name(self):
        return self.name
    def get_mass(self):
        return self.mass
    def get_radius(self):
        return self.radius
    def get_distance(self):
        return self.dist
    def get_volume(self):
        #V=4/3 pi r^3
        volume = 4/3 * math.pi * self.get_radius() ** 3
        #volume = 4/3 * math.pi * self.radius ** 3
        return volume

    #setters
    def set_name(self, new_name):
        self.name = new_name

    def __str__(self):
        msg = ""
        #make that message whatever you want.
        msg += f'greeting from the planet {self.get_name()}!!!'
        return msg

class Star:
    def __init__(self, name):
        self.name = name
    #getters
    def get_name(self):
        return self.name + " is a star."
    #setters
    def set_name(self, new_name):
        self.name = new_name

class PlanetarySystem:
    def __init__(self, a_star):
        self.star = a_star
        self.number_of_planets = 0
        self.planets = []
    #getters
    #setters

    def add_planet(self, new_planet):
        self.planets.append(new_planet)

    def show_plaents(self):
        for planet in self.planets:
            print(planet)

#planet1 = Planet("x23", 12, 345, 8374)
#planet2 = Planet("z46", 76, 324, 3123)


sun = Star("Sun")
solar_system = PlanetarySystem(sun)

mercury = Planet("Mercury",1,1,1)
solar_system.add_planet(mercury)

venus = Planet("Venus",1,1,1)
solar_system.add_planet(venus)

earth = Planet("Earth",1,1,1)
solar_system.add_planet(earth)

#solar_system.show_plaents()

earth.set_name("The Earth")

#lyst = ['a','b','c']
#for element in lyst:
#    print(element)


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




'''
table1 = Table()

chair1 = Chair("Blue", 15)
table1.add_chair(chair1)

chair1 = Chair("Green", 15)
table1.add_chair(chair1)


table1.show_chairs()
chair1.set_color("yellow")

print()
table1.show_chairs()
'''
#table1.change_chair_color("Blue", "Red")


table1 = Table()

table1.add_chair( Chair("Blue", 15) )
table1.add_chair( Chair("Green", 15) )

table1.show_chairs()

