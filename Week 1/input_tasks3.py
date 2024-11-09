
print("What is your name?")
name = input()

print("What is your age?")
age = int(input())

print("What is your weight?")
weight = float(input())

print("What is your height?")
height = float(input())


bmi = weight / (height ** 2)


print(f"{name} your bmi is {bmi}")