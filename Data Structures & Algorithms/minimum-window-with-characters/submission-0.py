class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        need = {}
        window = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        have = 0
        needCount = len(need)

        low = 0
        start = 0
        minLen = float("inf")

        for high in range(len(s)):

            window[s[high]] = window.get(s[high], 0) + 1

            if s[high] in need and window[s[high]] == need[s[high]]:
                have += 1

            while have == needCount:

                if high - low + 1 < minLen:
                    minLen = high - low + 1
                    start = low

                window[s[low]] -= 1

                if s[low] in need and window[s[low]] < need[s[low]]:
                    have -= 1

                low += 1

        if minLen == float("inf"):
            return ""

        return s[start:start + minLen]