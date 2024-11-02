print("What level of brightness is requires?")

brightness_level = int(input())

for brightness in range(2,brightness_level,2):
    print(f"Brightness level is : {'*' *brightness} ")

print("Complete!")