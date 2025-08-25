def maxChunksToSorted(arr):
    st = []
    for x in arr:
        if not st or st[-1] <= x:
            st.append(x)
        else:
            mx = st.pop()
            while st and st[-1] > x:
                st.pop()
            st.append(mx)
    return len(st)


print(maxChunksToSorted([1, 3, 5, 4, 2]))
