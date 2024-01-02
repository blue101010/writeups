#https://jsur.in/posts/2021-04-25-s4ctf-crypto-writeups

from sage.all import *
from Crypto.Util.number import long_to_bytes
load('coppersmith.sage')

N = 48564396752059338791464352725210493148212425902751190745668164451763507023284970474595680869078726765719920168392505794415687815488076204724659643390252172928332322944711949999326843460702414647825442748821062427474599006915155109396213406624079900714394311217571510958430682853948004734434233860146109894977
enc = 28767981118696173499362412795754123415661648348744243377735885542432968964926551295510845917978847771440173910696607195964650864733310997503291576565605508828208679238871651079005335403223194484223700571589836641593207297310906538525042640141507638449129445170765859354237239005410738965923592173867475751585

R.<x,y> = PolynomialRing(Zmod(N^2))
P = 10^77 * x + y
Q = 10^77 * y + x
f = N - P*Q
try:
    p, q = small_roots(f, (10^77, 10^77), m=3)[0]
    #f is the polynomial for which we are trying to find small roots.
    #bounds is a tuple representing the bounds within which we expect to find the roots of f.
    #m is an additional parameter that's typically used to set the dimension of the lattice used in the Coppersmith algorithm. It's an important parameter that can affect the #success and runtime of the algorithm. The value of m may need to be adjusted based on the specific problem and the expected size of the roots.
    #d is the degree of the polynomial, which defaults to the degree of f if not specified.

except IndexError:
    print("No small roots found with the given parameters.")
    # Handle the situation, perhaps by trying different parameters or notifying the user
    exit()

P = int(str(p) + str(q))
Q = int(str(q) + str(p))
d = pow(31337, -1, (P-1)*(Q-1))
m = pow(enc, d, N)
print(long_to_bytes(m).decode())