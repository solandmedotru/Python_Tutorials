import random


def roll():
    return random.randint(1, 6)


die1 = roll()
die2 = roll()
total = die1 + die2

print("На ваших кубиках выпало", die1, "и", die2, "очков. В сумме", total)
input("\n\nНажмите Enter, чтобы выйти.")

