class Room(object):
    def __init__(self, name, description, north=None, south=None, east=None, west=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description


class Player (object):
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
        return getattr(self.current_location, direction)        # Option 1


Room_1 = ("Start", "There is a strange blue house north to you." 
                   "Enter the blue house to began the game.", 'Room_2', None, None)
Room_2 = ("Blue House", "", None, None, 'Room_east')

playing = True
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']
current_node = Room_1

player = Player(Room_1)

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

