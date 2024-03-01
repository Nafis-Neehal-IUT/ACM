class Solution:
    def hammingWeight(self, n: int) -> int:
        bina = bin(n)[2:]
        sums = [1 for c in bina if c=='1']
        return (sum(sums))