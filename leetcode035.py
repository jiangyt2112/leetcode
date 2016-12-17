class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index=0
        for i in nums:
            if(i==target):
                return index
            if(i>target):
                return index
            index+=1
        return index
def test():
    s=Solution()
    nums=[1,3,5,6]
    print(s.searchInsert(nums,0))
if __name__=="__main__":
    test()
