def separator(ls):
    ls_even = [i for i in ls if i % 2 == 0]
    ls_odd = [j for j in ls if j % 2 == 1]
    result = (ls_even, ls_odd)
    return result
