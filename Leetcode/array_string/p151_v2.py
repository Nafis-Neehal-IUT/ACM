def reverseWords(self, s):
    
        stack = []
        start_word = 0
        end_word = 0
        in_word = 0
        i = 0
        while(i<len(s)):
            
            if i==len(s)-1 and in_word:
                stack.append(i)
                break
            
            if in_word==1 and s[i]==' ': #currently I'm in a word and encounter space at i-th
                end_word=i-1
                in_word=0
                stack.append(end_word)
                
            elif in_word==0 and s[i]!=' ': #currently I'm not in a word and encounter character at i-th
                start_word=i
                in_word=1
                stack.append(start_word)
                if i==len(s)-1:
                    stack.append(i)
                    break

            i = i+1 
        
        #got the stack
        string = ""
        i = len(stack)-1 
        
        while i > 0:
            start_idx = stack[i-1]
            end_idx = stack[i]+1
            word = s[start_idx:end_idx]
            if i>1: 
                string = string + word + " "
            else:
                string = string + word 
            i = i-2 
            
        return string