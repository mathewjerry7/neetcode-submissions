class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l1 = len(s1)
        l2 = len(s2)

        if l1 > l2:
            return False
        
        s1Count = [0]*26
        s2Count = [0]*26

        for i in range(l1):
            s1Count[ord(s1[i])-ord('a')] += 1
            s2Count[ord(s2[i])-ord('a')] += 1

        if s1Count == s2Count:
            return True

        for i in range(l1,l2):
            s2Count[ord(s2[i])-ord('a')] += 1
            s2Count[ord(s2[i-l1])-ord('a')] -= 1

            if s1Count == s2Count:
                return True
        
        return False

