world_map = {
    'R19A': {
        'NAME': "Mr. Wiebe's room",
        'DESCRIPTION': "This is the classroom you are in right now. "
                       "Now, there are two doors on the north wall.",
        'PATHS': {
            'NORTH': "PARKING_LOT"

        }

    },
    'The Lich': {
        'NAME': "The North Parking Lot",
        'DESCRIPTION': "You have to fight the Lich for the sword. in this room. Get you A game on!",
        'PATHS': {
            'SOUTH': 'R19A'
        }
    }
}

# controller
playing = True
current_node = world_map['R19A']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']
while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in {'q', 'quit', 'exit'}:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way")
    else:
        print("Command not found")
