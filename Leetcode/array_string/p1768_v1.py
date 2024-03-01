def mergeAlternately(self, word1, word2):
    
        common_merge_window = min(len(word1), len(word2))
        
        new_string = ""
        
        for i in range(common_merge_window):
            new_string = new_string + word1[i]
            new_string = new_string + word2[i]
        
        if (len(word1)>len(word2)):
            new_string = new_string + word1[common_merge_window:]
        else:
            new_string = new_string + word2[common_merge_window:]
            
        return new_string