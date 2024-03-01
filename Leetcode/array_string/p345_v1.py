def reverseVowels(self, s):
    stack = []
    list_s = list(s)
    new_str = ""
    for i in range(len(list_s)):
        if list_s[i] in ['a','A','e','E','i','I','o','O','u','U']:
            stack.append(i)
            
    for i in range(len(list_s)):
        if list_s[i] in ['a','A','e','E','i','I','o','O','u','U']:
            new_str = new_str + list_s[stack.pop()]
        else:
            new_str = new_str + list_s[i]
    
    return(new_str)