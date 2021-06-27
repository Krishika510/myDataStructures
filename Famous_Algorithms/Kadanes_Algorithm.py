def kadanesAlgorithm(array):
    currentSum = array[0]
    maximumSum = array[0]
    for i in range(1, len(array)):
        currentSum = max(array[i], currentSum + array[i])
        maximumSum = max(currentSum, maximumSum)

    return maximumSum