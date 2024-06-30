# List of times
times = [
    "06:15", "20:11", "07:30", "04:30", "18:00",
    "06:30", "15:45", "07:45", "07:15", "18:08",
    "19:18", "04:30", "06:09", "19:23", "20:11",
    "18:08", "07:45", "07:15"
]

# Function to convert time to printable ASCII characters by adding a base value (e.g., 32)
def time_to_printable_ascii(time_str, base=64):
    hh, mm = map(int, time_str.split(':'))
    return chr(hh + base) + chr(mm + base)

# Convert each time to printable ASCII characters
printable_ascii_flag = ''.join(time_to_printable_ascii(time) for time in times)

# Print the result
print(printable_ascii_flag)
