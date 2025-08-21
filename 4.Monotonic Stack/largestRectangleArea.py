def largestRectangleArea(heights):
    stack = []  # indices, heights are strictly increasing
    max_area = 0
    arr = heights + [0]  # sentinel to flush

    for i, h in enumerate(arr):
        while stack and arr[stack[-1]] > h:
            top = stack.pop()
            height = arr[top]
            left_smaller = stack[-1] if stack else -1
            width = i - left_smaller - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area


print(largestRectangleArea([3, 2, 1, 1, 1]))
