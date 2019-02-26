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
        'DESCRIPTION': "There are no windows but there is a pantry in front of you o north."
                       "You may find some valuable things in the pantry.",
        'PATHS': {
            'West': "Living_room",
            'North': "Pantry"
        }
    },

    'Room 4': {
        'NAME': "Pantry",
        'DESCRIPTION': "Upon opening the door, you found a bottle."
                       "The bottle reads, 'Strength potion'."
                       "This is perfect if your health is at risk."
                       "To the south and to the east, there are two rooms with the names: Loot_room2 or Loot_room1."
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
                       "This is an empty room.",
          'PATHS': {
               'North': "Kitchen"

}
},

    'Room 6': {
         'NAME': "Loot_room1",
         'DESCRIPTION': "You chose the right room!"
                        "In this room there are drawers."
                        "In the drawers there is gold."
                        "To the south there is the owner’s room.",
           'PATHS': {
               'South': "Owner’s_room",
               'West': "Kitchen"


            }
    },

    'Room 7': {
          'NAME': "Owner’s_room",
          'DESCRIPTION': "The room is very dark but there is a lantern in the corner on the nightstand"
                         "There is a door south."
                         "The door either leads to the dungeon or an empty room."
                         "The dungeon has some valuable stuff."
                         "But there is a door to the East that leads to the garden.",


            'PATHS': {
                'North': "Loot_room1",
                'South': "Dungeon",
                'East': "Garden"

            }
    },

    'Room 8': {
        'NAME': "Garden",
        'DESCRIPTION':
            "There are rows and rows of flowers"
            "There is one special purple flower named: Supernova to your left."
            "There are two buildings in front of you"
            "To the east, there is a science lab and to the south there is a mini house where the owner is waiting.",

        'PATHS': {
            'West': "Owner’s_room",
            'East': "Science_lab",
            'South': "Owner's_mini_house_entry"

            }
  },




    'Room 9': {
       'NAME': "Science_lab",
       'DESCRIPTION':
           "There are a lot of potions."
           "Looks like the owner or your master was a scientist!",

       'PATHS': {
            'West': "Garden"


            }
  },

   'Room 10': {
      'NAME': "Owner's_mini_house_entry",
      'DESCRIPTION': "You are led straight to the living room.",
                     "All the other two rooms: Kitchen/Bathroom can not be used without permission of master or owner.",
                     "To the east, there is a door to your master’s bedroom."

      'PATHS': {
           'East': "Bedroom",
           'North': "Garden"

            }
   },


  'Room 11': {
     'NAME': "Bedroom",
     'DESCRIPTION': "You have made it!",
                    "Let's see if you have all the things the master needs."
     'PATHS': {
          'West': "Owner's_mini_house_entry"
        }
},


            'Room 12': {
    'NAME': "Dungeon",
    'DESCRIPTION': "There is a sword and a lightsaber."
                   "To the south: Lich room."

                   'PATHS': {
    'South': "Lich_room"






             'Room 13': {
    'NAME': "Lich_room",
    'DESCRIPTION': "Fight the Lich!!!!"
                   "Next room: South: Troll room"

                   'PATHS': {
    'South': "Troll_room"
             'North': "Dungeon"



                      'Room 14': {
    'NAME': "Troll_room",
    'DESCRIPTION': "Fight the troll"
                   "South: where the emerald is."

                   'PATHS': {
    'South': "The_Emerald"
             'North': "Lich_room"


                      'Room 15': {
    'NAME': "The_Emerald ",
    'DESCRIPTION': "The emerald is east of you!"
                   "Take it and go to the garden to see where to go next!"


                   'PATHS': {
    'North': "Troll_room"








































             'Room 11': {
    'NAME': "Bedroom",
    'DESCRIPTION': "You have made it!"
                   "Let's see if you have all the things the master needs."


                   'PATHS': {
    'West': "Owner's_mini_house_entry"


            'Room 12': {
    'NAME': "Dungeon",
    'DESCRIPTION': "There is a sword and a lightsaber."
                   "To the south: Lich room."

                   'PATHS': {
    'South': "Lich_room"






             'Room 13': {
    'NAME': "Lich_room",
    'DESCRIPTION': "Fight the Lich!!!!"
                   "Next room: South: Troll room"

                   'PATHS': {
    'South': "Troll_room"
             'North': "Dungeon"



                      'Room 14': {
    'NAME': "Troll_room",
    'DESCRIPTION': "Fight the troll"
                   "South: where the emerald is."

                   'PATHS': {
    'South': "The_Emerald"
             'North': "Lich_room"


                      'Room 15': {
    'NAME': "The_Emerald ",
    'DESCRIPTION': "The emerald is east of you!"
                   "Take it and go to the garden to see where to go next!"


                   'PATHS': {
    'North': "Troll_room"
