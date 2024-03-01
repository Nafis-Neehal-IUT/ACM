class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for k in freq.keys():
            if freq[k]==1:
                return k
    