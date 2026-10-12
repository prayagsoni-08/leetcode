class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        a=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[a-1]:
                nums[a]=nums[i]
                a+=1
        return a