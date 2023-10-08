def min_size_board(leaf_num, width, height):
    if leaf_num not in range(1, 1012):
        return -1, -1

    if width not in range(1, 109):
        return -1, -1

    if height not in range(1, 109):
        return -1, -1

    left = max(width, height)
    right = left * leaf_num
    while left < right:
        mid = (left + right) // 2
        if (mid // width) * (mid // height) >= leaf_num:
            right = mid
        else:
            left = mid + 1
    return left
