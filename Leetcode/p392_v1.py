def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)==0:
            return bool(1)

        char = 0 
        for i in range(len(t)):
            if s[char] == t[i]:
                char = char + 1
            if char==len(s):
                return bool(1)
        return bool(0)