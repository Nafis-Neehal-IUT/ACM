class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        freqvals = list(freq.values())
        if sum(freqvals)>len(freqvals):
            return bool(1)
        else:
            return bool(0)
        