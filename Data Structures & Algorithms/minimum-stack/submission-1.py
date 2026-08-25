class MinStack:

    def __init__(self):
        self.stack = []
        self._min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self._min) == 0:
            self._min.append(val)
        else:
            curr_min = min(self._min[-1], val)
            self._min.append(curr_min)

    def pop(self) -> None:
        self.stack.pop()
        self._min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self._min[-1]
