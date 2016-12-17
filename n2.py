class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n>10):
            n=10
        if(n==0):
            return 1
        m=n
        n=n-1
        temp=9
        loop=9
        while(n>0):
            temp=temp*loop
            n=n-1
            loop=loop-1
        return temp+self.countNumbersWithUniqueDigits(m-1)
def test():
    n=input("输入n:")
    n=int(n)
    s=Solution()
    count=s.countNumbersWithUniqueDigits(n)
    print(count)
if(__name__=="__main__"):
    while(True):
        test()
        
            
