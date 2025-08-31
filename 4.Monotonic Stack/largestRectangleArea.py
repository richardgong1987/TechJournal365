class Solution:
    def maxNumber(self, nums1, nums2, k):
        n = len(nums1)
        m = len(nums2)

        better_choice = []

        for i in range(max(0, k - n), min(k, m)):
            result1 = get_monotonic_array(nums1, k - i)
            result2 = get_monotonic_array(nums2, i)
            merged_arr = merge(result1, result2)
            if merged_arr > better_choice:
                better_choice = merged_arr

        return better_choice

def merge(arr1, arr2):
    out = []
    left = right = 0
    while left < len(arr1) or right < len(arr2):
        if arr1[left:] > arr2[right:]:
            out.append(arr1[left])
            left += 1
        else:
            out.append(arr2[right])
            right += 1
    return out


def get_monotonic_array(arr, take):
    should_drops = len(arr) - take
    stack = []
    for v in arr:
        while should_drops and stack and stack[-1] < v:
            stack.pop()
            should_drops -= 1

        stack.append(v)

    return stack[:take]


s = Solution()
print(s.maxNumber(nums1=[6,7], nums2=[6,0,4], k=5))
