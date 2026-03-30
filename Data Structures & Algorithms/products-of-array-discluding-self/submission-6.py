class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        Prefix = 1
        for i in range (n):
            res[i] = Prefix
            Prefix *= nums[i]
        Suffix = 1
        for i in range(n-1,-1,-1):
            res[i] *= Suffix
            Suffix *= nums[i]
        
        return res
