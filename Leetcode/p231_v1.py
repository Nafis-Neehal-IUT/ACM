rom math import log2
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0: 
            return bool(0)
        power = log2(n)
        if power == int(power):
           return bool(1)
        else:
            return bool(0) 
        