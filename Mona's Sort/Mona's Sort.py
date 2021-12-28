def number_of_swaps(ar, swaps = 0):
    swapped = False
    for i in range(len(ar) - 1):
        if ar[i] > ar[i + 1]:
            swapped = True
            ar[i], ar[i + 1] = ar[i + 1], ar[i]
            swaps = 1 if swaps == 0 else swaps + 1
            
    return number_of_swaps(ar, swaps) if swapped else swaps
