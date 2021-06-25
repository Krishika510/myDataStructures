def minNumberOfCoinsForChange(n, denoms):
    ways = [float("inf") for amount in range(n+1)]
    ways[0] = 0

    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] = min(ways[amount], 1 + ways[amount-denom])

    if ways[n] == float("inf"):
        return -1
    else:
        return ways[n]