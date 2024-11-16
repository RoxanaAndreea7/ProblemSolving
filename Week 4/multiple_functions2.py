def sum_weights(person_weight, inventory_weight):
    total_weight = person_weight + inventory_weight
    return total_weight

def calc_avg_weight(person_weight, inventory_weight):
    avg_weight = sum_weights(person_weight, inventory_weight) / 2
    return avg_weight

def run():
    print("What is the weight of the person?")
    person_weight = float(input())

    print("What is the weight of their inventory?")
    inventory_weight = float(input())

    print("What would you like to calculate (sum or average)?")
    action = input()

    if action == "sum":
        answer = sum_weights(person_weight, inventory_weight)
        print(f"The sum of weights is {answer:.2f}")
    elif action == "average":
        answer = calc_avg_weight(person_weight, inventory_weight)
        print(f"The average weight is {answer:.2f}")
    else:
        print("I am not sure what you would like to do.")

run()