class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums2 = collections.deque(nums)
        while(k):
            popped = nums2.pop()
            nums2.appendleft(popped)
            k-=1
        i=0
        while nums2:
            nums[i] = nums2.popleft()
            i+=1