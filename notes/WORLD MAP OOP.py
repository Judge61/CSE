class Room(object):
    def __init__(self, name, north=None, south=None, east=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.characters[]


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
        return getattr(self.current_location, direction)        #option 1


playing = True
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']
current_node = world_map

player = Player(world_map)
while playing:
    print(player.current_location.name)
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in {'q', 'quit', 'exit'}:
        playing = False
    elif command.lower() in directions:
       try:
        room_name = current_node['PATHS'][command.upper()]
        current_node = world_map[room_name]
       except KeyError:
        print("I can't go that way")
    else:
        print("Command not found")

