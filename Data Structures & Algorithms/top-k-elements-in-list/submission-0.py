class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp = {}

        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1

        sorted_items = sorted(mp.items(), key=lambda x: x[1], reverse=True)

        ans = []

        for i in range(k):
            ans.append(sorted_items[i][0])

        return ans