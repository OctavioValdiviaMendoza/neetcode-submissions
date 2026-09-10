from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])

        visit = set()
        island = 0

        def bfs(r,c):
            visit.add((r,c))
            q = deque()
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = ((row+1,col),(row-1,col),(row,col+1),(row,col-1))
                for row, col in directions:
                    if  0 <= row < rows and 0 <= col < cols and grid[row][col] == "1" and (row,col) not in visit:
                        visit.add((row,col))
                        q.append((row,col))
                        




        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    island += 1
                    bfs(r, c)
        return island
