from math import floor

def binarySearch (s: list, value: float) -> int:
    l = 0
    r = len(s)-1

    while(l<=r):
        middle = floor((l + r)/2)
        if s[middle] == value:
            return middle
        elif s[middle] < value:
            l = middle + 1
        else:
            r = middle - 1
    
    return -1

testL = [0, 10, 20, 30, 40, 50]
testV = 50
print(binarySearch(testL, testV))