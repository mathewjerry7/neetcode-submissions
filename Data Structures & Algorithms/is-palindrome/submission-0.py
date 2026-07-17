class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean = ""

        for char in s:
            if char.isalnum():
                clean = clean + char.lower()

        return clean == clean[::-1]