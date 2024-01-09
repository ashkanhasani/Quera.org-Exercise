def calculator(n, m, li):
    sum_n = 0
    sum_list = []
    for i in range(n):
        sum_n += li[i]
        if i % m == m - 1:
            sum_list.append(sum_n)
            sum_n = 0
        else:
            continue
        if sum_n != 0:
            sum_list.append(sum_n)
    return sum_list


print(calculator(8, 3, [1, 2, 3, 4, 5, 6, 7, 8]))
