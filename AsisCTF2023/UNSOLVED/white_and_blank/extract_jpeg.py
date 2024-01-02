# Python 3
import binascii

# Define the JPEG header and EOI marker
#jpeg_header = b'\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01'
jpeg_header = b'\xFF\xD8'
jpeg_eoi = b'\xFF\xD9'

# Define the input and output file paths
input_file_path = 'whiteandblank'
output_file_path = 'output.jpg'

# Open the input file in binary mode
with open(input_file_path, 'rb') as input_file:
    # Read the entire file into memory
    # Note: This might not be feasible for very large files
    data = input_file.read()

# Find the start and end of the JPEG file
start = data.find(jpeg_header)
end = data.find(jpeg_eoi, start) + 2  # Add 2 to include the EOI marker itself

if start == -1 or end == -1:
    print('JPEG file not found in file.')
else:
    # Extract the JPEG file
    jpeg_data = data[start:end]

    # Write the JPEG data to the output file
    with open(output_file_path, 'wb') as output_file:
        output_file.write(jpeg_data)

    print('JPEG data extracted to:', output_file_path)