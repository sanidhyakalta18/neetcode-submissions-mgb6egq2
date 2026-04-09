class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_l = 0

        for x in num_set:
            if (x-1) not in num_set:
                current = x
                length = 1

                while (current+1) in num_set:
                    current +=1
                    length +=1
                
                max_l = max(max_l,length)
        return max_l
        