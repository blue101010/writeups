

# Review 1

Similarities : https://github.com/rishitsaiya/ASIS-CTF-Writeups/blob/master/Crypto/Baby%20RSA/README.md 


# Review 2 
Whenever there are RSA problems, one of the first things I look at is the generation of the prime numbers p and q.

The proper way to generate it is independently

p = getPrime(nbit)
q = getPrime(nbit)
If q is somehow derived from p, then this probably introduces some weakness

Bruteforce: https://github.com/pberba/ctf-solutions/blob/master/20190810-crytoctf/crypto-159-roxen/roxen-solution.ipynb

# Review 3

Initial math review : no evident issue ??........
u and v:

v is derived from u (as part of v = -(p + u * y) % n), but they are not necessarily directly related mathematically beyond this calculation.
u is modified in a loop until u + v is prime. However, this relationship doesn't provide a direct mathematical simplification between u and v.


n:
n is the product of two prime numbers P and Q. This relationship is based on the RSA key generation process.
n is used in various cryptographic operations, including encryption.


c:
c is the ciphertext generated using the public key pkey and the message flag. The exact mathematical relationship between c, u, and v depends on the specifics of the encryption scheme, which is not entirely clear from the provided code.

....however, potentially ?? a potential solution using a generic implementation of Coppersmith's method by "defund"" https://github.com/defund/coppersmith hat finds small roots for any modular multivariate polynomial. 
https://jsur.in/posts/2021-04-25-s4ctf-crypto-writeups




# other links
https://ask.sagemath.org/question/43240/sagemath-and-vscode/
https://github.com/jvdsn/crypto-attacks/blob/master/attacks/factorization/coppersmith.py
https://link.springer.com/chapter/10.1007/978-3-540-24676-3_29
https://github.com/pwang00/Cryptographic-Attacks/blob/master/Public%20Key/RSA/coppersmith_short_pad.sage
https://github.com/truongkma/ctf-tools/blob/master/ReadPublicKey_createPrivateKey.py
https://github.com/truongkma/ctf-tools/blob/master/RSAdecrypt.py
https://github.com/truongkma/ctf-tools/tree/master/rsatool
https://github.com/truongkma/ctf-tools/blob/master/RSA_AND_LLL.sage
https://github.com/truongkma/ctf-tools/blob/master/RecoverPrimeFactors.py
https://github.com/truongkma/ctf-tools/blob/master/RSA_AND_LLL.sage.py
https://asecuritysite.com/sage/

# Analysis review 2024-01-02
A Coppersmith approch to find "small roots" seems interest but even trying to reproduce Ref [2021-025-s4ctf-crypto_baby-RSA](../../../CTF_CRYPTO/RSA/2021-025-s4ctf-crypto_baby-RSA.md)   fails to find the small roots ??/

...TBC !!






# Analysis status


