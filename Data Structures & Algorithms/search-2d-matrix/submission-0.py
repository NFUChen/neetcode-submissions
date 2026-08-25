class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            if row[-1] < target:
                continue
            left = 0
            right = len(row) - 1
            while (left <= right):
                mid = (right + left) // 2
                if row[mid] == target:
                    return True
                
                else:
                    if row[mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1

        return False