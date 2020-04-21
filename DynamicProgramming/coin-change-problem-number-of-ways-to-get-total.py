def coin_change(coins, weight):
    coins.sort()
    coins.insert(0, 0)
    matrix = [[None for _ in range(weight + 1)] for j in range(len(coins))]
    matrix[0][0] = 1
    for j in range(1, weight + 1):
        matrix[0][j] = 0

    for i in range(1, len(matrix)):
        for j in range(weight + 1):
            if coins[i] > j:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - coins[i]]

    return matrix[-1][-1]


if __name__ == '__main__':
    available_coins = [2, 3, 5, 10]
    total = 15
    print(coin_change(available_coins, total))
