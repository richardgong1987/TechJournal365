def counting_sort(arr, exp):
    """
    按照当前位（exp）进行一次稳定的计数排序
    exp: 1 表示个位，10 表示十位，100 表示百位...
    """
    n = len(arr)
    output = [0] * n  # 存放排序结果
    count = [0] * 10  # 计数数组（0-9）

    # 统计当前位的数字出现次数
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # 将 count 转换为位置索引（累加）
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 从后往前遍历，保持稳定性
    for i in range(n):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # 把排序结果复制回原数组
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    # 找到最大值，确定位数
    max_num = max(arr)

    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


# 示例
data = [170, 45, 75]
print("原数组:", data)
radix_sort(data)
print("排序后:", data)
