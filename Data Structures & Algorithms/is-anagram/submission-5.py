class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mp = {}
        for ch in s:
            if ch in mp:
                mp[ch]+=1
            else:
                mp[ch] =1
        for ch in t:
            if ch in mp:
                mp[ch] -= 1
            else:
                return False
        for value in mp.values():
            if value != 0:
                return False
        return True

        