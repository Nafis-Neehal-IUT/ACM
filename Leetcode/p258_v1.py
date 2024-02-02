def addDigits(self, num: int) -> int:
        strnum = str(num)
        while(len(strnum)!=1):
            print(strnum)
            num = 0
            for i in range(len(strnum)):
                num = num + int(strnum[i])
            strnum = str(num)
        return(int(strnum))