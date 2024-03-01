from typing import List
def longestSubarray(self,nums: List[int]) -> int: 
    l=r=0
    z = 1
    for r in range(len(nums)):
        if nums[r]==0:
            z-=1
        if z<=-1:
            if nums[l]==0:
                z+=1 
            l+=1
    if r==l:
        return 0
    return(r-l)