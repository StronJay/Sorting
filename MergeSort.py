test = [
    -4,
    5,
    10,
    8,
    -10,
    -6,
    -4,
    -2,
    -5,
    3,
    5,
    -4,
    -5,
    -1,
    1,
    6,
    -7,
    -6,
    -7,
    8
]
test1 = [8, 5, 2, 9, 5, 6, 3]


# def mergeSort(array):
#     print("Array:",array)
#     if len(array) == 1:
#         return array
#     middleIdx = len(array) // 2
#     leftHalf = array[:middleIdx]
#     rightHalf = array[middleIdx:]
#     return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))


# def mergeSortedArrays(leftHalf, rightHalf):
#     sortedArray = [None] * (len(leftHalf) + len(rightHalf))
#     k = i = j = 0
#     print(sortedArray)
#     while i < len(leftHalf) and j < len(rightHalf):
#         if leftHalf[i] <= rightHalf[j]:
#             sortedArray[k] = leftHalf[i]
#             i += 1
#         else:
#             sortedArray[k] = rightHalf[j]
#             j += 1
#         k += 1
#     while i < len(leftHalf):
#         sortedArray[k] = leftHalf[i]
#         i += 1
#         k += 1
#     while j < len(rightHalf):
#         sortedArray[k] = rightHalf[j]
#         j += 1
#         k += 1

#     print(sortedArray)
#     return sortedArray


def mergeSort(array):
    if len(array) <= 1:
        return array
    auxiliaryArray = array[:]
    counter = 0
    #print(auxiliaryArray)
    mergeSortHelper(array, 0, len(array) - 1, auxiliaryArray, counter)
    return array


def mergeSortHelper(mainArray, startIdx, endIdx, auxiliaryArray, counter):
    print("MAIN:", mainArray, "AUX:", auxiliaryArray, counter)
    if startIdx == endIdx:
        print("RETURN:",startIdx, endIdx, "COUNTER:", counter)
        return
    middleIdx = (startIdx + endIdx) // 2
    mergeSortHelper(auxiliaryArray, startIdx, middleIdx, mainArray, counter + 1)
    mergeSortHelper(auxiliaryArray, middleIdx + 1, endIdx, mainArray, counter + 1)
    doMerge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray)


def doMerge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray):
    k = startIdx
    i = startIdx
    j = middleIdx + 1
    print("MAINNNNNN:", mainArray)
    while i <= middleIdx and j <= endIdx:
        if auxiliaryArray[i] <= auxiliaryArray[j]:
            mainArray[k] = auxiliaryArray[i]
            i += 1
        else:
            mainArray[k] = auxiliaryArray[j]
            j += 1
        k += 1
    while i <= middleIdx:
        mainArray[k] = auxiliaryArray[i]
        i += 1
        k += 1
    while j <= endIdx:
        mainArray[k] = auxiliaryArray[j]
        j += 1
        k += 1
    

print(mergeSort(test1))
