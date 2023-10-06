arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]


def diagonalDifference(arr):
    n = len(arr)
    l_t_r = r_t_l = 0
    for i in range(0, n):
        j = n - 1 - i
        l_t_r += arr[i][i]
        r_t_l += arr[i][j]

    return abs(l_t_r - r_t_l)


resp = diagonalDifference(arr)
print(resp)
