class Solution(object):
    def minOperationsToBalanceGrid(grid):
        n = len(grid)
        
        row_sums = [sum(row) for row in grid]
        col_sums = [sum(grid[i][j] for i in range(n)) for j in range(n)]
        
        target_sum = max(max(row_sums), max(col_sums))
        
        operations = 0
        
        for i in range(n):
            for j in range(n):
                diff = min(target_sum - row_sums[i], target_sum - col_sums[j])
                
                grid[i][j] += diff
                
                row_sums[i] += diff
                col_sums[j] += diff
                
                operations += diff
        
        return operations


    grid = [[1, 1], [1, 1]]


    print(minOperationsToBalanceGrid(grid))  # Output: 8


