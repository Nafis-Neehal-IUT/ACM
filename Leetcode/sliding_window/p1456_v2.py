from typing import List
from collections import Counter
#Version 1: Passed 102/106 test cases -> then ran into TLE
def getVowelCount(s: str) -> int:
    bigBatchSize = 10000
    if len(s) < bigBatchSize:
        charFreq = Counter(s)
        return (charFreq['a']+charFreq['e']+charFreq['i']+charFreq['o']+charFreq['u'])
    else:
        currentIndex = 0
        totalVowels = 0 
        while(currentIndex+bigBatchSize<=len(s)):
            charFreq = Counter(s[currentIndex:currentIndex+bigBatchSize])
            totalVowels = totalVowels + charFreq['a']+charFreq['e']+charFreq['i']+charFreq['o']+charFreq['u']
            currentIndex = currentIndex + bigBatchSize
        charFreq = Counter(s[currentIndex:])
        totalVowels = totalVowels + charFreq['a']+charFreq['e']+charFreq['i']+charFreq['o']+charFreq['u']
        return (totalVowels)

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        start = 0
        end = k 
        maxVowelCount = -1
        
        while(start<end):
            subString = s[start:end]
            vowelCount = getVowelCount(subString)
            if vowelCount > maxVowelCount:
                maxVowelCount = vowelCount
            start = start + 1
            end = end + 1 
            
            if end==len(s)+1:
                break 
        
        return(maxVowelCount)

#Version 2:
#Followed the hint

def maxVowels(self, s: str, k: int) -> int:
    start = 0
    end = k 
    vowels = "aeiou"
    currV = maxV = sum([1 for x in s[:k] if x in vowels])
    for i in range(0,len(s)-k):
        if s[i] in vowels:
            currV -=1 
        if s[i+k] in vowels:
            currV +=1 
        if currV>maxV:
            maxV = currV
    return(maxV)