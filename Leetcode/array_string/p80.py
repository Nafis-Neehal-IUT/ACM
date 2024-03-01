class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        index = 0
        k = 0
        for key in freq.keys():
            repeat = (2 if freq[key]>2 else freq[key])
            k = k + repeat
            while(repeat):
                nums[index] = key
                index +=1
                repeat -=1
        return k