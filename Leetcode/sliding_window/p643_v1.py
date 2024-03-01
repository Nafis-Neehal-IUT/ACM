def findMaxAverage(self, nums: List[int], k: int) -> float:
    currSum = maxSum = sum(nums[:k])
    
    for i in range(0, len(nums)-k):
        currSum = currSum - nums[i]
        currSum = currSum + nums[i+k]
        if currSum>maxSum:
            maxSum=currSum
    
    return(maxSum/k)