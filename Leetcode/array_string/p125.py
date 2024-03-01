class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1="".join(c for c in s if c.isalnum())
        news = s1.lower()

        print(news)
        if len(news) in [0,1]:
            return bool(1)

        length = len(news)
        mid = (length//2)
        left = news[:mid]
        if length%2==1:
            right = news[mid+1:]
        else:
            right = news[mid:]
        print(left, right)
        return left==right[::-1]
        