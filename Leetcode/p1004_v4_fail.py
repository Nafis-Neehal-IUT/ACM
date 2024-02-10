#tried and got stuck in several solutions
#borrowed from deleted_user 
def longestOnes(self, nums: List[int], k: int) -> int:
    l=r=0    
    for r in range(len(nums)):
        if nums[r] == 0:
            k-=1
        if k<0: # all k zeroes have been already found can't add more zero 
            if nums[l] == 0:
                k+=1
            l+=1
    return (r-l+1)