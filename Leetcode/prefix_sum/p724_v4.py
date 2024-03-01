from typing import List
def pivotIndex(self, nums: List[int]) -> int:
        
        #borrowed because trying to reduce runtime 
        total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]
        return -1

        #below three are my solutions

        # leftSum = []
        # rightSum = []
        # arraySum = sum(nums)

        # for i in range(len(nums)):
        #     if i==0:
        #         leftSum.append(0)
        #         rightSum.append(arraySum - nums[i])
        #     elif i==len(nums)-1:
        #         rightSum.append(0)
        #         leftSum.append(arraySum-nums[i])
        #     else:
        #         leftSum.append(sum(nums[:i]))
        #         rightSum.append(sum(nums[i+1:]))
        
        # for i in range(len(leftSum)):
        #     if leftSum[i]==rightSum[i]:
        #         return i 
        # return -1 
                

        # for i in range(len(nums)):
        #     if i==0 and arraySum - nums[i]==0:
        #         return 0
        #     elif i==len(nums)-1 and arraySum - nums[i]==0:
        #         return i
        #     else:
        #         if (arraySum-nums[i])/2 == sum(nums[:i]):
        #             return i
        # return -1

        

        # for i in range(len(nums)):
        #     if i==0:
        #         leftSum = 0
        #         rightSum = sum(nums[i+1:]) 
        #     elif i==len(nums)-1:
        #         leftSum = sum(nums[:i])
        #         rightSum = 0
        #     else:
        #         leftSum = sum(nums[:i])
        #         rightSum = sum(nums[i+1:])  
        #     if leftSum==rightSum:
        #         return i
        # return -1 