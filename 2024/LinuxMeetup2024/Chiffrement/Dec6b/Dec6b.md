# Dec6b - 50pts

```
110011101001111000111111100010101001110100111111101101100101110011110011100001100111100101111111100011101111100100100101
```

Step 1: Interpret the Clue "Dec6b"
The clue "Dec6b" can be interpreted as:

Dec: Decode
6b: 6 bits
So, we're likely dealing with an encoding that involves 6-bit groups.

Step 2: Group the Binary String into 6-bit Blocks
First, ensure the binary string's length is a multiple of 6. The given binary string has 120 bits, which is divisible by 6:

```bash
Group  1: 110011
Group  2: 101001
Group  3: 111000
Group  4: 111111
Group  5: 100010
Group  6: 101001
Group  7: 110100
Group  8: 111111
Group  9: 101101
Group 10: 100101
Group 11: 110011
Group 12: 110011
Group 13: 100001
Group 14: 100111
Group 15: 100101
Group 16: 111111
Group 17: 100011
Group 18: 101111
Group 19: 100100
Group 20: 100101
```

Step 3: Convert Each 6-bit Group to Decimal
Convert each 6-bit binary group into its decimal equivalent.

Step 4: Map Decimal Values to ASCII Characters
Given that standard Base64 didn't yield results, we'll use UUencoding mapping, 
which uses a 6-bit encoding and maps values 0–63 to ASCII characters starting from ASCII code 32 (space).

Compute ASCII Codes:
Add 32 to each decimal value to align with the printable ASCII range.

## FLAG

```bash
$ python decode6bitsgroups.py 
LinuxMUP{SIX_BIT_MESSAGE_CODE}
```