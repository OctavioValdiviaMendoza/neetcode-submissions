class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        set -> track visted islands
        1. figure out if im am currently in an island (grid[i][j] = '1')
        2. figure out its neighboors and add to set and make sure they are not visited

        int var -> keeps track of number of islands
        """

        rows, cols = len(grid), len(grid[0])
        visited = set()
        island_counter = 0

        def dfs(row, col):
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or grid[row][col] == "0"
                or (row, col) in visited
            ):
                return
            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    island_counter += 1
                    dfs(row, col)

        return island_counter
