class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        freq={}
        ans=0
        maxF=0

        for h in range(len(s)):
            freq[s[h]] = freq.get(s[h],0)+1

            maxF = max(maxF,freq[s[h]])

            while (h-l+1)-maxF > k:
                freq[s[l]] -=1
                l+=1
            ans=max(ans,h-l+1)
        return ans