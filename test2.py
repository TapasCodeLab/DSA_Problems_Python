MOD = 10 ** 9 + 7


def matrix_mult(A, B):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]]


def matrix_exponentiation(matrix, power):
    result = [[1, 0], [0, 1]]  # Identity matrix
    base = matrix
    while power:
        if power % 2:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        power //= 2
    return result


def fibonacci(n, F1, F2):
    if n == 1:
        return F1
    if n == 2:
        return F2

    transformation = [[1, 1], [1, 0]]
    result = matrix_exponentiation(transformation, n - 1)
    return (result[0][0] * F2 + result[0][1] * F1) % MOD


def sumonacci_sum(A, F1, F2):
    if A == 1:
        return F1 % MOD

    # Compute S[A] using Fibonacci sum formula: S[A] = F[A+2] - 1
    FA2 = fibonacci(A + 2, F1, F2)  # Compute F[A+2]
    SA = (FA2 - 1 + MOD) % MOD

    # Compute sum of first A Sumonacci numbers using sum formula: (S[1] + S[2] + ... + S[A])
    FAA3 = fibonacci(A + 3, F1, F2)  # Compute F[A+3]
    total_sum = ((FAA3 - 2) % MOD + MOD) % MOD  # Adjusting for 1-based indexing

    return total_sum


# Example Usage:
A = 2
F1 = 3
F2 = 4
print(sumonacci_sum(A, F1, F2))
