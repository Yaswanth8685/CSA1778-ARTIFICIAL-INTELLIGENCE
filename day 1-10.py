from collections import deque

# Function to solve the Water Jug Problem using BFS
def water_jug_problem(x_cap, y_cap, target):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue
        
        visited.add((x, y))

        if x == target or y == target:
            return True
        
        # Filling operations
        queue.append((x_cap, y))
        queue.append((x, y_cap))
        
        # Emptying operations
        queue.append((0, y))
        queue.append((x, 0))
        
        # Pouring operations
        pour_x_to_y = min(x, y_cap - y)
        queue.append((x - pour_x_to_y, y + pour_x_to_y))
        pour_y_to_x = min(y, x_cap - x)
        queue.append((x + pour_y_to_x, y - pour_y_to_x))

    return False

# Example usage
x_capacity = 4  # Capacity of the first jug
y_capacity = 3  # Capacity of the second jug
target_volume = 2  # Desired water volume

if water_jug_problem(x_capacity, y_capacity, target_volume):
    print("Solution exists.")
else:
    print("No solution exists.")



print("y.siva yaswanth,192110073")
