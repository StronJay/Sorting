test = [
    -19,
    759,
    168,
    306,
    270,
    -602,
    558,
    -821,
    -599,
    328,
    753,
    -50,
    -568,
    268,
    -92,
    381,
    -96,
    730,
    629,
    678,
    -837,
    351,
    896,
    63,
    -85,
    437,
    -453,
    -991,
    294,
    -384,
    -628,
    -529,
    518,
    613,
    -319,
    -519,
    -220,
    -67,
    834,
    619,
    802,
    207,
    946,
    -904,
    295,
    718,
    -740,
    -557,
    -560,
    80,
    296,
    -90,
    401,
    407,
    798,
    254,
    154,
    387,
    434,
    491,
    228,
    307,
    268,
    505,
    -415,
    -976,
    676,
    -917,
    937,
    -609,
    593,
    -36,
    881,
    607,
    121,
    -373,
    915,
    -885,
    879,
    391,
    -158,
    588,
    -641,
    -937,
    986,
    949,
    -321
]


def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array


def quickSortHelper(array, startIdx, endIdx):
    if startIdx >= endIdx:
        return
    leftIdx = startIdx + 1
    rightIdx = endIdx
    pivotValue = array[startIdx]
    while leftIdx <= rightIdx:
        if array[leftIdx] > pivotValue and array[rightIdx] < pivotValue:
            swap(leftIdx, rightIdx, array)
        if array[leftIdx] <= pivotValue:
            leftIdx += 1
        if array[rightIdx] >= pivotValue:
            rightIdx -= 1
    swap(startIdx, rightIdx, array)
    leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx - 1)
    if leftSubarrayIsSmaller:
        quickSortHelper(array, startIdx, rightIdx - 1)
        quickSortHelper(array, rightIdx + 1, endIdx)
    else:
        quickSortHelper(array, rightIdx + 1, endIdx)
        quickSortHelper(array, startIdx, rightIdx - 1)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


print(quickSort(test))
