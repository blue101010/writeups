from math import isqrt
from sympy import nextprime

"""
To implement a script that exploits the fact that P and Q are close to multiples of p for factoring n, we need to consider how P and Q are generated. 
As P and Q are the next primes after p * some_prime, where some_prime is a prime number of nbit // 2 - 10 bits, they are likely to be close to p * some_prime.

The strategy here will be to find a close multiple of a smaller prime near sqrt(n) and test nearby primes to see if they divide n. Once we find such a prime, we can divide n by this prime to get the other factor.
"""

def factor_n(n, max_attempts=1000):
    """
    Attempt to factor n by exploiting the fact that P and Q are close to multiples of a smaller prime.
    """
    base = isqrt(n)  # Start from square root of n, which is close to the middle of P and Q

    for attempt in range(max_attempts):
        # Print the current base value for each attempt
        print(f"Attempt {attempt + 1}: Trying with base = {base}")

        # Check if the current base is a factor
        if n % base == 0:
            return base, n // base

        # Move to the next prime number and try again
        base = nextprime(base)

    return None, None

# Example usage
n = 4008883280270490147018156798752367239459738170301430156348460445088206527048348763760917689680659443318901951360516237262067529304338022837630483645196033621304254000080347982506422415455884933061116059048068199094286198189562171954474774550333796393036361152513608385296841124457358944339309759412021626022854509621495881349117414093445491445654319715891479654096144019797840785614103437600093538599616479514552612464205903106999476721076731416925688036797972413175747167321276835717505959961674004440955460813234396658192578904514644322909786797887720838286121169342271751904104529587650648676532260230880251
P, Q = factor_n(n)
print(f"P: {P}\nQ: {Q}")

# Check if P and Q are correct
if P and Q and P * Q == n:
    print("Successfully factored n.")
else:
    print("Failed to factor n.")
