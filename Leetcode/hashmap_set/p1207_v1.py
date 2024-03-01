from typing import List
from collections import Counter 
def uniqueOccurrences(self, arr: List[int]) -> bool:
        freqDict = Counter(arr)
        val = freqDict.values()
        if len(val)==len(set(val)): #all values are unique
            return bool(1)
        else:
            return bool(0)