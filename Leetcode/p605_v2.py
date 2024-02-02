class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if n==0:
            return bool(1)
            
        if len(flowerbed)==0:
            return bool(0)
            
        if len(flowerbed)==1:
            if flowerbed[0]==0 and (n==1 or n==0):
                return bool(1)
            else:
                return bool(0)
            
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                #add two border cases
                if(i==0):
                    if(flowerbed[i+1]==1): #has neighbor
                        i = i+1
                        continue
                    else:
                        flowerbed[i] = 1
                        n = n-1
                        if (n==0):
                            return(bool(1))
                        i = i+1
                    
                elif(i==len(flowerbed)-1):
                    if(flowerbed[i-1]==1): #has neighbor
                        i = i+1
                        continue
                    else:
                        flowerbed[i] = 1
                        n = n-1
                        if (n==0):
                            return(bool(1))
                        i = i+1
                
                #add middle cases
                else: 
                    if (flowerbed[i-1] == 1) or (flowerbed[i+1] == 1): #there is valid neighbor with 1
                        i = i+1
                        continue 
                    else:
                        flowerbed[i] = 1
                        n = n-1
                        if (n==0):
                            return(bool(1))
                        i = i+1
                    
        return(bool(0))