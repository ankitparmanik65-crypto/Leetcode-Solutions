class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        size = m * n

        # Result grid
        ans = [[0] * n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                # Convert (row, col) to 1D index
                index = row * n + col

                # Find new index after shifting
                new_index = (index + k) % size

                # Convert back to 2D coordinates
                new_row = new_index // n
                new_col = new_index % n

                ans[new_row][new_col] = grid[row][col]

        return ans