class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_e = nums[0]
        res = nums[0]

        for i in range(1,len(nums)):
            max_e = max(max_e + nums[i], nums[i])
            res = max(max_e, res)
        return res
        