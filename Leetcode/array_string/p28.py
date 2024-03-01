class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            idx = haystack.index(needle)
            return idx
        except:
            return -1
        else:
            pass
        finally:
            pass
        