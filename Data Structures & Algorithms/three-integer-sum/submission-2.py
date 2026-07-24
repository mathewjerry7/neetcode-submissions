class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        ret = []

        for i in range(len(nums)):
            #Step 4
            if i!=0 and nums[i] == nums[i-1]:
                continue

            #Step 1
            left = i+1
            right = len(nums) - 1

            #Step 2
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left +=1
                elif total > 0:
                    right -=1
                else:
                    ret.append([nums[i],nums[left],nums[right]])
                    left +=1

                    #Step 3
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
        return ret