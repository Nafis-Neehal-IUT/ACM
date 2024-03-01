class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        if n==1:
            self.memo.update({'1':1})
            return 1
        elif n==2:
            self.memo.update({'2':2})
            return 2
        
        if str(n) not in self.memo.keys():
            self.memo.update({str(n): self.climbStairs(n-1) + self.climbStairs(n-2)})

        return self.memo[str(n)]
        

        