class Solution(object):
    def __init__(self, nums):
        self.nums = nums

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        finalNums = []
        for num in nums:
            if num in finalNums:
                finalNums.append("_")
            else:
                finalNums.append(num)
        finalNums.sort(key=lambda x: (x == '_', x))

        k = 0

        for i in range(1, len(finalNums)):
           if finalNums[i] != finalNums[k]: 
               k += 1  
               finalNums[k] = finalNums[i] 
        return k, finalNums

nums = list(map(int, input("Lista: ").split(",")))
test = Solution(nums)

k = test.removeDuplicates(nums)
print("Respuesta: ",k)