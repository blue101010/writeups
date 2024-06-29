import zlib
import struct
import sys

def png_crc_check(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    
    pos = 8  # Skip the first 8 bytes (header)
    errors = []
    expected_compression_methods = ["7801", "785E", "789C", "78DA", "78BB", "78F9", "776D", "77BD", "77FB", "779C", "765D", "769D", "76DC", "76FB", "753E", "757E", "75BE", "75 FD"]
    chunk_index = 0
    
    print("PNG CRC Check")
    print("+------+--------+-------------------+---------------------+-------------------+----------------+")
    print("| Index| Chunk  |    Expected CRC   |    Actual CRC       | CRC Status        | Zlib Status    |")
    print("+------+--------+-------------------+---------------------+-------------------+----------------+")

    while pos < len(data):
        chunk_start = pos
        chunk_length = struct.unpack('>I', data[pos:pos+4])[0]
        chunk_type = data[pos+4:pos+8]
        chunk_data = data[pos+8:pos+8+chunk_length]
        chunk_crc = struct.unpack('>I', data[pos+8+chunk_length:pos+12+chunk_length])[0]

        # Calculate the correct CRC
        calculated_crc = zlib.crc32(chunk_type)
        calculated_crc = zlib.crc32(chunk_data, calculated_crc)
        calculated_crc = calculated_crc & 0xffffffff
        
        crc_status = "OK" if chunk_crc == calculated_crc else f"ERROR=0x{calculated_crc:08X}"

        # Check IDAT chunk's zlib data integrity
        zlib_status = "N/A"
        collected_value = chunk_data[:2].hex().upper()
        if chunk_type == b'IDAT':
            try:
                zlib.decompress(chunk_data)
                zlib_status = f"OK (collected: {collected_value})"
            except zlib.error as e:
                zlib_status = f"Zlib Warning"
                errors.append((chunk_type.decode('ascii'), e, chunk_start, expected_compression_methods, collected_value))

        index_display = "N/A" if chunk_type == b'IHDR' else chunk_index
        print(f"| {str(index_display).ljust(4)} | {chunk_type.decode('ascii').ljust(5)}  | 0x{chunk_crc:08X}       | 0x{calculated_crc:08X}           | {crc_status.ljust(17)} | {zlib_status.ljust(65)}     ")
        print("+------+--------+-------------------+---------------------+-------------------+----------------+")

        if chunk_type != b'IHDR':
            chunk_index += 1
        
        pos += 12 + chunk_length

    # Print verbose error details
    if errors:
        print("\nVerbose Error Details:")
        print(f"Zlib versions: Expected 1.2.13, using {zlib.ZLIB_RUNTIME_VERSION}")
        print("+-------+--------+-------------------+---------------------+-------------------+--------------------------------------------------------------------------------------------------+")
        print("| Index |")
        print("+-------+--------+-------------------+---------------------+-------------------+--------------------------------------------------------------------------------------------------+")
        
        print(f"  Expected compression method hex values: {expected_compression_methods}")
        print("+-------+--------+-------------------+---------------------+-------------------+--------------------------------------------------------------------------------------------------+")
        
        
        disp_index = 1
        for chunk_type, error, offset, expected, collected in errors:
            disp_index += 1
            print(f"| Index = {str(disp_index).ljust(4)}")
            print("+------+--------+-------------------+---------------------+-------------------+-------------------------------------------------------------------------------------------------+")
            print(f"Chunk {chunk_type} at offset {offset:#010x}: {error}")
            print(f"  Collected value: {collected}")
            print("+------+--------+-------------------+---------------------+-------------------+-------------------------------------------------------------------------------------------------+")

# Use the function with the provided file or display usage help
if len(sys.argv) > 1:
    file_name = sys.argv[1]
    png_crc_check(file_name)
else:
    print("Usage: python png_crc_check.py <file_name>")
