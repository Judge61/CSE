world_map = {
    'room_1': {
        'NAME': "START",
        'DESCRIPTION': "There is a strange blue house north to you."
                       " Enter the blue house to began the game.",
        'PATHS': {
            'NORTH': "room_2"
        }
    },

    'room_2': {
        'NAME': "Blue_house",
        'DESCRIPTION': "The entrance leads right to the living room."
                       " There are cream colored sofas and a t.v. in front."
                       " There is a red carpet and a black coffee table with some compartments."
                       " To the east, there is a kitchen.",
        'PATHS': {
            'EAST': "room_3",
            'WEST': "room_1"
        }
    },

    'room_3': {
        'NAME': "Kitchen",
        'DESCRIPTION': "There are no windows but there is a pantry in front to the north."
                       " You may find some valuable things in the pantry.",
        'PATHS': {
            'WEST':  "room_2",
            'NORTH': "room_4"
        }
    },

    'room_4': {
        'NAME': "Pantry",
        'DESCRIPTION': "Upon opening the door, you found a bottle."
                       " The bottle reads, 'Strength potion'."
                       " This is perfect if your health is at risk."
                       " To the south and to the east, there are two rooms with the names: Loot_room2 or Loot_room1."
                       " Which room will you go to?",
        'PATHS': {

            'WEST': 'room_2',
            'SOUTH': "room_5",
            'EAST': "room_6"

        }
    },

    'room_5': {
        'NAME': "Loot_room2",
        'DESCRIPTION': "You chose the wrong room!"
                       " This is an empty room.",
        'PATHS': {
            'NORTH': "room_3"

        }
    },

    'room_6': {
        'NAME': "Loot_room1",
        'DESCRIPTION': "You chose the right room!"
                       " In this room there are drawers."
                       " In the drawers there is gold."
                       " To the south there is the owner’s room.",
        'PATHS': {
            'SOUTH': "room_7",
            'WEST': "room_3"

        }
    },

    'room_7': {
        'NAME': "Owner’s_room",
        'DESCRIPTION': "The room is very dark but there is a lantern in the corner on the nightstand"
                       " There is a door south."
                       " The door either leads to the dungeon or an empty room."
                       " The dungeon has some valuable stuff."
                       " But there is a door to the East that leads to the garden.",

        'PATHS': {
            'NORTH': "room_6",
            'SOUTH': "room_12",
            'EAST': "room_8"

        }
    },

    'room_8': {
        'NAME': "Garden",
        'DESCRIPTION':
            "There are rows and rows of flowers"
            " There is one special purple flower named: Supernova to your left."
            " There are two buildings in front of you"
            " To the east, there is a science lab and to the south there is a mini house where the owner is waiting.",

        'PATHS': {
            'WEST': "room_7",
            'EAST': "room_9",
            'SOUTH': "room_10"

        }
    },

    'room_9': {
        'NAME': "Science_lab",
        'DESCRIPTION':
            "There are a lot of potions."
            " Looks like the owner or your master was a scientist!",

        'PATHS': {
            'WEST': "room_8"

        }
    },

    'room_10': {
        'NAME': "Owner's_mini_house_entry",
        'DESCRIPTION': "You are led straight to the living room."
                       "All the other two rooms: Kitchen/Bathroom can not "
                       "be used without permission of master or owner."
                       "To the east, there is a door to your master’s bedroom.",

        'PATHS': {
            'EAST': "room_11",
            'NORTH': "room_8"

        }
    },

    'room_11': {
        'NAME': "Bedroom",
        'DESCRIPTION': "You have made it!",
                       "Let's see if you have all the things the master needs."
        'PATHS': {
            'WEST': "room_10",
        }
    },

    'room_12': {
        'NAME': "Dungeon",
        'DESCRIPTION': "There is a sword and a lightsaber.",
                       "To the south: Lich room."

        'PATHS': {
            'SOUTH': "room_13",
            'NORTH': "room_7",
        }
    },
    'room_13': {
        'NAME': "Lich_room",
        'DESCRIPTION': "Fight the Lich!!!!",
                       "Next room: South: Troll room"
        'PATHS': {
            'SOUTH': "room_14",
            'NORTH': "room_12"
        }
    },
    'room_14': {
        'NAME': "Troll_room",
        'DESCRIPTION': "Fight the troll.",
                       "South: where the emerald is."
        'PATHS': {
            'SOUTH': "room_15",
            'NORTH': "room_13"
        }
    },
    'room_15': {
        'NAME': "The_Emerald",
        'DESCRIPTION': "The emerald is east of you!"
                       "Take it and go to the garden to see where to go next!",
        'PATHS': {
            'NORTH': "room_14"
        }
    }
}

playing = True
current_node = world_map['room_1']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN', 'north', 'south', 'east', 'west', 'up', 'down', ]
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
