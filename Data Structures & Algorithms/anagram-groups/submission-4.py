class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            letter_frequency = [0]*26
            for c in s:
                letter_frequency[ord(c)-ord('a')] += 1
            res[tuple(letter_frequency)].append(s)
        return list(res.values())
            
        
        