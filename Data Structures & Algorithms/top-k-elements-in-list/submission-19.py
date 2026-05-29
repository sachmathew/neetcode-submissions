class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0)+1
        print(counts)
        freqs = [[] for n in range(len(nums)+1)]
        for n, f in counts.items():
            print(n, f)
            freqs[f].append(n)
            print(f, freqs[f])
        print(freqs)
        res = []
        for i in range(len(freqs)-1, 0, -1):
            for n in freqs[i]:
                print(n)
                res.append(n)
                if len(res) == k:
                    return res