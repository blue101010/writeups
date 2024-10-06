import base64

def create_minimal_elf():
    elf_header = bytearray(76)

    # ELF Magic Number
    elf_header[0:4] = b'\x7fELF'

    # ELF Class: 64-bit
    elf_header[4] = 2  # EI_CLASS (ELFCLASS64)

    # Data Encoding: Little Endian
    elf_header[5] = 1  # EI_DATA (ELFDATA2LSB)

    # ELF Version
    elf_header[6] = 1  # EI_VERSION (EV_CURRENT)

    # OS ABI
    elf_header[7] = 0  # System V

    # Padding
    elf_header[8:16] = b'\x00' * 8

    # File Type: Executable
    elf_header[0x10:0x12] = (2).to_bytes(2, byteorder='little')  # e_type (ET_EXEC)

    # Machine Type: x86-64
    elf_header[0x12:0x14] = (0x3e).to_bytes(2, byteorder='little')  # e_machine (EM_X86_64)

    # ELF Version
    elf_header[0x14:0x18] = (1).to_bytes(4, byteorder='little')  # e_version (EV_CURRENT)

    # Entry Point (set to 0 for minimal ELF)
    elf_header[0x18:0x20] = (0).to_bytes(8, byteorder='little')  # e_entry

    # Program Header Table Offset (no program headers)
    elf_header[0x20:0x28] = (0).to_bytes(8, byteorder='little')  # e_phoff

    # Section Header Table Offset
    elf_header[0x28:0x30] = (0).to_bytes(8, byteorder='little')  # e_shoff

    # Flags
    elf_header[0x30:0x34] = (0).to_bytes(4, byteorder='little')  # e_flags

    # ELF Header Size
    elf_header[0x34:0x36] = (64).to_bytes(2, byteorder='little')  # e_ehsize

    # Program Header Entry Size (no program headers)
    elf_header[0x36:0x38] = (0).to_bytes(2, byteorder='little')  # e_phentsize

    # Number of Program Header Entries
    elf_header[0x38:0x3a] = (0).to_bytes(2, byteorder='little')  # e_phnum

    # Section Header Entry Size
    elf_header[0x3a:0x3c] = (0).to_bytes(2, byteorder='little')  # e_shentsize

    # Number of Section Header Entries
    elf_header[0x3c:0x3e] = (0).to_bytes(2, byteorder='little')  # e_shnum

    # Section Header String Table Index
    elf_header[0x3e:0x40] = (0).to_bytes(2, byteorder='little')  # e_shstrndx

    # The rest of the data is zero-filled to reach 76 bytes
    elf_data = bytes(elf_header)

    # Base64 encode the ELF data
    b64_elf = base64.b64encode(elf_data).decode('ascii')
    return b64_elf

if __name__ == "__main__":
    b64_string = create_minimal_elf()
    print(b64_string)
