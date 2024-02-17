from math import isqrt
from multiprocessing import Pool

#################PROBLEMATIC SCRIPT that chains with errors################# 

# Define a helper function to factor a chunk
def factor_chunk(chunk):
    start, end = chunk
    for base in range(start, end):
        if n % base == 0:
            return base, n // base, end - start  # Return the number of attempts along with the factors
    return None, None, end - start

def factor_n_parallel(n, max_attempts=1000, num_processes=4):
    """
    Attempt to factor n by exploiting the fact that P and Q are close to multiples of a smaller prime.
    This version uses multiple processes to speed up the factoring process.
    """
    base = isqrt(n)  # Start from square root of n, which is close to the middle of P and Q

    # Split the range of possible factors into chunks
    chunks = [(base + i * (max_attempts // num_processes), min(base + (i + 1) * (max_attempts // num_processes), n)) for i in range(num_processes)]

    # Use a process pool to factor each chunk in parallel
    with Pool(num_processes) as pool:
        results = pool.map(factor_chunk, chunks)

    # Return the first successful result and print the number of attempts
    for result in results:
        if result[0] is not None and result[1] is not None:
            P, Q, attempts = result
            print(f"Successfully factored n in {attempts} attempts.")
            return P, Q

    print(f"Failed to factor n after {max_attempts} attempts.")
    return None, None

# Example usage
n = 40088832802704901470181567987523672394597381703014301563484604450882065270483487637609176896806594433189019513605162372620675293043380228376
P, Q = factor_n_parallel(n)
print(f"P: {P}\nQ: {Q}")

# Check if P and Q are correct
if P and Q and P * Q == n:
    print("Successfully factored n.")
else:
    print("Failed to factor n.")