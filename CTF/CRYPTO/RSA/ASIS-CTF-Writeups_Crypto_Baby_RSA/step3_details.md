```
t_p = pow(s*p + 1, (d-1)/(1 << r), n)
```
In this expression, the operation << in Python, which is a bitwise left shift, is equivalent to multiplying by $2^r$

$$
\Huge  t_p = (s \cdot p + 1)^{\frac{d - 1}{2^r}} \mod n
$$

The relation between n and t_p is to be observed.
```
t_p ≡ 1 *  mod ( p )
```
This is because all the other terms except 1 in the expansion of  would be divisible by p.

This means (t_p - 1) is a multiple of p.

Since n is also a multiple of p, the GCD of (t_p - 1) and n should be equal to p.

In the context of this equation. The pow function with three arguments in Python corresponds to exponentiation followed by taking the result modulo n.`


To demonstrate how the expression \( t_p = (s \cdot p + 1)^{\frac{d - 1}{2^r}} \mod n \) leads to the congruence \( t_p \equiv 1 \mod p \), we need to consider the properties of modular arithmetic and the binomial theorem. Let's break it down step by step:

### 1. Expression in Modular Arithmetic:

Given: \( t_p = (s \cdot p + 1)^{\frac{d - 1}{2^r}} \mod n \)

We are interested in how this expression behaves modulo \( p \), not \( n \).

### 2. Applying the Binomial Theorem:

The binomial theorem states that:

\[ (a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k \]

Applying this to our expression, where \( a = s \cdot p \) and \( b = 1 \):

\[ (s \cdot p + 1)^{\frac{d - 1}{2^r}} = \sum_{k=0}^{\frac{d - 1}{2^r}} \binom{\frac{d - 1}{2^r}}{k} (s \cdot p)^{\frac{d - 1}{2^r} - k} \cdot 1^k \]

### 3. Observing Terms in the Expansion:

Every term in this expansion, except the one where \( k = 0 \), contains a factor of \( p \). This is because when \( k = 0 \), the term is \( 1^{\frac{d - 1}{2^r}} \), which is just 1. For all other values of \( k \), there is at least one factor of \( s \cdot p \) in the term, making the term a multiple of \( p \).

### 4. Reduction Modulo \( p \):

When we take this sum modulo \( p \), all terms containing \( s \cdot p \) will be equivalent to 0 modulo \( p \), since \( s \cdot p \equiv 0 \mod p \). The only term that does not contain \( s \cdot p \) is the one where \( k = 0 \), which is 1.

So, \( (s \cdot p + 1)^{\frac{d - 1}{2^r}} \equiv 1 \mod p \).

### 5. Conclusion:

Therefore, \( t_p = (s \cdot p + 1)^{\frac{d - 1}{2^r}} \mod n \) simplifies to \( t_p \equiv 1 \mod p \) when considered modulo \( p \).

This shows that \( t_p \) is congruent to 1 modulo \( p \), which means \( t_p - 1 \) is a multiple of \( p \), as it's the difference between a number and its remainder upon division by \( p \).
