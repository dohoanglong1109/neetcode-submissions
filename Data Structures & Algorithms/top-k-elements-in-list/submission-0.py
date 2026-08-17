class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            if n not in freq:
                freq[n] = 1

        result = sorted(freq, key=freq.get, reverse=True)
        return result[0:k]