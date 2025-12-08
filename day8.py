import math

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

    def set_closest_neighbor(self, lights):
        for light in lights:
            if light.coords() == self.coords():
                continue

            if light.closest_neighbor != None and light.closest_neighbor.coords() == self.coords():
                continue

            val = math.dist(light.coords(), self.coords())
            if self.closest_neighbor == None:
                self.closest_neighbor = light
                self.closest_neighbor_val = val
                continue

            if val < self.closest_neighbor_val:
                self.closest_neighbor = light
                self.closest_neighbor_val = val

    def connect_to_closest_neighbor(self, circuits):
        if self.circuit == None:
            circuit = Circuit()
            self.add_to_circuit(circuit)
            circuits.append(circuit)
            self.closest_neighbor.add_to_circuit(circuit)
        else:
            self.closest_neighbor.add_to_circuit(self.circuit)

    def add_to_circuit(self, circuit):
        self.circuit = circuit
        circuit.add_light(self)

lights = []
for line in lines:
    x, y, z = line.split(",")
    light = Light(x, y, z)
    lights.append(light)

for light in lights:
    light.set_closest_neighbor(lights)

lights.sort(key=lambda light: light.closest_neighbor_val)
circuits = []
for light in lights:
    light.connect_to_closest_neighbor(circuits)


