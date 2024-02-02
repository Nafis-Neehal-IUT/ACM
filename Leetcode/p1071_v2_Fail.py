# My Solution - Got WA in TC 13 
def gcdOfStrings(self, str1, str2):
    
    common_window = min(len(str1), len(str2))
    common_string = ""
    
    #find the highest overlapping prefix
    for i in range(common_window): #O(n)
        if str1[i]==str2[i]:
            common_string = common_string + str1[i]
        else:
            break

    max_length = len(common_string)

    if max_length == 0:
        return ""
    
    #perform action in the larger string
    while(max_length>0):
        if len(str1) > len(str2):
            #search in str1 if max length happens again
            if str1[max_length:].count(common_string)>=1:
                #found max_string in str1 and break 
                return common_string
            else:
                #reduce string size
                common_string = common_string[:-1]
                max_length = max_length-1
        else:
            #search in str2 if max length happens again
            if str2[max_length:].count(common_string)>=1:
                #found max_string in str2 and break 
                return common_string
            else:
                #reduce string size 
                common_string = common_string[:-1]
                max_length = max_length-1 
    
    return ""

# Correct Solution
def gcdOfStrings(self, str1: str, str2: str) -> str:
    # Check if concatenated strings are equal or not, if not return ""
    if str1 + str2 != str2 + str1:
        return ""
    # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)
    from math import gcd
    return str1[:gcd(len(str1), len(str2))]