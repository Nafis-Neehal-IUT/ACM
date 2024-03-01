def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        
        global_max = -1 
        
        while(left<right):

            y = min(height[left], height[right])
            x = abs(right-left)
            if y*x > global_max:
                global_max = y*x 
            
            if height[left] <= height[right]:
                left = left + 1
            elif height[right] < height[left]:
                right = right - 1 
        
        return(global_max)