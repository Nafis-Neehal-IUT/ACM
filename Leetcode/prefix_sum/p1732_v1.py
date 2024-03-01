from typing import List 
def largestAltitude(self, gain: List[int]) -> int:
    maxAlt = 0
    currAlt = 0  
    for i in range(len(gain)):
        currGain = gain[i]
        currAlt = currAlt + currGain
        if currAlt > maxAlt:
            maxAlt = currAlt 
    return maxAlt