def is_linear(coefficients):
    """Check if all coefficients are numbers (linear)."""
    return all(isinstance(c, (int, float)) for c in coefficients)


def round_value(val, accuracy):
    return round(val, accuracy)


def simplex(obj, constraints, rhs, accuracy, is_maximization):
    n = len(obj)
    m = len(constraints)

    if not is_maximization:
        obj = [-x for x in obj]

    # Building the simplex tableau
    table = [[0 for i in range(n + 1 + m)] for j in range(m+1)]  # Create table

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

    # print("Initial Simplex Tableau:")
    # print(table)

    answers = [0] * n  # List to store decision variable values
    z_value = 0  # This will store the value of the objective function
    while any(round_value(x, accuracy) < 0 for x in table[0]):  # Check if there is any negative element
        key_col = -1
        min_val = float('inf')

        # Find the column to pivot on
        for i in range(n + m + 1):
            if round_value(table[0][i], accuracy) < round_value(min_val, accuracy):
                min_val = table[0][i]
                key_col = i

        if key_col == -1:
            print("No valid pivot column found. The method is not applicable!")
            exit()

        key_row = -1
        min_ratio = float('inf')

        # Find the row to pivot on
        for i in range(1, m + 1):
            if round_value(table[i][key_col], accuracy) > 0:
                ratio = table[i][-1] / table[i][key_col]
                if 0 <= round_value(ratio, accuracy) < round_value(min_ratio, accuracy):
                    min_ratio = ratio
                    key_row = i

        if key_row == -1:
            print("Unbounded solution. The method is not applicable!")
            exit()

        # Perform the pivot
        pivot = table[key_row][key_col]
        for i in range(n + m + 1):
            table[key_row][i] = round_value(table[key_row][i] / pivot, accuracy)

        for i in range(m + 1):  # Make all zeroes in key-column except key-row
            if i != key_row:
                divisor = table[i][key_col]
                for j in range(n + m + 1):
                    table[i][j] = round_value(table[i][j] - divisor * table[key_row][j], accuracy)

        # Check for degeneracy
        if round_value(table[key_row][-1], accuracy) == 0:
            print(f"Degeneracy detected in row {key_row}. A basic variable is zero.")

        z_value = round_value(table[0][-1], accuracy)  # Update the current value of z
        if key_col < n:
            answers[key_col] = round_value(table[key_row][-1], accuracy)  # Update the value of the corresponding decision variable

        print("Updated Simplex Tableau:")
        print(table, key_row)
        
    return z_value, answers


def input_values():
    # Input validation
    try:
        print("Enter the coefficients of objective function separated by space:")
        obj = list(map(float, input().split()))  # Ensure all values are floats
        if not is_linear(obj):
            raise ValueError("Non-linear coefficients in objective function.")
        n = len(obj)

        print("Enter number of constraints:")
        m = int(input())
        constraints = []
        
        print("Enter the coefficients of constraint function separated by space (each constraint on each line):")
        for i in range(m):
            constraint = list(map(float, input().split()))
            if len(constraint) != n:  # Check that each constraint has the correct number of coefficients
                raise ValueError("Incorrect number of coefficients in constraints.")
            if not is_linear(constraint):
                raise ValueError("Non-linear coefficients in constraints.")
            constraints.append(constraint)

        print("Enter the right-hand side numbers separated by space:")
        rhs = list(map(float, input().split()))
        if len(rhs) != m:
            raise ValueError("Number of RHS values does not match number of constraints.")

        print("Enter the accuracy (number of decimal places for rounding):")
        accuracy = int(input())

        print("Are you trying to maximize the function? (yes/no):")
        is_maximization = input().lower() == 'yes'

    except ValueError:
        print("The method is not applicable!")
        exit()
    
    return obj, constraints, rhs, accuracy, is_maximization


def output_values(z_value, answers, is_maximization):
    # Final output
    if is_maximization:
        print("Maximum z =", z_value)
    else:
        print("Minimum z =", -z_value)

    # Output the values of decision variables
    for i in range(len(answers)):
        print(f"x{i + 1} =", answers[i])


# obj, constraints, rhs, accuracy, is_maximization = input_values()
# or
obj, constraints, rhs, accuracy, is_maximization = [3, 9], [[1, 4], [1, 2]], [8, 4], 6, True
z_value, answers = simplex(obj, constraints, rhs, accuracy, is_maximization)
output_values(z_value, answers, is_maximization)