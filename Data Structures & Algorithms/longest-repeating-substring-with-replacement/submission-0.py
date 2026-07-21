from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #Step 1
        l = 0
        result = 0

        #Step 4
        count = defaultdict(int)
        maxC = 0
        
        #Step 1
        for r in range(len(s)):

            #Step 3
            count[s[r]] += 1

            maxC = max(maxC, count[s[r]])

            #Step 2
            while (r - l + 1) - maxC > k:
                count[s[l]] -= 1
                l +=1

            #Step 1
            result = max(result, r - l + 1)

        #Step 1
        return result

        