class Item(object):
    def __init__(self, name):
        self.name = name


class Beaker(Item):
    def __init__(self):
        super(Beaker, self).__init__("Beaker")


class Pixiedust(Item):
    def __init__(self):
        super(Pixiedust, self).__init__("Pixie Dust")


class Dragonblood (Item):
    def __init__(self):
        super(Dragonblood, self).__init__("Dragon Blood")


class Fourleafclover (Item):
    def __init__(self):
        super(Fourleafclover, self).__init__("Four Leaf Clover")


class Diamonds (Item):
    def __init__(self):
        super(Diamonds, self).__init__("Diamonds")


class Droppers (Item):
    def __init__(self):
        super(Droppers, self).__init__("Droppers")


class Bookexperiments (Item):
    def __init__(self):
        super(Bookexperiments, self).__init__("Book: Experiments")


class Serpentsblood (Item):
    def __init__(self):
        super(Serpentsblood, self).__init__("serpent's blood")


class Cauldren (Item):
    def __init__(self):
        super(Cauldren, self).__init__("couldren")


class Gloves (Item):
    def __init__(self):
        super(Gloves, self).__init__("gloves")


class Flower (Item):
    def __init__(self):
        super(Flower, self).__init__("Flower: supernova")


class Pan (Item):
    def __init__(self):
        super(Pan, self).__init__("Pan")


class Pocketwatch (Item):
    def __init__(self):
        super(Pocketwatch, self).__init__("Pocket Watch")


class Item(object):
    def __init__(self, name):
        self.name = name


class Lantern(Item):
    def __init__(self, name, lantern):
        super(Lantern, self).__init__(name)
        self.glow = lantern
        print("Your lantern is flowing and you can finally see!")


beaker = Beaker()

item_list = [Beaker]

# You will not be able to use any of the items even if you try. Only the scientist can!