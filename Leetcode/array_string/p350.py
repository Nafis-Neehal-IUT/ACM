class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        #You can use collections.Counter for this, which will provide the lowest count found in either list for each element when you take the intersection.
        c = list((Counter(nums1) & Counter(nums2)).elements())
        return c

        
        