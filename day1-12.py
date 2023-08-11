from collections import deque

# State class to represent the current state of the problem
class State:
    def __init__(self, missionaries_left, cannibals_left, boat_left):
        self.missionaries_left = missionaries_left
        self.cannibals_left = cannibals_left
        self.boat_left = boat_left
        self.parent = None

    def is_valid(self):
        if self.missionaries_left < 0 or self.missionaries_left > 3:
            return False
        if self.cannibals_left < 0 or self.cannibals_left > 3:
            return False
        if self.missionaries_left < self.cannibals_left and self.missionaries_left > 0:
            return False
        if 3 - self.missionaries_left < 3 - self.cannibals_left and 3 - self.missionaries_left > 0:
            return False
        return True

    def is_goal(self):
        return self.missionaries_left == 0 and self.cannibals_left == 0

    def generate_successors(self):
        successors = []
        if self.boat_left:
            move_options = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        else:
            move_options = [(-1, 0), (-2, 0), (0, -1), (0, -2), (-1, -1)]

        for move in move_options:
            new_state = State(
                self.missionaries_left + move[0],
                self.cannibals_left + move[1],
                not self.boat_left
            )
            new_state.parent = self
            if new_state.is_valid():
                successors.append(new_state)
        return successors

# Function to solve the Missionaries and Cannibals Problem using BFS
def solve_missionaries_cannibals():
    initial_state = State(3, 3, True)
    queue = deque([initial_state])
    visited = set([initial_state])

    while queue:
        current_state = queue.popleft()

        if current_state.is_goal():
            return current_state

        successors = current_state.generate_successors()
        for successor in successors:
            if successor not in visited:
                queue.append(successor)
                visited.add(successor)

    return None

# Function to print the path from initial state to goal state
def print_solution(solution_state):
    path = []
    current = solution_state
    while current:
        path.append(current)
        current = current.parent

    for state in reversed(path):
        print(f"Missionaries: {state.missionaries_left}, Cannibals: {state.cannibals_left}, Boat: {'Left' if state.boat_left else 'Right'}")

# Solve and print the solution
solution = solve_missionaries_cannibals()
if solution:
    print("Solution found:")
    print_solution(solution)
else:
    print("No solution found.")
