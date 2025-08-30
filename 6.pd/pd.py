from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for num in range(1, n + 1):
            ans[num] = (ans[num >> 1] + num & 1)

        return ans


s = Solution()
print(s.countBits(5))