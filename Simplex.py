# print("Enter the coefficients of objective function separated by space:")
obj = list(map(int, input().split()))
n = len(obj)
# print("Enter number of constraints:")
m = int(input())
constraints = []
# print("Enter the coefficients of constraint function separated by space (each constraint on each line):")

for i in range(m):
    constraints.append(list(map(int, input().split())))

# print("Enter the right-hand side numbers separated by space:")

rhs = list(map(int, input().split()))

# print("Enter the accuracy:")
accuracy = float(input())

table = [[0 for i in range(n + 1 + m)] for j in range(m+1)]  # Create table

for i in range(n):
    table[0][i] = -obj[i]  # Fill in z-row


for i in range(1, m + 1):  # Fill in constraints coefficients
    for j in range(n):
        if j < len(constraints[i-1]):
            table[i][j] = constraints[i-1][j]

table[0][-1] = 0  # RHS of z
for i in range(1, m+1):  # Other RHS
    table[i][-1] = rhs[i-1]

for i in range(1, m+1):  # Fill in slack variables
    for j in range(n, n + m):
        if j - n == i - 1:
            table[i][j] = 1


print(table)

answers = [0] * n

number_of_answers = 0
while any((x < 0 for x in table[0])):  # Check if there is any negative element
    key_col = -1
    min_val = 1000000000
    for i in range(n + m + 1):  # Find min value and key-column
        if table[0][i] < min_val:
            min_val = table[0][i]
            key_col = i

    key_row = -1
    min_val = 10000000000

    for i in range(1, m+1):  # Find min value and key-row
        if table[i][key_col] != 0 and min_val > table[i][-1] / table[i][key_col] > 0 + accuracy:
            min_val = table[i][-1] / table[i][key_col]
            key_row = i

    pivot = table[key_row][key_col]
    # print("pivot", pivot)
    for i in range(n+m+1):
        table[key_row][i] /= pivot

    for i in range(m+1):  # Make all zeroes in key-column except key-row
        if i != key_row:
            divisor = table[i][key_col]
            print(i+1, divisor)
            for j in range(n + m + 1):
                table[i][j] = table[i][j] - divisor * table[key_row][j]
    answers[0] = table[0][-1]  # Add current z
    if key_col < n:
        answers[key_col] = table[key_row][-1]

    print(table)

print("z =", answers[0])
for i in range(1, n+1):
    if answers[i] != 0:
        print("x"+str(i)+"  ", table[answers[i]][-1])
    else:
        print("x"+str(i)+" = 0")
