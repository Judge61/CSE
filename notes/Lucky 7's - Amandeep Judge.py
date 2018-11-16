import random
playing = True

money = int(15)
rounds = 0
max_money = int(15)
max_rounds = 0

while money > 0:
    D6 = random.randint(1, 6)
    D1 = random.randint(1, 6)
    roll = D1+D6
    if roll == 7:
        money += 4
        print("You rolled a %s and %s" % (D1, D6))
        print(money)
        rounds += 1
        if max_money < money:
            max_money = money
            max_rounds = rounds
    elif roll > 7:
        money -= 1
        print("You rolled a %s and %s" % (D1, D6))
        print(money)
        rounds += 1
    else:
        money -= 1
        print("You rolled a %s and %s" % (D1, D6))
        print(money)
        rounds += 1


print("You rolled %s rounds" % rounds)
print("Your maximum amount was %s" % max_money)
print("You should have stopped at round %s" % max_rounds)









