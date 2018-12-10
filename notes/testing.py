# Math
print(3+5)
print(5-2)
print(3*4)
print(6/2)
print(6 % 2)

print("Figure this out...")
print(6 // 2)
print(5 // 2)
print(9 // 4)

# powers
# what is 2^20
print(2**100)
print(3**27)
num: int(input("Enter a number"))# use this whenever you want them to answer something while it is running

# Equality Statements
print(5 > 3)
print(5 >= 3)
print(3 == 3)
print(3 != 4)

"""
At the moment you START the loop:
For loops - Use when you know EXACTLY how many iterations (how many times)
While loops - Use when you know DON'T know how many iterations    
"""
food_list = ["salad", "pizza", "subway sandwhich", "brownies", "overnight oats", "barbecue chips", "pistachio ice cream", "spinach",
        "chicken", "chocolate", "apple pie", "eggs", "blueberry pie", "cherry pie", "cheeto chips", "mashed potatoes",
        "noodles", "chili", "chocolate chips", "chocolate ice cream", "cheerios"]
print(len(food_list))

# Adding food
food_list.append("bacon")
food_list.append("eggs")
# Notice that everything is object.method(parameters)
print(food_list)
# Removing things from the list
food_list.insert(1, "eggo waffles")
print(food_list.remove("salad"))
# Also removing stuff from a list
print(food_list)# index number and it starts from 0
food_list.pop(0)# removes thing on top = student id so it can add without errors
print(food_list)

