'''
Issue with class variable initialization: was giving correct answer if run, but WA after submit.
Solve: initialize any class variables properly
'''

class Solution:

    def __init__(self):
        self.path = []
        self.flag = 0

    def isHappy(self, n: int) -> bool:
        if n == 1:
            return bool(1)

        def get_sum_squared(n):
            ns = str(n)
            sumlist = [int(i) ** 2 for i in ns]
            sumns = sum(sumlist)
            return sumns

        getsum = get_sum_squared(n)

        if getsum == 1:
            self.flag = 1
            return bool(1)

        if getsum in self.path:
            self.flag = 0
            return bool(0)

        else:
            self.path.append(getsum)
            return self.isHappy(getsum)
