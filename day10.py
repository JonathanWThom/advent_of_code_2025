import re

raw_machines = open("./day10_input.txt").read().splitlines()

# The manual describes one machine per line. Each line contains a single indicator light diagram in [square brackets], one or more button wiring schematics in (parentheses), and joltage requirements in {curly braces}.

# \[(.*?)\]
# \(([^)]*)\)
class Button:
    def __init__(self, instructions, initial_diagram, generation):
        self.instructions = self._build_instructions(initial_diagram, instructions)

    def _build_instructions(self, initial_diagram, instructions):
        tmp = initial_diagram # initial diagram got too long??
        for i in instructions:
            tmp[i] = 1
        return tmp


class Diagram:
    def __init__(self, raw):
        self.raw = raw

    def to_binary(self):
        tmp = []
        for r in raw:
            if r == "#":
                tmp.append(1)
            else:
                tmp.append(0)

        return tmp

class Machine:
    def __init__(self, raw_machine):
        d = Diagram(list(re.findall(r"\[([^\]]*)\]", raw_machine)[0]))
        self.goal_diagram = d.to_binary()
        self.initial_diagram = []
        for i in range(len(self.goal_diagram)):
            self.initial_diagram.append(0)
        self.buttons = self._build_buttons(raw_machine)

    def _build_buttons(self, raw_machine):
        buttons = []
        for raw_button in re.findall(r"\(([^)]*)\)", raw_machine):
            buttons.append(Button(raw_button.split(","), self.initial_diagram, 0))

        return buttons

    def find_fastest_iteration(self):
        if self.initial_diagram == self.goal_diagram:
            return 0

        target = [(self.goal_diagram[i] - self.initial_diagram[i]) % 2 for i in range(len(self.initial_diagram))]
        A = []
        for i in range(len(self.initial_diagram)):
            row = [buttons.instructions[j][i] for j in range(num_sets)]
            A.append(row)

        print(A)
        # I need guassain elimination? or
        # https://math.libretexts.org/Bookshelves/Combinatorics_and_Discrete_Mathematics/Applied_Discrete_Structures_(Doerr_and_Levasseur)/12%3A_More_Matrix_Algebra/12.06%3A_Linear_Equations_over_the_Integers_Mod_2
        # ?


        return 0 # should not hit


button_presses = 0
for raw in raw_machines:
    m = Machine(raw)
    button_presses += m.find_fastest_iteration()

# [#] (
print(button_presses)
