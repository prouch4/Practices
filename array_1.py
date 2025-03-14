class Solution:
    def __init__(self, nums):
        self.nums = nums
    def removeDuplicates(self):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        k = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[k]: 
                k += 1  
                nums[k] = nums[i]  

            return k + 1


nums = list(input())
test = Solution(nums)
print(test.removeDuplicates())