class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        freq = {}
        ans=0

        for h in range(len(s)):
            freq[s[h]] = freq.get(s[h],0)+1

            while freq[s[h]] > 1:
                freq[s[l]] -= 1

                if freq[s[l]] == 0:
                    del freq[s[l]]
                l+=1
            ans= max(ans,h-l+1)
        return ans