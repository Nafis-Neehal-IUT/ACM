from typing import List

#borrowed from anwendeng

def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for x in asteroids:
            surv = True
            if x > 0:
                st.append(x)
            else:
                while len(st) > 0:
                    y = st[-1]
                    if y < 0:
                        break
                    elif x + y == 0:
                        surv = False
                        st.pop()
                        break
                    elif x + y < 0:
                        st.pop()
                    else:
                        surv = False
                        break
                if surv:
                    st.append(x)
        return st



###################################### My Solution got stuck at 143/275 ##########
def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = []
    for elem in asteroids:
        collisionDestroyedRight = 0
        print(stack)
        if elem>0:
            stack.append(elem)
        if elem<0:
            if len(stack)==0:
                stack.append(elem)
                continue
            prevc = stack.pop()
            if prevc>0: #collision will happen: only if previous is positive and current is negative
                #both equal
                if abs(elem)==abs(prevc):
                    collisionDestroyedRight = 1 
                    continue
                elif abs(elem)<abs(prevc):
                    collisionDestroyedRight = 1
                    stack.append(prevc)
                else:
                    collisionDestroyedRight = 0
                    while(len(stack)!=0):
                        c = stack.pop()
                        if abs(c)>abs(elem):
                            stack.append(c)
                            collisionDestroyedRight = 1 
                            break
                        else:
                            collisionDestroyedRight = 0 
                            continue
                
            if collisionDestroyedRight==0:
                stack.append(elem)
    
    print(stack)
     
    
asteroidCollision(asteroids = [5,10,-5])
asteroidCollision(asteroids = [8,-8])
asteroidCollision(asteroids = [10,2,-5])
asteroidCollision(asteroids = [2,8,-8])
asteroidCollision(asteroids = [-5,-5,10])
asteroidCollision(asteroids = [-2,-1,1,2])

    # stack = [] #-5 -5 
    # initSign = -1 if asteroids[0]<0 else 1  #-1
    # for elem in asteroids: #-5 -5
    #     sameSign = bool((elem * initSign) > 0) #
    #     collisionDestroyedRight = 0
    #     if sameSign == 1:
    #         stack.append(elem)
    #     else:
    #         while(len(stack)>0):
    #             c = stack.pop()
    #             if abs(elem)==abs(c):
    #                 collisionDestroyedRight = 1
    #                 break 
    #             elif abs(elem)<abs(c):
    #                 stack.append(c)
    #                 collisionDestroyedRight = 1
    #                 break 
    #             else:
    #                 collisionDestroyedRight = 0
    #                 continue
    #         if(collisionDestroyedRight==0):
    #             stack.append(elem)
        
    # return (stack)
