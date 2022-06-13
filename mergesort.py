def mergesort(a):
    if(len(a) <= 1):
        return

    #recursion
    middle = (len(a))//2
    leftArr = a[:middle]
    rightArr = a[middle:]

    mergesort(leftArr)
    mergesort(rightArr)

    #merge
    lIndex = 0
    rIndex = 0
    aIndex = 0

    while (lIndex < len(leftArr) and rIndex < len(rightArr)):
        if (leftArr[lIndex] <= rightArr[rIndex]):
            a[aIndex] = leftArr[lIndex]
            lIndex += 1
        else:
            a[aIndex] = rightArr[rIndex]
            rIndex += 1
        aIndex += 1
    
    while (lIndex < len(leftArr)):
        a[aIndex] = leftArr[lIndex]
        lIndex += 1
        aIndex += 1

    while (rIndex < len(rightArr)):
        a[aIndex] = rightArr[rIndex]
        rIndex += 1
        aIndex += 1

l = [10, 10, 8, 6, 9, 16, 1, 2, 1]
# l = []
# l = [1]
# l = [12, 10, 10, 9]

mergesort(l)

print(l)