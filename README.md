# Simplex Method Implementation in Python

This repository contains a Python implementation of the **Simplex Method** for solving linear programming problems. The Simplex algorithm is used to find the optimal solution to a linear optimization problem, either maximizing or minimizing an objective function subject to a set of linear constraints.

## Overview

This implementation allows for solving both maximization and minimization problems, and it supports the input of arbitrary constraints. The algorithm pivots over a tableau to find the optimal solution by iterating over the decision variables and slack variables.

### Key Features

- Handles maximization and minimization problems.
- Accepts arbitrary number of decision variables and constraints.
- Includes slack variables for constraints.
- Provides precision control via rounding to specified decimal places.
- Detects unbounded solutions and degeneracy in the Simplex method.

## How to Use

### Prerequisites

You need to have Python installed on your system. This implementation is written in pure Python without external dependencies.

### Input

The input consists of the following elements:

1. **Objective Function Coefficients**: Coefficients of the variables in the objective function (either to maximize or minimize).
2. **Constraints Coefficients**: Coefficients of the variables in the constraints.
3. **Right-hand Side Values (RHS)**: The RHS values for each constraint.
4. **Accuracy**: The decimal accuracy for rounding during the algorithm.
5. **Maximization/Minimization Flag**: Whether the objective function is a maximization or minimization problem.

### Functions

#### `is_linear(coefficients)`
This function checks whether all coefficients provided are linear (i.e., numbers).

#### `round_value(val, accuracy)`
This function rounds a value to the specified number of decimal places.

#### `simplex(obj, constraints, rhs, accuracy, is_maximization)`
This is the core function that performs the Simplex algorithm on the given input to find the optimal solution.

#### `input_values()`
Prompts the user to input the values for the objective function, constraints, RHS, and accuracy.

#### `output_values(z_value, answers, is_maximization)`
Outputs the final results of the optimization, including the optimal value of the objective function and the values of the decision variables.

### Example Usage

You can run the algorithm by calling the `simplex()` function with the appropriate inputs from standard input or state them explicitly in the code. Here is a sample test case where we define an objective function, constraints, and RHS:

```python
# Example input for the simplex method
obj = [-2, 3, 4]  # Objective function coefficients
constraints = [[1, 2, 3], [2, 1, 4], [1, 3]]  # Constraint coefficients
rhs = [12, 15, 8]  # Right-hand side values
accuracy = 6  # Decimal places for rounding
is_maximization = False  # Minimization problem

# Running the simplex method
z_value, answers = simplex(obj, constraints, rhs, accuracy, is_maximization)

# Output the results
output_values(z_value, answers, is_maximization)
