def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    else:
        maxSums = [0] * len(array)
        maxSums[0] = array[0]
        for i in range(1, len(array)):
            maxSums[i] = max(maxSums[i-1], maxSums[i-2] + array[i])

        return maxSums[-1]