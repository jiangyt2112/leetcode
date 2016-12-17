class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length=len(nums)
        for i in range(length):
            if(nums[i]==target):
                return i
        return -1
