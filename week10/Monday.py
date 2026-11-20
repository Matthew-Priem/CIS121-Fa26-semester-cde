class Planet:

	def __init__(self, name, radius, the_mass, the_dist):
		self.name = name
		self.radius = radius
		self.mass = the_mass
		self.dist = the_dist
		
	def get_name(self):
		return self.name
	def get_radius(self):
		return self.radius
	def get_mass(self):
		return self.mass
	


planet1 = Planet("x25", 45, 198, 1000)
planet2 = Planet("z37", 123, 454, 2320)

print(planet1.get_name())
print(planet2.get_name())

print(planet1.get_mass())
print(planet2.get_mass())





class Dog:
	def __init__(banana, dogs_name = "unknown"):
		banana.name = dogs_name


dog1 = Dog("spot")
dog2 = Dog()








