# ==========================================================
# ARTIFICIAL INTELLIGENCE - ASSESSMENT 2
# Python Programs for Questions 1 to 3
# Name : KRISHA MEENATCHI M
# Reg No : 192511338
# ==========================================================


# ==========================================================
# QUESTION 1 - DOCTOR SHIFT SCHEDULING USING BACKTRACKING
# ==========================================================

print("=" * 60)
print("QUESTION 1 - DOCTOR SHIFT SCHEDULING")
print("=" * 60)

doctors = ["D1", "D2", "D3"]
shifts = ["Morning", "Afternoon", "Night"]

assignment = {}


def is_valid(doctor, shift):

    # D1 cannot work Night
    if doctor == "D1" and shift == "Night":
        return False

    # D3 cannot work Morning
    if doctor == "D3" and shift == "Morning":
        return False

    # One doctor per shift
    if shift in assignment.values():
        return False

    return True


def backtrack(index):

    if index == len(doctors):

        # Check D2 before D3
        order = {"Morning": 1, "Afternoon": 2, "Night": 3}

        if order[assignment["D2"]] < order[assignment["D3"]]:
            return True
        else:
            return False

    doctor = doctors[index]

    for shift in shifts:

        if is_valid(doctor, shift):

            assignment[doctor] = shift

            if backtrack(index + 1):
                return True

            del assignment[doctor]

    return False


if backtrack(0):

    print("\nValid Shift Schedule\n")

    for doctor in doctors:
        print(doctor, "->", assignment[doctor])

else:
    print("No Solution Found")

print("\n")


# ==========================================================
# QUESTION 2 - ROBOT GRID NAVIGATION USING BFS
# ==========================================================

from collections import deque

print("=" * 60)
print("QUESTION 2 - ROBOT GRID NAVIGATION")
print("=" * 60)

grid = [

['S', 0, 1, 0, 0],

[0, 1, 0, 1, 0],

[0, 0, 0, 1, 0],

[1, 1, 0, 0, 0],

[0, 0, 0, 1, 'G']

]

rows = len(grid)
cols = len(grid[0])

start = (0, 0)
goal = (4, 4)

moves = [

(-1, 0),

(1, 0),

(0, -1),

(0, 1)

]


def bfs():

    queue = deque([(start, [start])])

    visited = set()

    while queue:

        node, path = queue.popleft()

        if node == goal:
            return path

        if node in visited:
            continue

        visited.add(node)

        x, y = node

        for dx, dy in moves:

            nx = x + dx
            ny = y + dy

            if 0 <= nx < rows and 0 <= ny < cols:

                if grid[nx][ny] != 1 and (nx, ny) not in visited:

                    queue.append(((nx, ny), path + [(nx, ny)]))

    return None


path = bfs()

print("\nShortest Path\n")

for p in path:
    print(p)

print("\nTotal Cost =", len(path) - 1)

print("\nManhattan Distance from Start to Goal =",
      abs(4 - 0) + abs(4 - 0))

print("\n")


# ==========================================================
# QUESTION 3 - AUTONOMOUS RESCUE ROBOT USING UCS
# ==========================================================

print("=" * 60)
print("QUESTION 3 - AUTONOMOUS RESCUE ROBOT")
print("=" * 60)

import heapq

graph = {

'Base':[('A',2),('B',5)],

'A':[('C',3),('D',4)],

'B':[('D',2)],

'C':[('Victim',4)],

'D':[('Victim',1)],

'Victim':[]

}


def ucs(start, goal):

    pq = [(0, start, [start])]

    visited = set()

    while pq:

        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return cost, path

        if node in visited:
            continue

        visited.add(node)

        for neighbour, weight in graph[node]:

            if neighbour not in visited:

                heapq.heappush(

                    pq,

                    (cost + weight,
                     neighbour,
                     path + [neighbour])

                )


cost, path = ucs("Base", "Victim")

print("\nOptimal Rescue Path\n")

print(" -> ".join(path))

print("\nMinimum Cost =", cost)

print("\nRobot Actions")

print("---------------------")

print("Scanning Area")

print("Avoiding Obstacles")

print("Finding Victim")

print("Rescuing Victim")

print("Sending Location to Rescue Team")

print("\n")

print("=" * 60)
print("ALL PROGRAMS EXECUTED SUCCESSFULLY")
print("=" * 60)
