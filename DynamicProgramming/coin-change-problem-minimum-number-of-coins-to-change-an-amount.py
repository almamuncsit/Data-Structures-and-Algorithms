def min_coins(coins, weight):
    coins.sort()
    matrix = [[0 for _ in range(weight + 1)] for j in range(len(coins))]
    matrix[0][0] = 0
    for j in range(1, weight + 1):
        if j % coins[0] == 0:
            matrix[0][j] = j // coins[0]

    for i in range(1, len(matrix)):
        for j in range(weight + 1):
            if coins[i] > j:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = min(matrix[i - 1][j], 1 + matrix[i][j - coins[i]])

    return matrix[-1][-1]


if __name__ == '__main__':
    available_coins = [1, 5, 6, 9]
    total = 24
    print(min_coins(available_coins, total))
