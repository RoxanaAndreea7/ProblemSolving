print("How far are we from the target?")
no_of_steps = int(input())

for count in range(no_of_steps, 0 , -1):
    print(f"{count} steps remaining")

print ("Target achieved!")