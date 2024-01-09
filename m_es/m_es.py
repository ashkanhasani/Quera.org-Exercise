def calculator(n, m, li):
    remind = n - (n % m)
    temporary = []
    list_of_list = []
    for i in range(n):
        if i % m == 0:
            list_of_list.append(sum(temporary))
            temporary = []
            temporary.append(li[i])
        else:
            temporary.append(li[i])
    list_of_list = list_of_list[1:]
    temporary = []
    for i in range(len(li) - 1, remind - 1, -1):
        temporary.append(li[i])
    list_of_list.append(sum(temporary))
    for j in range(len(list_of_list)):
        if j % 2 == 1:
            list_of_list[j] *= -1
    return sum(list_of_list)


print(calculator(8, 3, [1, 2, 3, 4, 5, 6, 7, 8]))