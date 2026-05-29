class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for c in s:
            if c.isalnum():
                clean+=c.lower()
        forward = 0
        backward = len(clean)-1
        while forward <= backward:
            if not clean[forward] == clean[backward]:
                return False
            forward+=1
            backward-=1
        return True


        