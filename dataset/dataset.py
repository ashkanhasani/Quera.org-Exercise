nq = input().split(" ")
data_dict = {}
data_check = []
for i in range(int(nq[0])):
    j = input().split(" ")
    data_dict.update({j[0]: j[1]})
for i in range(int(nq[1])):
    j = input()
    if j in data_dict.keys():
        data_check.append(data_dict[j])
    else:
        data_check.append("unknown")
print(*data_check, sep="\n")
