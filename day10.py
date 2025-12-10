import re

raw_machines = open("./day10_input.txt").read().splitlines()

# The manual describes one machine per line. Each line contains a single indicator light diagram in [square brackets], one or more button wiring schematics in (parentheses), and joltage requirements in {curly braces}.

# \[(.*?)\]
# \(([^)]*)\)
class Button:
    def __init__(self, instructions, initial_diagram, generation):
        self.instructions = instructions
        self.current_diagram = initial_diagram
        self.generation = generation

    def apply_button(self, other_button):
        for inst in other_button.instructions:
            if self.current_diagram[int(inst)] == ".":
                self.current_diagram[int(inst)] = "#"
            else:
                self.current_diagram[int(inst)] = "."

        self.generation += 1
        return self.current_diagram

class Machine:
    def __init__(self, raw_machine):
        self.goal_diagram = list(re.findall(r"\[([^\]]*)\]", raw_machine)[0])
        self.initial_diagram = []
        for i in range(len(self.goal_diagram)):
            self.initial_diagram.append(".")
        self.buttons = self._build_buttons(raw_machine)

    def _build_buttons(self, raw_machine):
        buttons = []
        for raw_button in re.findall(r"\(([^)]*)\)", raw_machine):
            buttons.append(Button(raw_button.split(","), self.initial_diagram, 0))

        return buttons

    def find_fastest_iteration(self):
        if self.initial_diagram == self.goal_diagram:
            return 0

        for button in self.buttons:
            diagram = button.apply_button(button)
            if diagram == self.goal_diagram:
                return button.generation

        return 0 # should not hit


button_presses = 0
for raw in raw_machines:
    m = Machine(raw)
    button_presses += m.find_fastest_iteration()

print(button_presses)
