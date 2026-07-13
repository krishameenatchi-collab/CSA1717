from collections import deque
# Capacities
CAP1 = 4
CAP2 = 3
TARGET = (2, 0)
def get_next_states(x, y):
    states = []
    # Fill either jug
    states.append((CAP1, y))
    states.append((x, CAP2))
    # Empty either jug
    states.append((0, y))
    states.append((x, 0))
    # Pour Jug1 -> Jug2
    transfer = min(x, CAP2 - y)
    states.append((x - transfer, y + transfer))
    # Pour Jug2 -> Jug1
    transfer = min(y, CAP1 - x)
    states.append((x + transfer, y - transfer))
    return states

def bfs():
    queue = deque()
    queue.append(((0, 0), []))
    visited = set()
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        path = path + [(x, y)]
        if (x, y) == TARGET:
            return path
        for state in get_next_states(x, y):
            if state not in visited:
                queue.append((state, path))
    return None
solution = bfs()
print("Steps:")
for step in solution:
    print(step)
