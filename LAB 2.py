import heapq

GOAL = (1,2,3,4,5,6,7,8,0)

def heuristic(s):
    d = 0
    for i, v in enumerate(s):
        if v != 0:
            j = GOAL.index(v)
            d += abs(i//3 - j//3) + abs(i%3 - j%3)
    return d

def neighbors(s):
    result = []
    b = s.index(0)
    r, c = b//3, b%3

    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr*3 + nc
            t = list(s)
            t[b], t[j] = t[j], t[b]
            result.append(tuple(t))
    return result

def a_star(start):
    pq = [(heuristic(start), 0, start, [])]
    visited = set()

    while pq:
        f, g, s, path = heapq.heappop(pq)

        if s in visited:
            continue
        visited.add(s)
        path = path + [s]

        if s == GOAL:
            return path

        for n in neighbors(s):
            if n not in visited:
                ng = g + 1
                heapq.heappush(pq, (ng+heuristic(n), ng, n, path))
    return None

def display(s):
    for i in range(0, 9, 3):
        print(*["_" if x == 0 else x for x in s[i:i+3]])
    print()

start = tuple(map(int, input("Enter 9 numbers (0 for blank): ").split()))
solution = a_star(start)

if solution:
    print("Solution Found! Moves:", len(solution)-1)
    for i, s in enumerate(solution):
        print("Step", i)
        display(s)
else:
    print("No solution found.")
