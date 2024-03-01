def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        prefix_mult = [0]*len(nums)
        suffix_mult = [0]*len(nums)
        final_list  = [0]*len(nums)
        
        for i in range(len(nums)):
            if i>0: 
                prefix_mult[i] = prefix_mult[i-1] * nums[i]
            else:
                prefix_mult[i] = nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            if i<len(nums)-1: 
                suffix_mult[i] = suffix_mult[i+1] * nums[i]
            elif i==len(nums)-1:
                suffix_mult[i] = nums[i]
                
        for i in range(len(final_list)):
            if i==0: 
                final_list[i] = suffix_mult[i+1]
            elif i==len(final_list)-1:
                final_list[i] = prefix_mult[i-1]
            else:
                final_list[i] = prefix_mult[i-1] * suffix_mult[i+1]
    
        return (final_list)