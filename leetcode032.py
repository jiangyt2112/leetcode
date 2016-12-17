class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length=0
        l=list(s)
        length=len(s)
        mapper=[]
        for i in range(length):
            mapper.append(i)
        i=0
        while(i<len(l)):
            if(l[i]==')' and i>0 and l[i-1]=='('):
                l.pop(i)
                l.pop(i-1)
                mapper.pop(i)
                mapper.pop(i-1)
                i=i-1
            else:
                i=i+1
        i=0
        j=1
        mapper=[-1]+mapper+[length]
        ll=len(mapper)
        while(j<ll):
            temp=mapper[j]-mapper[i]
            if(temp>max_length):
                max_length=temp
            i+=1
            j+=1    
        return max_length-1
def test():
    s=Solution()
    print(s.longestValidParentheses("()"))
if __name__=='__main__':
    test()
                
