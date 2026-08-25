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

        # Step 2: Find the longest alternating sequence in sym
        # Loop through sym and:
        # If current symbol is "=", reset.
        # If current symbol is different from the previous one, it's alternating → increase length.
        # If it's the same as previous (like > followed by >), reset to 2 (this symbol and the one before it).
        # Why 2 ? A: Even though sym has only 1 item, [2, 4] is a valid turbulent subarray of length 2.


        max_len = 1  # at least one element
        curr_len = 1
        for i in range(len(sym)):
           
            if sym[i] == "=":
                curr_len = 1 
            elif i == 0:
                curr_len = 2
            elif sym[i] != sym[i - 1]:
                curr_len += 1
            else: # cases not alternating.
                curr_len = 2  # start new sequence from this point
            max_len = max(max_len, curr_len)

        return max_len
