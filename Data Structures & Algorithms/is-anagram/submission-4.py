class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = {}
        for c in s:
            if c in s_letters:
                s_letters[c] += 1
            else:
                s_letters[c] = 1

        t_letters = {}
        for c in t:
            if c in t_letters:
                t_letters[c] += 1
            else:
                t_letters[c] = 1
        
        for letter in s_letters:
            if (not letter in t_letters) or (t_letters[letter] != s_letters[letter]):
                return False
        
        for letter in t_letters:
            if (not letter in s_letters) or (s_letters[letter] != t_letters[letter]):
                return False
        
        return True
            
        