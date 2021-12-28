def recur_add(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + recur_add(lst[1:]) if len(lst) != 1 else lst[0]
