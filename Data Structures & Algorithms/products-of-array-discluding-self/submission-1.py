class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]

        # [1, 2 ,4 ,6]
        # [1, 1, 2, 8]
        for idx in range(1, len(nums)):
            curr = nums[idx - 1] * prefix[idx - 1]
            prefix.append(curr)
       



        _reversed = nums[::-1]
        for idx in range(1, len(_reversed)):
            curr = _reversed[idx - 1] * postfix[idx - 1]
            postfix.append(curr)
        res = []
        for pre, post in zip(prefix, postfix[::-1]):
            res.append(pre * post)
        return res

        # 
        # [1, 2 4, 6]
        # [48 ,24 ,6 ,1]