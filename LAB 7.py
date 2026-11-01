from collections import deque

def bfs(start, goal):
    q = deque([(start, [])])
    seen = [start]

    while q:
        s, path = q.popleft()

        if s == goal:
            return path

        b = s.index(0)

        for j in [b-3, b+3, b-1, b+1]:
            if 0 <= j < 9 and abs(j//3-b//3)+abs(j%3-b%3) == 1:
                t = list(s)
                t[b], t[j] = t[j], t[b]
                t = tuple(t)

                if t not in seen:
                    seen.append(t)
                    q.append((t, path+[t]))

    return None

def show(s):
    for i in range(0, 9, 3):
        print(*["_ " if x == 0 else str(x)+" " for x in s[i:i+3]])

start = tuple(map(int, input("Enter 9 numbers: ").split()))
goal = (1,2,3,4,5,6,7,8,0)

path = bfs(start, goal)

if path is not None:
    print("Initial State:")
    show(start)

    for i, s in enumerate(path, 1):
        print("Step", i)
        show(s)

    print("Total Moves:", len(path))
else:
    print("No solution found.")
