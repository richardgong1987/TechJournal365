from typing import List


def next_greater(nums):
    result = [-1] * len(nums)
    stack = []  # stores indices

    for i, num in enumerate(nums):
        while stack and num > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = num
        stack.append(i)
    return result


print(next_greater([1, 3, 4, 2]))


# 4,5,-1


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result_map = {}

        for num2 in nums2:
            while stack and num2 > stack[-1]:
                cur = stack.pop()
                result_map[cur] = num2

            stack.append(num2)

        return [result_map.get(num1, -1) for num1 in nums1]

s = Solution()
print(s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
