print ("How many obstacles I must avoid?")

user_obstacle = int(input())

initial_no_obstacles = 0

while initial_no_obstacles < user_obstacle:
    print("avoiding...")
    initial_no_obstacles += 1
    print(f"Done{initial_no_obstacles}")