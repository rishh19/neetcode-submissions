class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need={}
        window={}

        for ch in s1:
            need[ch] = need.get(ch,0)+1

        l=0

        for h in range(len(s2)):
            window[s2[h]] = window.get(s2[h],0)+1

            if h-l+1 > len(s1):
                window[s2[l]] -= 1

                if window[s2[l]] == 0:
                    del window[s2[l]]
                l+=1

            if window==need:
                return True
        return False