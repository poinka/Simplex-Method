def simplex(obj, constraints, rhs, accuracy):
    n = len(obj)
    m = len(constraints)
    table = [[0 for i in range(n + 1 + m)] for j in range(m + 1)]  # Create table

    for i in range(n):
        table[0][i] = -obj[i]  # Fill in z-row

    for i in range(1, m + 1):  # Fill in constraints coefficients
        for j in range(n):
            if j < len(constraints[i - 1]):
                table[i][j] = constraints[i - 1][j]

    table[0][-1] = 0  # RHS of z
    for i in range(1, m + 1):  # Other RHS
        table[i][-1] = rhs[i - 1]

    for i in range(1, m + 1):  # Fill in slack variables
        for j in range(n, n + m):
            if j - n == i - 1:
                table[i][j] = 1

    # print(table)

    while any((x < 0 for x in table[0])):  # Check if there is any negative element
        key_col = -1
        min_val = 1000000000
        for i in range(n + m + 1):  # Find min value and key-column
            if table[0][i] < min_val:
                min_val = table[0][i]
                key_col = i

        key_row = -1
        min_val = 10000000000

        for i in range(1, m + 1):  # Find min value and key-row
            if table[i][key_col] != 0 and min_val > table[i][-1] / table[i][key_col] > 0 + accuracy:
                min_val = table[i][-1] / table[i][key_col]
                key_row = i

        pivot = table[key_row][key_col]
        # print("pivot", pivot)
        for i in range(n + m + 1):
            table[key_row][i] /= pivot

        for i in range(m + 1):  # Make all zeroes in key-column except key-row
            if i != key_row:
                divisor = table[i][key_col]
                # print(i + 1, divisor)
                for j in range(n + m + 1):
                    table[i][j] = table[i][j] - divisor * table[key_row][j]

    print("z =", table[0][-1])
    for i in range(1, n + 1):
        print("x" + str(i) + " =", table[i][-1])


simplex([5, 4], [[6, 4], [1, 2], [-1, 1], [0, 1]], [24, 6, 1, 2], 0)
