world_map = {
    'R19A': {
        'Name': "Mr. Wiebe's room",
        'Description': "This is the classroom you are in right now. "
                       "Now, there are two doors on the north wall.",
        'Paths': {
            'North': "PARKING_LOT"

}

    },
    'PARKING_LOT': {
        'Name': "The North Parking Lot",
        'Description': "There are a couple of cars parked here",
        'Paths': {
            'South': 'R19A'
        }
    }
}


# controller
playing = True
current_node = world_map['R19A']
while playing:
    print(current_node{})
    command = input(">_")
    if command.lower() in {'q', 'quit', 'exit'}:
        playing = False