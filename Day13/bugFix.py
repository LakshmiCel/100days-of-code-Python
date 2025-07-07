from random import randint
dice_image = ["1", "2", "3", "4", "5", "6"]
dice_roll = randint(0, 5)
print(f"You rolled a {dice_roll}{dice_image[dice_roll]}")