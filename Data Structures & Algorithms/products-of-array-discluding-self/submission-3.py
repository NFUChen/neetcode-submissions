class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        # [1, 2, 4, 6] -> 
        # [1, 1, 2, 8]
        for idx in range(len(nums) - 1):
            curr_val = prefix[idx] * nums[idx]
            prefix.append(curr_val)
        rev_nums = nums[::-1]
        postfix = [1]
        for idx in range(len(rev_nums) -1):
            curr_val = postfix[idx] * rev_nums[idx]
            postfix.append(curr_val)

        res = []
        for pre, post in zip(prefix, postfix[::-1]):
            res.append(pre * post)

        return res