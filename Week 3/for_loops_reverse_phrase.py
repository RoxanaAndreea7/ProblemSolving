print("What phrase do you want to see in reverse?")
phrase = input()

print("\nReversing...")
print("The phrase is ", end="")

for position in range(len(phrase) - 1, -1, -1):
    print(phrase[position], end="")