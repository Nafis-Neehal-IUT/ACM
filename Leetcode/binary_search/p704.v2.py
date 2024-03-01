class Solution:
    idx = -1
    def search(self, nums: List[int], target: int) -> int:
        def bsearch(lst, left, right, target):
            if left>right:
                return
            mid = left + int((right-left)/2)
            if target == lst[mid]:
                self.idx = mid
                return
            elif target > lst[mid]:
                bsearch(lst, mid+1, right, target)
            elif target < lst[mid]:
                bsearch(lst, left, mid-1, target)
        
        #edge cases
        if not nums:
            return None
        if len(nums)==1:
            return (0 if nums[0]==target else -1)

        #generic cases
        left = 0
        right = len(nums)-1
        bsearch(nums, left, right, target)
        return self.idx
        
        