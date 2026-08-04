import heapq

# Graph represented as an adjacency list
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 3), ('D', 7), ('E', 2)],
    'C': [('A', 4), ('B', 3), ('E', 3)],
    'D': [('B', 7), ('E', 2), ('G', 2)],
    'E': [('B', 2), ('C', 3), ('D', 2)],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 2,
    'G': 0
}


def a_star(graph, heuristic, start, goal):
    # Priority queue stores (f_cost, g_cost, current_node, path)
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))

    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        print("-------------------------------------")
        print("Current Node :", current)
        print("Path         :", " -> ".join(path))
        print("g(n) =", g)
        print("h(n) =", heuristic[current])
        print("f(n) =", f)

        if current == goal:
            return path, g

        if current in visited:
            continue

        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(open_list,
                               (new_f, new_g, neighbor, path + [neighbor]))

    return None, float("inf")


# Main Program
while True:

    start = input("\nEnter Start Node : ").upper()
    goal = input("Enter Goal Node  : ").upper()

    if start not in graph or goal not in graph:
        print("Invalid Node! Please enter valid nodes.")
        continue

    path, cost = a_star(graph, heuristic, start, goal)

    print("\n========== RESULT ==========")

    if path:
        print("Shortest Path :", " -> ".join(path))
        print("Total Cost :", cost)
    else:
        print("No Path Found")

    choice = input("\nDo you want to search again? (y/n): ").lower()

    if choice != 'y':
        print("Program Exited.")
        break
