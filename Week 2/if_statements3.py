
print("Towards which direction should I go (up, down, left or right)?")
direction = input()


if direction == "up":
    print("I am moving in the upward direction!")
elif direction == "down":
    print("I am moving in the downward direction!")
elif direction == "left":
    print("I am moving in the leftward direction!")
elif direction == "right":
    print("I am moving in the rightward direction!")
else:
    print("Not sure which direction to move!")