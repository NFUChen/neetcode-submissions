class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_arr = [[] for _ in range(len(nums))]
        count_map = {}
        for num in nums:
            if num not in count_map:
                count_map[num] = 0
            count_map[num] += 1
        
        for num, count in count_map.items():
            count_arr[count - 1].append(num)
        
        res = []

        for left in range(len(nums) -1, -1, -1):
            while (len(count_arr[left]) != 0):
                curr_value = count_arr[left].pop()
                res.append(curr_value)
                if len(res) == k:
                    return res