import math

# Using a tuple for coordinates
position = (0, 0)  

while True:
    # Take input from the user
    command = input("Enter movement (or type 'STOP' to finish): ").strip()

    if command.upper() == "STOP":
        break

    try:
        # Split the direction and steps
        direction, steps = command.split()
        steps = int(steps)
    except ValueError:
        print("Invalid input. Please enter a direction followed by steps (e.g., 'UP 5').")
        continue

    # Update coordinates based on direction
    x, y = position
    if direction.upper() == "UP":
        position = (x, y + steps)
    elif direction.upper() == "DOWN":
        position = (x, y - steps)
    elif direction.upper() == "LEFT":
        position = (x - steps, y)
    elif direction.upper() == "RIGHT":
        position = (x + steps, y)
    else:
        print("Invalid direction. Use UP, DOWN, LEFT, or RIGHT.")


# Calculate distance from the origin
x, y = position
distance = math.sqrt(x**2 + y**2)
print(f"Distance from the origin: {round(distance)}")


'''Output
Enter movement (or type 'STOP' to finish): up 5
Enter movement (or type 'STOP' to finish): down 3
Enter movement (or type 'STOP' to finish): left 3
Enter movement (or type 'STOP' to finish): right 2
Enter movement (or type 'STOP' to finish): stop
Distance from the origin: 2
'''