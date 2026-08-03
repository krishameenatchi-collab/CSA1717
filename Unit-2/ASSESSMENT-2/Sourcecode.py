# ==========================================================
# ARTIFICIAL INTELLIGENCE - ASSESSMENT 2
# Python Programs for Questions 1 to 5
# Name : KRISHA MEENATCHI M
# Reg No : 192511338
# ==========================================================

import heapq
import random
import math

# ==========================================================
# QUESTION 1
# EMERGENCY MEDICINE DELIVERY
# GREEDY BEST-FIRST SEARCH & A* SEARCH
# ==========================================================

print("="*70)
print("QUESTION 1 - GREEDY BEST-FIRST SEARCH & A* SEARCH")
print("="*70)

graph = {
    'Base':[('A',2),('B',4)],
    'A':[('C',3),('D',6)],
    'B':[('D',2)],
    'C':[('Hospital',4)],
    'D':[('Hospital',2)],
    'Hospital':[]
}

heuristic = {
    'Base':7,
    'A':6,
    'B':4,
    'C':2,
    'D':1,
    'Hospital':0
}

def greedy(start,goal):
    pq=[(heuristic[start],start,[start])]
    visited=set()

    while pq:
        h,node,path=heapq.heappop(pq)

        if node==goal:
            return path

        if node in visited:
            continue

        visited.add(node)

        for nxt,cost in graph[node]:
            if nxt not in visited:
                heapq.heappush(pq,(heuristic[nxt],nxt,path+[nxt]))

def astar(start,goal):
    pq=[(heuristic[start],0,start,[start])]
    visited=set()

    while pq:

        f,g,node,path=heapq.heappop(pq)

        if node==goal:
            return g,path

        if node in visited:
            continue

        visited.add(node)

        for nxt,cost in graph[node]:

            if nxt not in visited:

                new_g=g+cost
                new_f=new_g+heuristic[nxt]

                heapq.heappush(
                    pq,
                    (new_f,new_g,nxt,path+[nxt])
                )

print("\nGreedy Path")
print(" -> ".join(greedy("Base","Hospital")))

cost,path=astar("Base","Hospital")

print("\nA* Path")
print(" -> ".join(path))
print("Minimum Cost =",cost)

print()

# ==========================================================
# QUESTION 2
# SMART TRAFFIC SIGNAL OPTIMIZATION
# HILL CLIMBING & SIMULATED ANNEALING
# ==========================================================

print("="*70)
print("QUESTION 2 - SMART TRAFFIC SIGNAL OPTIMIZATION")
print("="*70)

target=50

def objective(x):
    return -(x-target)**2

print("\nHill Climbing")

current=random.randint(0,100)

for i in range(20):

    left=current-1
    right=current+1

    best=current

    if objective(left)>objective(best):
        best=left

    if objective(right)>objective(best):
        best=right

    if best==current:
        break

    current=best

print("Best Signal Timing =",current)

print("\nSimulated Annealing")

current=random.randint(0,100)
temperature=100

while temperature>1:

    new=current+random.choice([-1,1])

    delta=objective(new)-objective(current)

    if delta>0 or random.random()<math.exp(delta/temperature):
        current=new

    temperature*=0.90

print("Optimized Timing =",current)

print()

# ==========================================================
# QUESTION 3
# ONLINE SEARCH AGENT - MARS ROVER
# ==========================================================

print("="*70)
print("QUESTION 3 - ONLINE SEARCH AGENT")
print("="*70)

environment=["Safe","Rock","Safe","Crater","Safe","Sample"]

knowledge=[]

for cell in environment:

    print("Observing :",cell)

    knowledge.append(cell)

    if cell=="Rock":
        print("Action : Turn Right")

    elif cell=="Crater":
        print("Action : Move Left")

    elif cell=="Sample":
        print("Action : Collect Sample")

    else:
        print("Action : Move Forward")

print("\nKnowledge Base")

print(knowledge)

print()

# ==========================================================
# QUESTION 4
# CSP USING BACKTRACKING
# UNIVERSITY EXAM TIMETABLE
# ==========================================================

print("="*70)
print("QUESTION 4 - CSP USING BACKTRACKING")
print("="*70)

subjects=["Math","Physics","AI"]

slots=["Day1","Day2","Day3"]

assignment={}

def valid(subject,slot):

    return slot not in assignment.values()

def solve(index):

    if index==len(subjects):
        return True

    subject=subjects[index]

    for slot in slots:

        if valid(subject,slot):

            assignment[subject]=slot

            if solve(index+1):
                return True

            del assignment[subject]

    return False

solve(0)

print("\nExam Timetable")

for s in assignment:

    print(s,"->",assignment[s])

print()

# ==========================================================
# QUESTION 5
# MINIMAX WITH ALPHA-BETA PRUNING
# ==========================================================

print("="*70)
print("QUESTION 5 - MINIMAX WITH ALPHA-BETA PRUNING")
print("="*70)

tree={
'A':['B','C'],
'B':['D','E'],
'C':['F','G'],
'D':3,
'E':5,
'F':2,
'G':9
}

def minimax(node,depth,maximizing,alpha,beta):

    if depth==0:
        return tree[node]

    if maximizing:

        value=-1000

        for child in tree[node]:

            value=max(
                value,
                minimax(child,depth-1,False,alpha,beta)
            )

            alpha=max(alpha,value)

            if beta<=alpha:
                break

        return value

    else:

        value=1000

        for child in tree[node]:

            value=min(
                value,
                minimax(child,depth-1,True,alpha,beta)
            )

            beta=min(beta,value)

            if beta<=alpha:
                break

        return value

answer=minimax('A',2,True,-1000,1000)

print("\nBest Utility Value =",answer)

print()

print("="*70)
print("ALL PROGRAMS EXECUTED SUCCESSFULLY")
print("="*70)
