print("How many numbers you want to add?")
numbers = int(input())

sum_of_numbers = 0

total = 0

while sum_of_numbers < numbers:
    print(f"Please enter number {sum_of_numbers + 1} of {numbers}:")
    sum_number = int(input())

    total = total + sum_number
    sum_of_numbers = sum_of_numbers + 1

print(f"...Done! Total of all numbers is {total}.")