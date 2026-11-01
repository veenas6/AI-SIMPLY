
b = [" "] * 9

def show():
    for i in range(0, 9, 3):
        print(b[i:i+3])

def check():
    w = [(0,1,2),(3,4,5),(6,7,8),
         (0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,c,d in w:
        if b[a] == b[c] == b[d] != " ":
            return b[a]
    return "Draw" if " " not in b else None

def minimax(ai):
    r = check()
    if r == "O": return 1
    if r == "X": return -1
    if r == "Draw": return 0

    s = []
    for i in range(9):
        if b[i] == " ":
            b[i] = "O" if ai else "X"
            s.append(minimax(not ai))
            b[i] = " "
    return max(s) if ai else min(s)

def best():
    score, move = -999, 0
    for i in range(9):
        if b[i] == " ":
            b[i] = "O"
            s = minimax(False)
            b[i] = " "
            if s > score:
                score, move = s, i
    return move

while True:
    show()
    p = int(input("Enter position (1-9): ")) - 1

    if p not in range(9) or b[p] != " ":
        print("Invalid move")
        continue

    b[p] = "X"
    if check():
        show()
        print("Result:", check())
        break

    b[best()] = "O"
    if check():
        show()
        print("Result:", check())
        break
