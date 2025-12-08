import math
import itertools

lines = open("./day8_input.txt").read().splitlines()
class Circuit:
    def __init__(self):
        self.lights = []

    def add_light(self, light):
        if light in self.lights: # might need to check coords?
            return

        self.lights.append(light)

class Light:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.closest_neighbor = None
        self.closest_neighbor_val = None
        self.circuit = None

    def coords(self):
        return [self.x, self.y, self.z]

    def get_relationships_with_distance(self, lights):
        relationships = []
        for light in lights:
            if light.coords() == self.coords():
                continue
            val = math.dist(self.coords(), light.coords())
            relationships.append([self, light, val])

        return relationships

lights = []
for line in lines:
    x, y, z = line.split(",")
    light = Light(x, y, z)
    lights.append(light)

relationships = []
for light in lights:
    relationships.append(light.get_relationships_with_distance(lights))
relationships = list(itertools.chain.from_iterable(relationships))

relationships.sort(key= lambda relationship: relationship[2]) # distance
