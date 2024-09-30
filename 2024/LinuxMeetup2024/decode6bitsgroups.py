# Python script to decrypt the binary string using 6-bit decoding

# The binary string provided
binary_string = '110011101001111000111111100010101001110100111111101101100101110011110011100001100111100101111111100011101111100100100101'

# Step 1: Split the binary string into 6-bit groups
six_bit_groups = [binary_string[i:i+6] for i in range(0, len(binary_string), 6)]

# Step 2: Convert each 6-bit group to decimal
decimal_values = [int(b, 2) for b in six_bit_groups]

# Step 3: Map decimal values to ASCII characters (adding 32 to each value)
ascii_codes = [value + 32 for value in decimal_values]
characters = [chr(code) for code in ascii_codes]

# Step 4: Combine the characters to form the message
message = ''.join(characters)

# Step 5: Form the flag
flag = f'LinuxMUP{{{message}}}'

# Output the flag
print(flag)
