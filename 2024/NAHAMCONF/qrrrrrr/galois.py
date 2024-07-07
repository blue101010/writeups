# Precomputed tables for GF(2^8)
gf_exp = [0] * 512
gf_log = [0] * 256

def init_tables(prim=0x11d):
    """ Initialize the exponential and logarithm tables for GF(2^8). """
    x = 1
    for i in range(255):
        gf_exp[i] = x
        gf_log[x] = i
        x <<= 1
        if x & 0x100:
            x ^= prim
    for i in range(255, 512):
        gf_exp[i] = gf_exp[i - 255]

def gf_mul(x, y):
    """ Multiply two numbers in GF(2^8). """
    if x == 0 or y == 0:
        return 0
    return gf_exp[gf_log[x] + gf_log[y]]

def gf_poly_mul(p, q):
    """ Multiply two polynomials in GF(2^8). """
    r = [0] * (len(p) + len(q) - 1)
    for j in range(len(q)):
        for i in range(len(p)):
            r[i + j] ^= gf_mul(p[i], q[j])
    return r

def gf_poly_add(p, q):
    """ Add two polynomials in GF(2^8). """
    r = [0] * max(len(p), len(q))
    for i in range(len(p)):
        r[i + len(r) - len(p)] = p[i]
    for i in range(len(q)):
        r[i + len(r) - len(q)] ^= q[i]
    return r

def rs_generator_poly(nsym):
    """ Generate a generator polynomial for RS encoding. """
    g = [1]
    for i in range(nsym):
        g = gf_poly_mul(g, [1, gf_exp[i]])
    return g

def rs_encode_msg(msg_in, nsym):
    """
    Encode a message using Reed-Solomon codes.

    Args:
        msg_in (list): The input message to be encoded.
        nsym (int): The number of error correction symbols to be added.

    Returns:
        list: The encoded message with error correction symbols.

    """
    init_tables()
    gen = rs_generator_poly(nsym)
    msg_out = [0] * (len(msg_in) + nsym)
    msg_out[:len(msg_in)] = msg_in

    for i in range(len(msg_in)):
        coef = msg_out[i]
        if coef != 0:
            for j in range(len(gen)):
                msg_out[i + j] ^= gf_mul(gen[j], coef)
    
    msg_out[:len(msg_in)] = msg_in
    return msg_out

# Example usage
if __name__ == "__main__":
    message = [32, 91, 11, 98, 56]  # example message
    nsym = 10  # number of error correction symbols
    encoded_message = rs_encode_msg(message, nsym)
    print("Original message:", message)
    print("Number of error correction symbols:", nsym)
    print("Encoded message:", encoded_message)
