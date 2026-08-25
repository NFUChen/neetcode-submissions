class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]
        # [1, 2, 4, 6]
        # [1, 1, 2, 8]
        for idx in range(1, len(nums)):
            current_num = nums[idx - 1] * prefix[idx - 1]
            prefix.append(current_num)

        # [6, 4, 2, 1]
        # [1, 6, 24, 48]
        _rev = nums[::-1]
        for idx in range(1, len(nums)):
            curr = _rev[idx - 1] * postfix[idx - 1]
            postfix.append(curr)
        res = []
        for pre, post in zip(prefix, postfix[::-1]):
            res.append(pre * post)
        
        return res


        #[1, 1, 2,8]
        #[48, 24, 6, 1]
        # [48, 24, 12, 8]

