class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return bool(0)
        return (log10(n)/log10(3)) % 1 == 0
