from typing import List
from collections import Counter 
def maxOperations(self, nums: List[int], k: int) -> int:
    reverseNums = [k-x for x in nums] 
    pairCounter = 0
    frequencyNumsCopy = Counter(nums)
    frequencyNums = {key:value for key,value in frequencyNumsCopy.items() if key<k}
    
    for revNum in reverseNums:
        if revNum<=0:
            continue
            
        if (revNum in frequencyNums.keys()):
            if (revNum==k-revNum) and (0<frequencyNums.get(revNum)<2):
                continue
            elif (frequencyNums.get(revNum)>0) and (frequencyNums.get(k-revNum)>0):
                pairCounter = pairCounter + 1
                frequencyNums[revNum] = frequencyNums[revNum] - 1 
                frequencyNums[k-revNum] = frequencyNums[k-revNum] - 1 
    
    return (pairCounter)