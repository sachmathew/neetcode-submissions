class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = {}
        for n in nums:
            h[n] = 1
        
        h2 = {}
        current_n = None
        previous = None
        for n in h:
            print(n)
            if not n-1 in h:
                print("new start")
                sequence = 1
                while n+sequence in h:
                    sequence+=1
                h2[n] = sequence
        
        max = 0
        for n in h2:
            if h2[n] > max:
                max = h2[n]
        return max
            
        