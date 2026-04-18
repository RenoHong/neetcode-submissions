class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for m in range(0,len(matrix)): 
            n = len(matrix[m])
            if target == matrix[m][0] or target == matrix[m][n-1]:
                return True
            if target > matrix[m][0] and target < matrix[m][n -1]:
                l = 0 
                while(l<=n):
                    mid = l + ((n -l)>>1)
                    if matrix[m][mid] == target:
                        return True
                    elif matrix[m][mid] < target: 
                        l = mid +1
                    else:
                        n = mid -1
        return False



        