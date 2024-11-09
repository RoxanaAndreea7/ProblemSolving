
print("Where should I look?")
place = input()


if place == "in the bedroom":
    print("Where in the bedroom should I look?")
    bedroom_place = input()

    if bedroom_place == "under the bed":
        print("Found some shoes but no phone")
    else:
        print("Found some mess but no phone.")


elif place == "in the bathroom":
    print("Where in the bathroom should I look?")
    bathroom_place = input()

    if bathroom_place == "in the bathtub":
        print("Found a rubber duck but no phone")
    else:
        print("Found some stuff but no phone.")


elif place == "in the living room":
    print("Where in the living room should I look?")
    lab_place = input()

    if lab_place == "on the table":
        print("Yes! I found my phone!")
    else:
        print("Found some stuff but no phone.")

else:
    print("I am not sure where that place is located.")