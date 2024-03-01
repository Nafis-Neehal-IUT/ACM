class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        pairs = [['(',')'], ['{','}'], ['[',']']]
        if n%2==1:
            return bool(0)
        stack = []
        for p in s:
            if p in ['(', '{', "["]:
                stack.append(p)
            elif p in [')', '}', "]"]:
                if stack:
                    popped = stack.pop() #possibly pop out an opening pair
                    if [popped, p] not in pairs:
                        return bool(0)
                else:
                    return bool(0)
        if not stack:
            return bool(1)

        