import zlib
import struct

def read_chunk(file):
    # Read chunk length
    length_data = file.read(4)
    if len(length_data) < 4:
        return None, None, None, None
    length = struct.unpack('>I', length_data)[0]
    
    # Read chunk type
    type_data = file.read(4)
    if len(type_data) < 4:
        return None, None, None, None
    
    # Read chunk data
    chunk_data = file.read(length)
    if len(chunk_data) < length:
        return None, None, None, None
    
    # Read chunk CRC
    crc_data = file.read(4)
    if len(crc_data) < 4:
        return None, None, None, None
    crc = struct.unpack('>I', crc_data)[0]
    
    # Calculate CRC for verification
    calculated_crc = zlib.crc32(type_data)
    calculated_crc = zlib.crc32(chunk_data, calculated_crc)
    calculated_crc = calculated_crc & 0xffffffff
    
    crc_status = 'OK' if crc == calculated_crc else 'ERRONEOUS'
    
    return type_data.decode('ascii'), chunk_data, crc, crc_status

def display_png_structure(file_path):
    with open(file_path, 'rb') as file:
        # Read and display the magic header
        magic_header = file.read(8)        
        print("+--------------------------------------------------+")
        print("|   PNG File Structure                             |")
        print("+--------------------------------------------------+")
        print("|  Expected Magic Header (8 bytes)                 |")
        # Convert each byte in the magic header to its hex representation and join them into a string
        magic_header_hex = ' '.join([f"{ord(c):02x}" for c in "\x89PNG\r\n\x1a\n"])
        print(f"|  {magic_header_hex}          |")
        if magic_header != b'\x89PNG\r\n\x1a\n':
            #print("\033[91mError: The header is", magic_header.decode('ascii'), "\033[0m")
            print("\033[91mError: The header is", magic_header.hex(), "\033[0m")
        print("+--------------------------------------------------+")
        
        while True:
            chunk_type, chunk_data, crc, crc_status = read_chunk(file)
            if chunk_type is None:
                break
            
            print(f"|  {chunk_type} Chunk ({len(chunk_data)} bytes)   ")
            print("|  +---------------------------------------------+ |")
            print("|  | Length (4 bytes)                            ")
            print("|  +---------------------------------------------+ |")
            print(f"|  | Type: {chunk_type} (4 bytes)               ")
            print("|  +---------------------------------------------+ |")
            print("|  | Data:                                      |  |")
            print(f"|  |  {len(chunk_data)} bytes                     ")
            print("|  +---------------------------------------------+ |")
            print(f"|  | CRC (4 bytes): {crc:08X} : {crc_status}      ")
            print("|  +---------------------------------------------+ |")
            print("+--------------------------------------------------+")
        
        print("+------------------------------------------------------+")
        print("|  IEND Chunk (0 bytes)       |")
        print("|  +------------------------+ |")
        print("|  | Length (4 bytes)       | |")
        print("|  +------------------------+ |")
        print("|  | Type: IEND (4 bytes)   | |")
        print("|  +------------------------+ |")
        print("|  | CRC (4 bytes)         |  |")
        print("|  +------------------------+ |")
        print("+-----------------------------+")

# Use the function with your file
display_png_structure('magic_repairman.png')
