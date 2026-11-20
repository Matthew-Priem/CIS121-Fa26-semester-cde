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
    def __init__(self, name:str):
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
        self.planet_list = []

    def add_planet(self, new_planet):
        """This methods will add the new_planet to the planet_list"""
        self.planet_list.append(new_planet)

    def show_planets(self):
        for planet in self.planet_list:
            print(planet)
        #print(self.planet_list)
    
    def find_planet(self,name_of_planet_to_find):
        for planet in self.planet_list:
            if planet.get_name() == name_of_planet_to_find:
                return planet

    def change_planet_name(self, old_name, new_name):
        planet = self.find_planet(old_name)
        planet.set_name(new_name)

    def change_planet_name_alt(self, old_name, new_name):
        for planet in self.planet_list:
            if planet.get_name() == old_name:
                planet.set_name(new_name)
                




#planet1 = Planet("x23", 12, 345, 8374)
#planet2 = Planet("z46", 76, 324, 3123)
'''
sun = Star("Sun")
solar_system = PlanetarySystem(sun)

mercury = Planet("Mercury",1,1,1)
solar_system.add_planet(mercury)

venus = Planet("Venus",1,1,1)
solar_system.add_planet(venus)

earth = Planet("Earth",1,1,1)
solar_system.add_planet(earth)

earth.set_name("Terra")

solar_system.show_planets()
'''

solar_system = PlanetarySystem( Star("Sun") )

solar_system.add_planet( Planet("Mercury",1,1,1) )
solar_system.add_planet( Planet("Venus",1,1,1) )
solar_system.add_planet( Planet("Earth",1,1,1) )

solar_system.show_planets()


solar_system.change_planet_name("Earth", "Terra")

print()
solar_system.show_planets()







'''
table1 = Table()
table2 = Table()
...
table10 = Table()


chair1 = Chair()
table1.add_to_table(chair1)

chair2 = Chair()
table1.add_to_table(chair2)

chair10 = Chair()
table2.add_to_table(chair10)

chair11 = Chair()
table3.add_to_table(chair11)


chair50 = Chair()
table10.add_to_table(chair50)
'''