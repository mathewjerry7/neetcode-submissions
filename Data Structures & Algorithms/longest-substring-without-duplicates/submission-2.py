class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        l = 0
        max_length = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            max_length = max(max_length, r-l + 1)
            seen.add(s[r])

        return max_length


#go to this chat called Mastering the sliding window pattern on Claude

#or ask claude to build a Architected interactive stepper 
#to visualize substring algorithm logic using example 'abbacd'