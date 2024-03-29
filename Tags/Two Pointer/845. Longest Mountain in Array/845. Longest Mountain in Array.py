class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) < 3:
            return 0

        mountain = 0

        for i in range(1, len(arr)-1):
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                left, right = i - 1, i + 1
                while left > 0 and arr[left-1] < arr[left]:
                    left -= 1
                while right < len(arr) - 1 and arr[right] > arr[right+1]:
                    right += 1
                mountain = max(mountain, right - left + 1)
        return mountain
