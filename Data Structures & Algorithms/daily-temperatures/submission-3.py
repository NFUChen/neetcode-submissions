class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temps))]

        for i in range(len(temps)):
            while (stack and temps[stack[-1]] < temps[i]):
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)

        
        return res