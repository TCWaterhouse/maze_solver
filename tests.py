import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 50
        num_rows = 60
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m2._cells),
            num_cols,
        )
        self.assertEqual(
            len(m2._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 10
        num_rows = 10
        m4 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m4._break_entrance_and_exit()
        self.assertEqual(
            m4._cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m4._cells[m4._num_cols - 1][m4._num_rows - 1].has_bottom_wall,
            False
        )

if __name__ == "__main__":
    unittest.main()