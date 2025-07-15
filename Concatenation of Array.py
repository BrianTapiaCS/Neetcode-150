# 1929. Concatenation of Array


''' 
Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]

'''

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums) # length of nums 
        helper = ['_'] * (2 * n) 

        for i in range(n):
            helper[i] = helper[i+n] = nums[i]

        return helper