
def moveZeroes(self, nums):
    current_zero = 0
    next_digit_after_current_zero = 0
    
    #edge cases - length 1 
    if len(nums)==1:
        return nums
        
    if len(nums)==2:
        if nums[0]==0 and nums[1]!=0:
            vtemp = nums[1]
            nums[1] = 0
            nums[0] = vtemp
            return nums
        else:
            return nums
    
    for i in range(len(nums)):
        if nums[i]==0:
            current_zero = i
            next_digit_after_current_zero = i
            
            while(next_digit_after_current_zero < len(nums)-1 and nums[next_digit_after_current_zero]==0):
                next_digit_after_current_zero = next_digit_after_current_zero + 1
            
            if (next_digit_after_current_zero == len(nums)-1) and (nums[next_digit_after_current_zero]==0): #there are no digits after current zero 
                return nums 
                
            #if loop breaks and reaches here, that means there is a digit after current zero 
            #now swap and increase current_zero pointer by 1
            temp_v = nums[next_digit_after_current_zero]
            nums[next_digit_after_current_zero] = 0
            nums[current_zero] = temp_v
            
    return nums