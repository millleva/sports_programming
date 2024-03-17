def findLongestDivisibleSubsequence(sequence):
    n = len(sequence)
    dp = [1] * n
    maxLength = 1

    for i in range(1, n):
        for j in range(i):
            if sequence[i] % sequence[j] == 0 and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                maxLength = max(maxLength, dp[i])

    subsequence = []
    lastElement = -1

    for i in range(n - 1, -1, -1):
        if dp[i] == maxLength and (lastElement == -1 or lastElement % sequence[i] == 0):
            subsequence.append(sequence[i])
            maxLength -= 1
            lastElement = sequence[i]

    subsequence.reverse()
    return subsequence

sequence = [2, 3, 4, 5, 8, 9, 16, 32, 64, 128, 256, 512]
result = findLongestDivisibleSubsequence(sequence)
print("Максимально довга підпослідовність:", result)