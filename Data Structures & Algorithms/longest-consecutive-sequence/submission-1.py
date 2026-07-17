class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        sorted_nums = sorted(nums)

        streak = 1
        longest = 1


        [2,20,4,10,3,4,5]
        [2,3,4,4,5,10,20]

        for i in range(1,len(sorted_nums)):

            if sorted_nums[i] == sorted_nums[i-1]:
                continue

            elif sorted_nums[i] == sorted_nums[i-1] + 1:
                streak += 1
                longest = max(longest,streak)

            else:
                streak = 1

        return longest

            
