# def fight(opponent):
#     player.attack(opponent)
#     opponent.attack(player)


class Room(object):
    def __init__(self, name, description, north=None, east=None, south=None, west=None, characters=None, _item=None):
        if characters is None:
            characters = []
        self.characters = characters
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.description = description
        self.item = _item


class Item(object):
    def __init__(self, name):
        self.name = name


class Beaker(Item):
    def __init__(self):
        super(Beaker, self).__init__("Beaker")


class Venomboomslang(Item):
    def __init__(self):
        super(Venomboomslang, self).__init__("Venom: Boomslang")


class Pixiedust(Item):
    def __init__(self):
        super(Pixiedust, self).__init__("Pixie Dust")


class Phoenixfeather(Item):
    def __init__(self):
        super(Phoenixfeather, self).__init__("Phoenix feather")


class Dragonblood(Item):
    def __init__(self):
        super(Dragonblood, self).__init__("Dragon Blood")


class Fourleafclover(Item):
    def __init__(self):
        super(Fourleafclover, self).__init__("Four Leaf Clover")


class Diamonds(Item):
    def __init__(self):
        super(Diamonds, self).__init__("Diamonds")


class Droppers(Item):
    def __init__(self):
        super(Droppers, self).__init__("Droppers")


class Blackmagic(Item):
    def __init__(self):
        super(Blackmagic, self).__init__("Book: Black Magic")


class Cauldron(Item):
    def __init__(self):
        super(Cauldron, self).__init__("Cauldron")


class Gloves(Item):
    def __init__(self):
        super(Gloves, self).__init__("gloves")


class Serpentblood(Item):
    def __init__(self):
        super(Serpentblood, self).__init__("Serpent's Blood")


class Flower(Item):
    def __init__(self):
        super(Flower, self).__init__("Flower: supernova")


class Pan(Item):
    def __init__(self):
        super(Pan, self).__init__("Pan")


class Pocketwatch(Item):
    def __init__(self):
        super(Pocketwatch, self).__init__("Pocket Watch")


class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage
        print("Nice attack")

# class character(object):
#     def __init__(self, name, weapon):
#         self.name = name
#         self.health = 150
#         self.weapon = weapon
#
#     def take_damage(self, damage):
#         self.health -= damage
#         if self.health < 0:
#             self.health = 0
#         print("%s has %d health left" % (self.name, self.health))
#
#     def attack(self, target):
#         print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
#         target.take_damage(self.weapon.damage)
#
#
# lich1 = character("Bri the Lich")
# troll1 = character("Troll")


book = Blackmagic()


# You will not be able to use any of the items even if you try. Only the scientist can!


class Player(object):
    def __init__(self, starting_location, weapon):
        self.current_location = starting_location
        self.inventory = []
        self.name = "Player"
        self.weapon = weapon
        self.health = 100

    def move(self, new_location):
        """This moves the player to a new room

        :param new_location: The room object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """This method searches current room to see if a room exists in that direction

        :param direction: The direction that you want to move to
        :return: The room object if it does exist, or none if it does not exist
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


Room_1 = Room("Start", "There is a strange house north to you."
                       " Enter the house to began the game.", 'Room_2', None, None, None, None)

Room_2 = Room("Blue House", "The entrance leads right to the living room."
                            " There is a red carpet and a black coffee table with some compartments."
                            " To the east, there is a kitchen.", None, 'Room_3', 'Room_1', None, None,
              [Blackmagic()])

Room_3 = Room("Kitchen", "There are no windows but there is a pantry to your north."
                         " You may find some valuable things in the pantry.", 'Room_4', None, None, 'Room_2')

Room_4 = Room("Pantry", " Upon opening the door, There are only two items in here."
                        " There is a phoenix feather."
                        " There is a bottle that says: Venom: Boomslang"
                        " To the south and to the east, there are two rooms with the names: Loot_room2 or Loot_room1."
                        " Which room will you go to?", None, 'Room_6', 'Room_5', 'Room_3', None, [Phoenixfeather(),
                                                                                                  Venomboomslang()])

Room_5 = Room("Loot_room2", "You chose the wrong room!"
                            " This is an empty room.", 'Room_4', None, None, None)

Room_6 = Room("Loot_room1", "You chose the right room!"
                            " In this room there are many drawers."
                            " In the drawers there is a pocket watch."
                            " There is a huge diamond."
                            " On the back it reads: Brianna Lich "
                            " To the south there is the owner’s room.", None, None, 'Room_7', 'Room_4', None,
              [Diamonds(), Pocketwatch()])

Room_7 = Room("Owner's_room", "The room is very dark but there is a lantern in the corner on the nightstand"
                              " There is a door south."
                              " The door either leads to the dungeon or an empty room."
                              " The dungeon has some valuable stuff."
                              " But there is a door to the East that leads to the garden.", 'Room_6', 'Room_8',
              'Room_12', None, None, )

Room_8 = Room("Garden", "There are rows and rows of flowers."
                        " There is one special/violet flower named: Supernova."
                        " There is a four leaf clover too."
                        " There are two buildings in front of you"
                        " To the east, there is a science lab and to the south there is a mini"
                        "house where the owner is waiting.", None, 'Room_9', 'Room_10', 'Room_7', None, [Flower(),
                                                                                                         Fourleafclover(

                                                                                                         )])

Room_9 = Room("Science_lab", "There is a beaker, a pan, gloves, a cauldren, and droppers."
                             " Looks like the owner or your master was a scientist!", None, None, None, 'Room_8',
              [Droppers(), Cauldron(), Pan(), Gloves()])

Room_10 = Room("Owner's_mini_house_entry", "You are led straight to the living room."
                                           " All the other two rooms: Kitchen/Bathroom can not"
                                           " be used without permission of master or owner."
                                           " To the east, there is a door to your master’s bedroom.", 'Room_8',
               'Room_11', None, None)

Room_11 = Room("Bedroom", "You have made it!"
                          " Let's see if you have all the things the master needs.", None, None, None, 'Room_10')

Room_12 = Room("Dungeon", "There is a sword."
                          " To the south: Lich room.", 'Room_7', None, 'Room_13', None)

Room_13 = Room("Lich_room", "Fight the Lich!!!!"
                            " Next room: South: Troll room", 'Room_12', None, 'Room_14', None)

Room_14 = Room("Troll_room", "Fight the troll."
                             " South: where the dragon's blood is.", 'Room_13', None, 'Room_15', None)

Room_15 = Room("Loot_room3", "The dragon's blood and the pixie dust is east of you!"
                             " Take it and go to the garden to see where to go next!", 'Room_14', None, None, None,
               [Dragonblood(), Serpentblood(), Pixiedust()])

player = Player(Room_1, Weapon)

playing = True
directions = ['north', 'east', 'south', 'west']
short_directions = ['n', 'e', 's', 'w']
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    if player.current_location.item is not None:
        for item in player.current_location.item:
            print("There is an item: %s" % item.name.lower())
    command = input(">_")

    if command.lower() in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]

    if player.current_location.item is not None and command.lower() in ['pick up', 'grab']:
        for item in player.current_location.item:
            player.inventory.append(item)
            print("Your player picked up the %s" % item.name.lower())
        player.current_location.item = None
    elif command.lower() in {'q', 'quit', 'exit'}:
        playing = False
    elif command.lower() in directions:
        try:
            room_name = player.find_next_room(command)
            player.move(room_name)
        except KeyError:
            print("I can't go that way")
    else:
        print("Command not found")
    if player.current_location == Room_15:
        print("You collected the following items:")
        for item in player.inventory:
            print(item.name)
        print()

        if len(player.inventory) >= 15:
            print("CONGRATS!!!!!!!!")
            quit(0)
