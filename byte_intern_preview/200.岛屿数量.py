#
# @lc app=leetcode.cn id=200 lang=python
#
# [200] 岛屿数量
#
#图论深度优先搜索，时间复杂度为O(M*N),空间复杂度为O()
# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m,n = len(grid),len(grid[0])
        count = 0
        # dfs函数负责把所有与(i,j)相连的陆地('1')全部铲除
        def dfs(i,j):
            #1.递归终止条件，越过网格边界或遇到水域或者已经被销毁过的陆地('0')
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return
            
            #2.否则即遇到陆地，直接销毁为'0'
            grid[i][j] = '0'

            #3.向四周扩散，上下左右
            dfs(i-1,j) #上
            dfs(i+1,j) #下
            dfs(i,j-1) #左
            dfs(i,j+1) #右
        
        #迭代每个网格格子，判断是否为陆地'1'，若正确则计数,同时对该格子(i,j)实行销毁
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i,j)
        
        # 循环结束返回计数
        return count
  
# @lc code=end
# BFS 时间复杂度O(M*N)m每个网格只会入队出队以一次，空间复杂度为O(min(M,N))
from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m,n = len(grid),len(grid[0])
        count = 0

        def bfs(i,j):
            queue = deque()
            queue.append((i,j))
            grid[i][j] = '0' #入队即淹没避免重复入队
            while queue:
                x,y =  queue.popleft()
                # 检查四个方向
                for dx,dy in [(-1,0),(1,0),(0,1),(0-1)]:
                    nx = x + dx
                    ny = y + dy
                    # 检查令居是否是合法的陆地
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                        grid[nx][ny] = '0'# 一旦是就先标记
                        queue.append((nx,ny)) #再入队

        # 主循环
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    bfs(i,j)
        
        return count
