class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = collections.Counter(s)
        keylist = [key for key in list(freq.keys()) if freq[key]==1]
        if len(keylist)==0:
            return -1
        return s.index(keylist[0])