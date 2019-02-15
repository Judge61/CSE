class Sword(object):
    def __init__(self):
        self.clean = 0
        self.kill = 0
        self.glow = True
        self.activate_laser = True
        self.scream = True

    def clean(self):
        self.clean += 0
        if self.clean > 4:
            self.clean = 4

    def kill(self):
        self.kill += 0
        if self.kill > 1:
            self.kill = 1

    def glow(self):
        self.glow += 2
        if self.glow > 6:
            self.glow = 6


first_sword = Sword()
second_sword = Sword()




