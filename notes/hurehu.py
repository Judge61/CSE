class Room(object):
    def __init__(self, name, description, north=None, east=None, south=None, west=None):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.description = description


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []

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


Room_1 = Room("Start", "There is a strange blue house north to you."
                       " Enter the blue house to began the game.", "Room_2", None, None, None)

Room_2 = Room("Blue House", "The entrance leads right to the living room."
                            " There are cream colored sofas and a t.v. in front."
                            " There is a red carpet and a black coffee table with some compartments."
                            " To the east, there is a kitchen.", None, 'Room_3', "Room_1", None)

Room_3 = Room("Kitchen", "There are no windows but there is a pantry to your north."
                         " You may find some valuable things in the pantry.", 'Room_4', None, None, 'Room_2')

Room_4 = Room("Pantry", "Upon opening the door, you found a bottle."
                        " The bottle reads, 'Strength potion'."
                        " This is perfect if your health is at risk."
                        " To the south and to the east, there are two rooms with the names: Loot_room2 or Loot_room1."
                        " Which room will you go to?", None, 'Room_6', 'Room_5', 'Room_3')

Room_5 = Room("Loot_room2", "You chose the wrong room!"
                            " This is an empty room.", 'Room_4', None, None, None)

Room_6 = Room("Loot_room1", "You chose the right room!"
                            " In this room there are drawers."
                            " In the drawers there is gold."
                            " To the south there is the owner’s room.", None, None, 'Room_7', 'Room_4')

Room_7 = ("Owner's_room","The room is very dark but there is a lantern in the corner on the nightstand"
                         " There is a door south."
                         " The door either leads to the dungeon or an empty room."
                         " The dungeon has some valuable stuff."
                         " But there is a door to the East that leads to the garden.", "Room_6", "Room_8", "Room_12", None

Room_8 = ("Garden", "There are rows and rows of flowers."
                    " There is one special purple flower named: Supernova to your left."
                    " There are two buildings in front of you",
                    " To the east, there is a science lab and to the south there is a mini house where the owner is waiting.", None, "Room_9", "Room_10", "Room_7")

Room_9 = ("Science_lab",  "There are a lot of potions."
                          " Looks like the owner or your master was a scientist!", None, None, None, "Room_8")

Room_10 = ("Owner's_mini_house_entry", "You are led straight to the living room."
                                      "All the other two rooms: Kitchen/Bathroom can not "
                                      "be used without permission of master or owner."
                                      "To the east, there is a door to your master’s bedroom.", "Room_8", "Room_11", None, None

player = Player(Room_1)

playing = True
directions = ['north', 'east', 'south', 'west']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")

    if command.lower() in {'q', 'quit', 'exit'}:
        playing = False
    elif command.lower() in directions:
        try:
            room_name = player.find_next_room(command)
            player.move(room_name)
        except KeyError:
            print("I can't go that way")
    else:
        print("Command not found")

