class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = Counter(nums)
        i=0
        for key in freq.keys():
            nums[i]=key
            i+=1
        return i