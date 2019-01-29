states = {
    "CA": "California",
    "FL": "Florida",
    "AK": "Alaska",
    "GA": "Georgia"

}
print(states["CA"])
print(states["AK"])


nested_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 2130000
    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 737000

    },
    "GA": {
        "NAME": "Georgia",
        "POPULATION": 10500000
    },

}
print(nested_dictionary["GA"]["POPULATION"])

print(nested_dictionary["FL"]["NAME"])

print(nested_dictionary["GA"])


georgia = nested_dictionary["GA"]
print("georgia")


complex_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000,
        "CITIES": [
            "Fresno",
            "San Francisco",
            "Los Angelas"
        ]
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 2130000,
        "Cities": [
            "Miami",
            "Tampa",
            "Jacksonville",

        ]
    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 737000,
        "Cities": [
            "Anchorage",
            "Fairbanks",
            "Juneau"
        ]

    },
    "GA": {
        "NAME": "Georgia",
        "POPULATION": 10500000
        "Cities": [
            "Atlanta",
            "Savannah",
            "Augusta"
        ]
    }
}
print(complex_dictionary["AK"]["CITIES"][0])













