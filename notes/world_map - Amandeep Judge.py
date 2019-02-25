world_map = {
    'Room 1': {
        'NAME': "START",
        'DESCRIPTION': "There is a strange blue house north to you."
                       "Enter the blue house to began the game.",
        'PATHS': {
          'NORTH': "Blue_House"
        }
    },

    'Room 2': {
        'NAME': "Living_room",
        'DESCRIPTION': "The entrance leads right to the living room."
                       "There are cream colored sofas and a t.v. in front."
                       "There is a red carpet and a black coffee table with some compartments."
                       "To the east, there is a kitchen.",
        'PATHS': {
            'East': "Kitchen",
            'West': "START"
        }
    },
    
    'Room 3': {
        'NAME': "Kitchen",
        'DESCRIPTION': "There are no windows but there is a pantry in front of you."
                       "You may find some valuable things in the pantry.",
        'PATHS': {
            'West': "Living_room",
            'UP': "Pantry"
        }
    },

    'Room 4': {
       'NAME': "Pantry",
       'DESCRIPTION': "Upon opening the door, you found a bottle."
                      "The bottle reads, 'Strength potion'."
                      "This is perfect if your health is at risk." 
                      "To the south and to the east, there are two rooms with the names: Loot_room1 or Loot_room2."
                      "Which room will you go to?",
       'PATHS': {

            'West': 'Living_Room',
            'South': "Loot_room2",
            'East': "Loot_room1"

        }
    },


    'Room 5': {
       'NAME': "Loot_room2",
       'DESCRIPTION': "You chose the wrong room!"
                      "This is an empty room",
       'PATHS': {
           'East': "Kitchen"


        }
    },

    'Room 6': {
        'NAME': "Loot_room1",
        'DESCRIPTION': "You chose the right room!"
                       "In this room there are drawers." 
                       "In the drawers there is gold."
                       "To the "
        'PATHS': {
             'North' "I",
         }
    },


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