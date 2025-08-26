class Solution:
    def maxNumber(self, nums1, nums2, k):
        m, n = len(nums1), len(nums2)
        best = []
        for i in range(max(0, k - n), min(k, m) + 1):
            a1 = pick_max(nums1, i)
            a2 = pick_max(nums2, k - i)
            cand = merge(a1, a2)
            if cand > best:
                best = cand
        return best


def pick_max(arr, t):
    """Monotonic decreasing stack: keep the best length-t subsequence."""
    drops = len(arr) - t
    st = []
    for x in arr:
        while drops and st and st[-1] < x:
            st.pop()
            drops -= 1
        st.append(x)
    return st[:t]


def merge(a, b):
    """Greedy merge by lexicographic suffix."""
    i = j = 0
    out = []
    while i < len(a) or j < len(b):
        if a[i:] > b[j:]:  # Python does lexicographic list compare
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    return out


s = Solution()
print(s.maxNumber(nums1=[3, 4, 6, 5], nums2=[9, 1, 2, 5, 8, 3], k=5))

