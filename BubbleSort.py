test = [
    -823,
    164,
    48,
    -987,
    323,
    399,
    -293,
    183,
    -908,
    -376,
    14,
    980,
    965,
    842,
    422,
    829,
    59,
    724,
    -415,
    -733,
    356,
    -855,
    -155,
    52,
    328,
    -544,
    -371,
    -160,
    -942,
    -51,
    700,
    -363,
    -353,
    -359,
    238,
    892,
    -730,
    -575,
    892,
    490,
    490,
    995,
    572,
    888,
    -935,
    919,
    -191,
    646,
    -120,
    125,
    -817,
    341,
    -575,
    372,
    -874,
    243,
    610,
    -36,
    -685,
    -337,
    -13,
    295,
    800,
    -950,
    -949,
    -257,
    631,
    -542,
    201,
    -796,
    157,
    950,
    540,
    -846,
    -265,
    746,
    355,
    -578,
    -441,
    -254,
    -941,
    -738,
    -469,
    -167,
    -420,
    -126,
    -410,
    59
]


def bubbleSort(array):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                isSorted = False
                array[i], array[i + 1] = array[i + 1], array[i]
        counter += 1
    return array
print(bubbleSort(test))
