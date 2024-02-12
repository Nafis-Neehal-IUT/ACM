def removeStars(self, s: str) -> str:
    stack = []
    for c in list(s):
        if c=='*':
            stack.pop()
        else:
            stack.append(c)

    s = ''.join([str(elem) for elem in stack])
            
    return(s)