class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0 for _ in range(len(temps))]
        stack = []

        for i in range(len(temps)):
            while (stack and temps[i] > temps[stack[-1]]):
                prev = stack.pop()
                res[prev] = i - prev

            stack.append(i)
        
        return res