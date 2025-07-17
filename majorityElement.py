class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        c = 0
        r = nums[0]

        for n in nums:
            if n == r:
                c += 1
            else: 
                c -= 1
            if c == 0:
                r = n
                c = 1
        return r

