print("Enter the coefficients of objective function separated by space:")
obj = list(map(int, input().split()))
n = len(obj)
print("Enter number of constraints:")
m = int(input())
constraints = []
print("Enter the coefficients of constraint function separated by space (each constraint on each line):")

for i in range(m):
    constraints.append(list(map(int, input().split())))

print("Enter the right-hand side numbers separated by space:")

rhs = list(map(int, input().split()))

print("Enter the accuracy:")
accuracy = float(input())

table = [[0 for i in range(n + 1 + m)] for j in range(m+1)]

for i in range(n):
    table[0][i] = obj[i]


for i in range(1, m + 1):
    for j in range(n):
        if j < len(constraints[i-1]):
            table[i][j] = constraints[i-1][j]

for i in range(m+1):
    table[i][-1] = rhs[i]

for i in range(1, m+1):
    for j in range(n, n + m):
        if (j + 1) % n == i:
            table[i][j] = 1

print(table)

while any(table[0]) < 0:
    key_col = -1
    min_val = 10000
    for i in range(n + m + 1):
        if table[0][i] < min_val:
            min_val = table[0][i]
            key_col = i

    key_row = -1
    min_val = 10000
    for i in range(1, m+1):
        if min_val > table[i][-1] / table[i][key_col] > 0 + accuracy:
            min_val = table[i][-1] / table[i][key_col]
            key_row = i

    pivot = table[key_row][key_col]
    print(pivot)
    break