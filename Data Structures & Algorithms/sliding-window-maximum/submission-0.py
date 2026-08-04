from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = deque()
        ans = []
        low = 0

        for high in range(len(nums)):

            # 1. Remove smaller elements from BACK
            while dq and nums[dq[-1]] < nums[high]:
                dq.pop()

            # 2. Add current index
            dq.append(high)

            # 3. Remove FRONT if it is outside current window
            if dq[0] < low:
                dq.popleft()

            # 4. Complete window of size k
            if high - low + 1 == k:

                # FRONT always represents maximum
                ans.append(nums[dq[0]])

                # Slide the window
                low += 1

        return ans