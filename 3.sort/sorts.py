def largestRectangleArea(heights):
    stack = []  # will store indices with increasing heights
    max_area = 0
    # Append a sentinel 0 height to flush the stack at the end
    for i, h in enumerate(heights + [0]):
        # If current bar is lower, resolve rectangles with taller bars
        while stack and heights[stack[-1]] > h:
            top = stack.pop()
            height = heights[top]
            left_smaller_idx = stack[-1] if stack else -1
            width = i - left_smaller_idx - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area


print(largestRectangleArea([2,2,2,2]))