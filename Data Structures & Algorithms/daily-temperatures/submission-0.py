class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temps)
        for idx in range(len(temps)):
            curr_temp = temps[idx]
            while (stack and curr_temp > temps[stack[-1]]):
                prev = stack.pop()
                res[prev] = idx - prev
            stack.append(idx)


        
        return res
