
# Overview

The security of RSA relies on the practical difficulty of factoring the product of two large prime numbers, the "factoring problem". RSA key pair is generated using 3 large positive integers -

e A constant, usually 65537
n Known as the modulus of public-private key pair. It is a product of 2 large random prime numbers, p and q.  n = p x q
d A large positive integer that makes up the private key. It is calculated as, d = modinv(e, lcm(p - 1, q - 1)) Where modinv is the modulus inverse function and lcm is the least common multiple function.

(e, n) are public variables and make up the public key. d is the private key and is calculated using p and q. If we could somehow factorize n into p and q, we could then be able to calculate d and break RSA. However, factorizing a large number is very difficult and would take some unrealistic amount of time to do so, provided the two prime numbers are randomly chosen.

# Links

# Fermat's factorization Method

<https://github.com/murtaza-u/zet/tree/main/20220808171808>
