class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)
        lens = len(s)-2
        req = 32-lens
        news = '0'*req + s[2:]
        flippeds = ''
        for i in range(len(news)-1, -1, -1):
            flippeds += news[i]
        return int(flippeds, 2)