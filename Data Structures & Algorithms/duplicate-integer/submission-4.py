class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for num in nums:
            if num in hash:
                hash[num] = hash[num]+1
            else:
                hash[num] = 1
            if hash[num] > 1:
                return True
        return False