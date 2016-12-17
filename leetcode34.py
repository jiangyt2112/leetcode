class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length=len(nums)
        start=0
        end=length-1
        hit=-1
        while(start<=end):
            mid=(start+end)//2
            if(nums[mid]==target):
                hit=mid
                break
            if(nums[mid]<target):
                start=mid+1
            else:
                end=mid-1
        if(hit==-1):
            return [-1,-1]
        else:
            left=hit
            right=hit
            while(left>=0 and nums[left]==target):
                left-=1
            if(left<0):
                left=0
            else:
                left+=1
            while(right<length and nums[right]==target):
                right+=1
            if(right==length):
                right=length-1
            else:
                right-=1
        return [left,right]
def test():
    s=Solution()
    nums=[]
    print(s.searchRange(nums,3))
if __name__=="__main__":
    test()
