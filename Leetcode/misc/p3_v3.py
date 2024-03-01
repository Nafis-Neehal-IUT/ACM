def lengthOfLongestSubstring(self, s):
        strlen = len(s)
        offset = 0
        current_pointer = 0 #will run through the whole array sequentially
        current_string = ""
        max_len = 0
        
        if strlen==0:
            return 0
        
        while (current_pointer+offset) < strlen: 
            current_character = s[current_pointer+offset] #a 
            
            if (current_character in current_string): #if "a" in hashtable.keys()
                offset = 0
                current_pointer = current_pointer + 1
                current_string = ""
                continue
            
            else: #if "a" not in hashtable.keys()
                current_string = s[current_pointer: (current_pointer+offset)+1]
                if len(current_string) > max_len:
                    max_len = len(current_string)
                offset = offset + 1
        
        return max_len