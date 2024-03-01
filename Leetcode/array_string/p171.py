class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphs = {}
        counter = 1
        for c in range(ord('A'), ord('Z')+1):
            alphs.update({chr(c):counter})
            counter +=1
        numsum = 0 #
        rev_i = 0
        for i in range(len(columnTitle)-1, -1, -1):
            n = (26**rev_i)*alphs[columnTitle[i]]
            numsum += n
            rev_i +=1
        return(numsum)