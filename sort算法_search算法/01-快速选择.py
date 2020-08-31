def quickSelect(nums, begin, end, n):
    t = nums[end-1]
    # i:下一个待交换的元素 j:遍历数组的指针
    i = j = begin
    # 遍历数组
    while j < end:
        # 对于比基准值小的数,就放到左边
        if nums[j] <= t:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1

    # 如果交换好的元素的长度,大于要查找的元素应该在的位置
    # 那么必定在左边
    if i-1 > n:
        quickSelect(nums, begin, i-1, n)
    # 否则在右边
    elif i <= n:
        quickSelect(nums, i, end, n)


if __name__ == "__main__":
    test = [5, 4, 3, 2]
    quickSelect(test, 0, len(test), 2)
    print(test[2])
