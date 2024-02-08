#v2
def compress(self, chars):
        i=0
        end=0
        chars_list = []
        while(i<=len(chars)-1):
            while (end<=len(chars)-1 and chars[end]==chars[i]):
                end = end + 1
            #if loop didn't run once
            if (end-1)==i:
                chars_list.append(chars[i])
            else: #if loop did run couple of times but didn't go at list end 
                chars_list.append(chars[i])
                freq = list(str(end-i))
                chars_list.extend(freq)
            if(end>len(chars)-1):
                break 
            i=end
        
        for i in range(len(chars_list)):
            chars[i] = chars_list[i]
        
        return(len(chars_list))