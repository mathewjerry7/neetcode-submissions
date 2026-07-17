class Solution:
    def findMin(self, nums: List[int]) -> int:

        """   
        [3, 4, 5, 1, 2]
        b     m     e

        [1, 2, 3, 4, 5]
        b     m     e

        """
        beg = 0
        end = len(nums) - 1

        while beg < end:
            mid = (beg + end) //2
            if nums[mid] > nums[end]:
                beg = mid + 1 # minimum is in the right half
            elif nums[mid] < nums[end]:
                end = mid # minimum is in the left half including mid
    
        return nums[end]
