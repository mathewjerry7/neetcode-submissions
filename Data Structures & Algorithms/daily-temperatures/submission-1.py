class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [0]
        output = [0]*len(temperatures)

        for i in range(1,len(temperatures)):
            temp = temperatures[i]
            while stack and temperatures[stack[-1]]<temp:
                prev = stack.pop()
                output[prev] = i-prev #4
            stack.append(i)

        return output




'''
[0, 1, 2 , 3, 4, 5, 6]
[30,38,30,36,35,40,28]
[1, 4, 1, 0, 1, 0, 0]
stack = [5]


[1, 4, 1, 2, 1, 0, 0]

'''