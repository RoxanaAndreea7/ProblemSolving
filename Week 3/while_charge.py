print("How many bars should I be charged?")

user_charged = int(input())

initial_no_charged = 0

while initial_no_charged < user_charged:
    initial_no_charged += 1
    print(f"charging:{ "_" * initial_no_charged}")

print ("Batery is fully charged")
