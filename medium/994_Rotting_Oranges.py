class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        fresh = 0
        queue = []
        ans = 0
        direction = [[-1,0],[1,0],[0,1],[0,-1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        while queue != []:
            for i in range(len(queue)):
                data = queue.pop(0)
                for j in range(4):
                    x = data[0] + direction[j][0]
                    y = data[1] + direction[j][1]
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                        grid[x][y] = 2;
                        queue.append([x, y]);
                        fresh -= 1
            ans += 1
        if fresh == 0:
            return ans - 1
        else:
            return -1
            
