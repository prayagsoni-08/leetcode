class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
       if len(nums) ==0:
        return 0
       if len(nums) ==1:
        return nums[0]**2
       else:
        s=0
        for i in range(1,len(nums)+1):
            if len(nums)%i ==0:
                s=s + ((nums[i-1])**2)
        return s