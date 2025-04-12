import unittest
from sudoku import solve_sudoku

class TestSudokuSolver(unittest.TestCase):

    def test_solve_valid_board_1(self):
        grid = [
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
        solution = solve_sudoku([row[:] for row in grid])
        self.assertIsNotNone(solution)
        for row in solution:
            self.assertTrue(all(1 <= n <= 9 for n in row))

    def test_solve_valid_board_2(self):
        grid = [
            [0, 0, 0, 0, 0, 0, 2, 0, 0],
            [0, 8, 0, 0, 0, 7, 0, 9, 0],
            [6, 0, 2, 0, 0, 0, 5, 0, 0],
            [0, 7, 0, 0, 6, 0, 0, 0, 0],
            [0, 0, 0, 9, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 4, 0],
            [0, 0, 5, 0, 0, 0, 6, 0, 3],
            [0, 9, 0, 4, 0, 0, 0, 7, 0],
            [0, 0, 6, 0, 0, 0, 0, 0, 0]
        ]
        solution = solve_sudoku([row[:] for row in grid])
        self.assertIsNotNone(solution)
        for row in solution:
            self.assertTrue(all(1 <= n <= 9 for n in row))

    def test_invalid_duplicate_row(self):
        grid = [
            [5, 5, 8, 0, 0, 0, 0, 1, 6],  # (invalid)
            [5, 0, 0, 0, 9, 2, 0, 0, 8],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [9, 0, 0, 3, 0, 0, 8, 2, 0],
            [0, 2, 0, 0, 0, 0, 0, 7, 0],
            [0, 8, 4, 0, 0, 6, 0, 0, 5],
            [0, 0, 0, 0, 0, 3, 0, 0, 0],
            [4, 0, 0, 9, 6, 0, 0, 0, 2],
            [1, 6, 0, 0, 0, 0, 7, 0, 0]
        ]
        self.assertIsNone(solve_sudoku([row[:] for row in grid]))

    def test_invalid_duplicate_column(self):
        grid = [
            [5, 0, 8, 0, 0, 0, 0, 1, 6],
            [5, 0, 0, 0, 9, 2, 0, 0, 8],  # (invalid)
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [9, 0, 0, 3, 0, 0, 8, 2, 0],
            [0, 2, 0, 0, 0, 0, 0, 7, 0],
            [0, 8, 4, 0, 0, 6, 0, 0, 5],
            [0, 0, 0, 0, 0, 3, 0, 0, 0],
            [4, 0, 0, 9, 6, 0, 0, 0, 2],
            [1, 6, 0, 0, 0, 0, 7, 0, 0]
        ]
        self.assertIsNone(solve_sudoku([row[:] for row in grid]))

    def test_already_solved(self):
        # A valid completed puzzle
        solved_grid = [
            [8, 2, 7, 1, 5, 4, 3, 9, 6],
            [9, 6, 5, 3, 2, 7, 1, 4, 8],
            [3, 4, 1, 6, 8, 9, 7, 5, 2],
            [5, 9, 3, 4, 6, 8, 2, 7, 1],
            [4, 7, 2, 5, 1, 3, 6, 8, 9],
            [6, 1, 8, 9, 7, 2, 4, 3, 5],
            [7, 8, 6, 2, 3, 5, 9, 1, 4],
            [1, 5, 4, 7, 9, 6, 8, 2, 3],
            [2, 3, 9, 8, 4, 1, 5, 6, 7]
        ]
        result = solve_sudoku([row[:] for row in solved_grid])
        self.assertEqual(result, solved_grid)

    def test_empty_board(self):
        empty_grid = [[0 for _ in range(9)] for _ in range(9)]
        solution = solve_sudoku(empty_grid)
        self.assertIsNotNone(solution)
        for row in solution:
            self.assertTrue(all(1 <= n <= 9 for n in row))


if __name__ == '__main__':
    unittest.main()
