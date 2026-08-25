class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        
        sym = []
        for i in range(1, len(arr)):
            before = arr[i - 1]
            curr = arr[i]
            print(before, curr)
            if before > curr:
                sym.append(">")
            elif before < curr:
                sym.append("<")
            else:
                sym.append("=")
            
        print(sym)

        # Step 2: Find the longest alternating sequence in sym
        max_len = 1  # at least one element
        curr_len = 1

        for i in range(len(sym)):
            if sym[i] == "=":
                curr_len = 1
            elif i == 0:
                curr_len = 2
            elif sym[i] != sym[i - 1]:
                curr_len += 1
            else:
                curr_len = 2  # start new sequence from this point

            max_len = max(max_len, curr_len)


        return max_len
