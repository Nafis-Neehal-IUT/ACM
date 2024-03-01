class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        maxfreq = -1
        maxkey = -1
        for k in freq.keys():
            if freq[k] > maxfreq:
                maxfreq = freq[k]
                maxkey = k

        return maxkey