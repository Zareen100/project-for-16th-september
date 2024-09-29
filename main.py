# Function to multiply using 1 iteration (direct multiplication)
def multiply_one_iteration(N, M):
    return N * M

# Function to multiply using N iterations (repeated addition)
def multiply_n_iterations(N, M):
    result = 0
    for _ in range(N):
        result += M
    return result

# Example usage
N = int(input("Enter value for N: "))
M = int(input("Enter value for M: "))

# Multiply using one iteration
result_one_iter = multiply_one_iteration(N, M)
print(f"Multiplication using 1 iteration: {result_one_iter}")

# Multiply using N iterations
result_n_iter = multiply_n_iterations(N, M)
print(f"Multiplication using N iterations: {result_n_iter}")
