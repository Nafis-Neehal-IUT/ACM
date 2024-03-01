class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(str(c) for c in digits))+1
        str_num = str(num)
        return([int(c) for c in list(str_num)])
        