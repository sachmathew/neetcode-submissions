class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+=f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        strs = []
        str_index = -1
        length = ''
        index = 0
        while index < len(s):
            if(s[index] == '#'):
                index+=1
                strs.append("");
                str_index+=1
                start = index
                while index < start+int(length):
                    strs[str_index]+=s[index]
                    index+=1
                length = ''
            else:
                length += s[index]
                index+=1
        return strs

