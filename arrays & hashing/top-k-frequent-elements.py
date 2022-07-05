class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int) # map nums to their count
        
        for num in nums:
            count[num] += 1
        
        lst = [(key, freq) for key, freq in count.items()]
        lst.sort(key=lambda numAndFreq: numAndFreq[1], reverse=True)
        
        res = list(map(lambda numAndFreq: numAndFreq[0], lst))

        return res[0:k]
        
            