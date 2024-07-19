import os
import base64

def collect_extraneous_bytes(filename, num_bytes):
    with open(filename, 'rb') as f:
        f.seek(-num_bytes, os.SEEK_END)  # Seek to `num_bytes` from the end of the file
        return f.read()

def display_as_hex(byte_data):
    # Format the bytes as a hex dump similar to `xxd`
    hex_lines = []
    for i in range(0, len(byte_data), 16):
        chunk = byte_data[i:i+16]
        hex_chunk = ' '.join(f'{b:02x}' for b in chunk)
        hex_lines.append(f'{i:08x}: {hex_chunk}')

    hex_output = '\n'.join(hex_lines)
    return hex_output

def decode_base64(base64_string):
    try:
        decoded_bytes = base64.b64decode(base64_string)
        return decoded_bytes.decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error decoding base64 string: {e}")
        return ''

def main():
    filename = 'doubletake.jpg'
    num_bytes = 78  # Number of extraneous bytes to be extracted, can be adjusted
    
    # Step a: Collect the extraneous bytes
    extraneous_bytes = collect_extraneous_bytes(filename, num_bytes)
    
    # Step b: Display as HEX
    hex_output = display_as_hex(extraneous_bytes)
    print("Hex Bytes:")
    print(hex_output)
    
    # Convert the bytes to a string directly
    ascii_string = extraneous_bytes.decode('latin1')
    
    # Filter out non-base64 characters
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    cleaned_base64_string = ''.join(filter(lambda x: x in base64_chars, ascii_string))
    
    print(f"Cleaned Base64 String: {cleaned_base64_string}")
   


if __name__ == "__main__":
    main()
