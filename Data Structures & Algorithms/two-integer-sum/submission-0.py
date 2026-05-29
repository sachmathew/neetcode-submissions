class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            difference = target-nums[i]
            if difference in hash:
                return [hash[difference], i]
            else:
                hash[nums[i]]=i