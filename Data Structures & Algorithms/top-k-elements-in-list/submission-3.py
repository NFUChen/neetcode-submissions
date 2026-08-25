class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = defaultdict(int)
        for number in nums:
            nums_dict[number]+=1
        # return sorted(nums_dict).keys()[:k]
        sorted_keys = sorted(nums_dict, key = nums_dict.get, reverse = True)
        return sorted_keys[:k]
