class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(log(mn)) / O(1)
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n-1
        while l < r:
            mid = (l+r)//2
            if matrix[mid//n][mid % n] < target:
                l = mid + 1
            else:
                r = mid
        return matrix[l//n][l % n] == target
