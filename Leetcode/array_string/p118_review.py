class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        main_list = []
        for i in range(numRows):
            rowval = []
            for j in range(i+1):
                rowval.append(factorial(i)//(factorial(j)*factorial(i-j)))
            main_list.append(rowval)
        return main_list
            
        