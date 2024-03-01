#1. Write a Python program to calculate the sum of a list of numbers using recursion. 
def getSum(lst, ssum=0, i=0):
  if i == len(lst)-1:
    return ssum
  else:
    return getSum(lst, ssum=ssum+lst[i], i=i+1)

lst = [1,2,3,4,5,6]
result = getSum(lst,0,0)
print(result)

#2. Write a Python program to get the sum of a non-negative integer using recursion.
def getNumSum(num):
  if num < 10:
    return num
  else:
    numList = list(str(num)) #['1', '2', '3']
    return getNumSum(sum([int(x) for x in numList]))
    
result = getNumSum(12345)
print(result)