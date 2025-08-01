import os
os.system('cls')

def spiral_order(matrix):

    m = len(matrix)
    n = len(matrix[0])
    sol = []
    row, col = 0, 0
    rb, db, lb, ub = n - 1, m - 1, 0, 0

    while len(sol) < n*m:
        # Right
        for col in range(lb, rb + 1):
            sol.append(matrix[ub][col])
        ub += 1 

        # Down
        for row in range(ub, db + 1):
            sol.append(matrix[row][rb])
        rb -= 1 

        if ub <= db:
            # Left
            for col in range(rb, lb - 1, -1):
                sol.append(matrix[db][col])
            db -= 1 

        if lb <= rb:
            # UP
            for row in range(db, ub - 1, -1):
                sol.append(matrix[row][lb])
            lb += 1 

    return sol

m = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12]]

print(spiral_order(m))

