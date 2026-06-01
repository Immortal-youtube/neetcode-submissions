class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        k = ""
        for i in s:
            if i.isalnum():
                k += i
        return k.lower() == k.lower()[::-1]
        