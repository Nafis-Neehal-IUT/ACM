class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return bool(0)

        freq1 = Counter(s)
        freq1 = Counter(t)

        return Counter(s)==Counter(t)
