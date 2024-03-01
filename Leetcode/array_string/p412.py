class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n+1): #range goes upto n-1
            if i%5==0 and i%3==0:
                answer.append("FizzBuzz")
            elif i%5==0 and not i%3==0:
                answer.append("Buzz")
            elif not i%5==0 and i%3==0:
                answer.append("Fizz")
            else:
                answer.append(str(i))
        return answer


        