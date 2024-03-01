class Solution:
    def mySqrt(self, x: int) -> int:
        num = 1
        while (num*num)<=x:
            num +=1
        return num-1

class Solution:
    def mySqrt(self, x: int) -> int:
        left,right=1,x
        while left<=right:
            mid=(left+right)//2
            if mid*mid==x:
                return mid
            if mid*mid>x:
                right=mid-1
            else:
                left=mid+1
        return right