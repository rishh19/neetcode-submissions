from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return Counter(s) == Counter(t)

        #check length
        if len(s) != len(t):
            return False
        mp={}

        #fill map
        for ch in s:
            mp[ch] = mp.get(ch,0)+1

        #check t for s presence
        for ch in t:
            if ch not in mp:
                return False
            else: 
                #reduce ch one by one
                mp[ch]-=1

            if mp[ch] < 0:
                return False
        return True