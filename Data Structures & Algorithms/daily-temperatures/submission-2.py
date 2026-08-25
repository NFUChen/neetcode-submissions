class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temps))]

        for i in range(len(temps)):
            while (len(stack) != 0 and temps[i] > temps[stack[-1]]):
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)


        return res