# sudoku_solver.py

def printGrid(grid):
    for i in range(0, 9):
        if i > 0 and i % 3 == 0:
            print("------+-------+------")
        for j in range(0, 9):
            if j > 0 and j % 3 == 0:
                print("| ", end="")
            n = grid[i][j]
            c = "." if n == 0 else str(n)
            print(c, end=" ")
        print()

def is_valid(grid, row, col, n):
    for i in range(9):
        if grid[row][i] == n or grid[i][col] == n:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == n:
                return False
    return True


def test_invalid_board(self):
    # Duplicate 5 in the first row => invalid board
    invalid_grid = [
        [5, 5, 8, 0, 0, 0, 0, 1, 6],
        [5, 0, 0, 0, 9, 2, 0, 0, 8],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [9, 0, 0, 3, 0, 0, 8, 2, 0],
        [0, 2, 0, 0, 0, 0, 0, 7, 0],
        [0, 8, 4, 0, 0, 6, 0, 0, 5],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [4, 0, 0, 9, 6, 0, 0, 0, 2],
        [1, 6, 0, 0, 0, 0, 7, 0, 0]
    ]

    result = solve_sudoku([row[:] for row in invalid_grid])
    self.assertIsNone(result)


def validate_board(grid):
    def has_duplicates(block):
        nums = [n for n in block if n != 0]
        return len(nums) != len(set(nums))

    for i in range(9):
        row = grid[i]
        col = [grid[j][i] for j in range(9)]
        if has_duplicates(row) or has_duplicates(col):
            return False

    for box_row in range(3):
        for box_col in range(3):
            block = [
                grid[r][c]
                for r in range(box_row * 3, box_row * 3 + 3)
                for c in range(box_col * 3, box_col * 3 + 3)
            ]
            if has_duplicates(block):
                return False

    return True

def solve_sudoku(grid):
    if not validate_board(grid):
        return None
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for n in range(1, 10):
                    if is_valid(grid, row, col, n):
                        grid[row][col] = n
                        result = solve_sudoku(grid)
                        if result:
                            return result
                        grid[row][col] = 0
                return None
    return grid


grid0 = [
    [0, 0, 8, 0, 0, 0, 0, 1, 6],
    [5, 0, 0, 0, 9, 2, 0, 0, 8],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [9, 0, 0, 3, 0, 0, 8, 2, 0],
    [0, 2, 0, 0, 0, 0, 0, 7, 0],
    [0, 8, 4, 0, 0, 6, 0, 0, 5],
    [0, 0, 0, 0, 0, 3, 0, 0, 0],
    [4, 0, 0, 9, 6, 0, 0, 0, 2],
    [1, 6, 0, 0, 0, 0, 7, 0, 0]
]

print("Original Sudoku:")
printGrid(grid0)

solution = solve_sudoku([row[:] for row in grid0])  # Deep copy to avoid modifying original

print("\nSolved Sudoku:")

if solution:
    printGrid(solution)
else:
    print("No solution found.")
