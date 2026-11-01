N = 8

def safe(b, r, c):
    for i in range(r):
        if b[i][c] == 1:
            return False

        if c-(r-i) >= 0 and b[i][c-(r-i)] == 1:
            return False

        if c+(r-i) < N and b[i][c+(r-i)] == 1:
            return False
    return True

def solve(b, r):
    if r == N:
        return True
    for c in range(N):
        if safe(b, r, c):
            b[r][c] = 1

            if solve(b, r+1):
                return True
            b[r][c] = 0
    return False

board = [[0]*N for _ in range(N)]

if solve(board, 0):
    print("8 Queens Solution:")
    for row in board:
        print(*["Q" if x else "." for x in row])
else:
    print("No solution")
