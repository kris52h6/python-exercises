class Machine:
    def __init__(self):
        self.powered = False

    def power_up(self):
        self.powered = True if self.powered == False else self.powered == False


class Printer(Machine):
    def __init__(self):
        Machine.__init__(self)
        pass


class Papertray:
    def __init__(self):
        self.amount_of_paper = 0


p = Printer()
print(p.powered)
p.power_up()
print(p.powered)
p.power_up()
print(p.powered)
p.power_up()
print(p.powered)
# p.powered = True
# print(p.powered)
