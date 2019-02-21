class Sword(object):
    def __init__(self):
        self.clean = 0
        self.glow = 0
        self.activate_laser = 0
        self.scream = 0
        self.stab_wounds = 0

    def clean(self):
        self.clean += 0
        if self.clean > 4:
            self.clean = 4

    def stab(self):
        if self.stab_wounds < 3:
            self.stab_wounds += 1
            if self.stab_wounds == 3:
                print("You kill someone")
        else:
            print("They are already dead")

    def glow(self):
        self.glow += 2
        if self.glow > 6:
            self.glow = 6

    def activate_laser(self):
        self.activate_laser += 90
        if self.activate_laser > 100:
            self.activate_laser = 100

    def scream(self):
        self.scream = 0
        if self.scream +=


