class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                
            max_length = max(max_length, right-left + 1)
            seen.add(s[right])
        
        return max_length

#go to this chat called Mastering the sliding window pattern on Claude

#or ask claude to build a Architected interactive stepper 
#to visualize substring algorithm logic using example 'abbacd'