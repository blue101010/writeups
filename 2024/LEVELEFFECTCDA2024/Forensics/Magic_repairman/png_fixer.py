import zlib
import struct

def fix_png_file(file_path, output_path):
    with open(file_path, 'rb') as file:
        data = file.read()

    # Replace modified header
    modified_header = b'\x89RNG'
    correct_header = b'\x89PNG'

    if data.startswith(modified_header):
        data = correct_header + data[len(modified_header):]
    else:
        print("Modified header not found.")
        return

    # Function to check and fix CRCs of PNG chunks
    def fix_crc(data):
        pos = 8  # Skip the first 8 bytes (header)
        fixed_data = data[:pos]

        while pos < len(data):
            chunk_length = struct.unpack('>I', data[pos:pos+4])[0]
            chunk_type = data[pos+4:pos+8]
            chunk_data = data[pos+8:pos+8+chunk_length]
            chunk_crc = struct.unpack('>I', data[pos+8+chunk_length:pos+12+chunk_length])[0]

            # Calculate the correct CRC
            calculated_crc = zlib.crc32(chunk_type)
            calculated_crc = zlib.crc32(chunk_data, calculated_crc)
            calculated_crc = calculated_crc & 0xffffffff

            if chunk_crc != calculated_crc:
                print(f"Fixing CRC for chunk: {chunk_type.decode('ascii')}")
                fixed_data += struct.pack('>I', chunk_length) + chunk_type + chunk_data + struct.pack('>I', calculated_crc)
            else:
                fixed_data += data[pos:pos+12+chunk_length]

            pos += 12 + chunk_length

        return fixed_data

    # Fix CRCs
    data = fix_crc(data)

    # Save the fixed file
    with open(output_path, 'wb') as output_file:
        output_file.write(data)

    print(f"File saved as {output_path}")

# Use the function with your file
fix_png_file('magic_repairman.png', '2_fixed_magic_repairman.png')
