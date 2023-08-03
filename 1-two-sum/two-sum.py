class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
           for k in range(len(nums)):
               sum = nums[i] + nums[k]
               if sum == target and i != k:
                   print(i, k)
                   return [i, k]
       





              
