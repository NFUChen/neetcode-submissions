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
        for idx in range(len(count_arr) - 1, -1, -1):
            while len(count_arr[idx]) != 0:
                res.append(count_arr[idx].pop())
                if len(res) == k:
                    return res
            

        