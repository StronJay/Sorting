def heapSort(array):
    buildMaxHeap(array)
    for endIdx in reversed(range(1, len(array))):
        swap(0, endIdx, array)
        siftDown(0, endIdx - 1, array)
    return array


def buildMaxHeap(array):
    firstParentIdx = (len(array) - 2) // 2
    for currentIdx in reversed(range(firstParentIdx + 1)):
        siftDown(currentIdx, len(array) - 1, array)


def siftDown(currentIdx, endIdx, heap):
    firstChildIdx = (currentIdx * 2) + 1
    while firstChildIdx <= endIdx:
        secondChildIdx = (currentIdx * 2) + \
            2 if (currentIdx * 2) + 2 <= endIdx else -1
        if secondChildIdx != -1 and heap[secondChildIdx] > heap[firstChildIdx]:
            idxToSwap = secondChildIdx
        else:
            idxToSwap = firstChildIdx
        if heap[idxToSwap] > heap[currentIdx]:
            swap(currentIdx, idxToSwap, heap)
            currentIdx = idxToSwap
            firstChildIdx = (currentIdx * 2) + 1
        else:
            return


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
