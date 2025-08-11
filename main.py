grid = [[" "]*3 for _ in range(3)]
p1, s1 = input("Player 1 name: "), input("Symbol: ")
p2, s2 = input("Player 2 name: "), input("Symbol: ")
turn = True

def print_grid():
    for i, row in enumerate(grid):
        print("  |  ".join(row))
        if i < 2: print("---+---+---")

def check_winner():
    lines = grid + [list(c) for c in zip(*grid)] + [[grid[i][i] for i in range(3)], [grid[i][2-i] for i in range(3)]]
    for line in lines:
        if line == [s1]*3: return p1
        if line == [s2]*3: return p2
    if all(c != " " for r in grid for c in r): return "Tie"

while True:
    print_grid()
    cp, cs = (p1, s1) if turn else (p2, s2)
    try:
        c = int(input(f"{cp} ({cs}), 1-9: ")) - 1
        if 0 <= c < 9 and grid[c//3][c%3] == " ":
            grid[c//3][c%3] = cs
            res = check_winner()
            if res:
                print_grid()
                print("Tie!" if res == "Tie" else f"Winner: {res}")
                break
            turn = not turn
        else: print("Invalid move.")
    except: print("Enter 1-9.")
