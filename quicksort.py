def quicksort(a):
    if(len(a) <= 1):
        return a
    
    small_arr = []
    big_arr = []

    pivot = a[len(a) - 1]

    for value in a:
        if value < pivot:
            small_arr.append(value)
        elif value > pivot:
            big_arr.append(value)

    print(small_arr, pivot)

    small_arr = quicksort(small_arr)
    big_arr = quicksort(big_arr)

    return small_arr + [pivot] + big_arr

l = [10, 9, 8, -1, -2, 4, 7, 6, 2]

l = quicksort(l)

print(l)