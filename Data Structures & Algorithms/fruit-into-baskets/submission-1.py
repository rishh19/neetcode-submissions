class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        freq={}
        ans=0

        for h in range(len(fruits)):
            freq[fruits[h]] = freq.get(fruits[h],0)+1

            while len(freq) > 2:
                freq[fruits[l]] -=1

                if freq[fruits[l]]==0:
                    del freq[fruits[l]]
                l+=1
            ans = max(ans,h-l+1)
        return ans
