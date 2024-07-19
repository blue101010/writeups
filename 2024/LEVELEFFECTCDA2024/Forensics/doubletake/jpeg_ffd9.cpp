// script to display the last ffd9 marker and its offset
// build with debug:: g++ -Wall -Wextra -Werror -O2 -o jpeg_ffd9 jpeg_ffd9.cpp


#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <cstdint> // Include this header for uint8_t

// Function to find and display the last ffd9 marker and its offset
/**
 * Displays the last occurrence of the FFd9 marker in a binary file.
 *
 * @param filePath The path to the binary file.
 */
void displayLastFFd9Marker(const char *filePath) {
    std::ifstream file(filePath, std::ios::binary);
    if (!file.is_open()) {
        std::cerr << "Failed to open the file." << std::endl;
        return;
    }

    std::vector<uint8_t> fileData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();

    size_t lastFFd9Offset = std::string::npos;
    for (size_t i = 0; i < fileData.size() - 1; ++i) {
        if (fileData[i] == 0xFF && fileData[i + 1] == 0xD9) {
            lastFFd9Offset = i;
        }
    }

    if (lastFFd9Offset == std::string::npos) {
        std::cerr << "No ffd9 marker found in the file." << std::endl;
        return;
    }

    // Print the offset in both decimal and hexadecimal formats
    std::cout << "Last FFD9 marker found at position: " << lastFFd9Offset 
              << " (0x" << std::hex << lastFFd9Offset << std::dec << ")" << std::endl;

    // Print the bytes around the offset in xxd format
    std::cout << std::hex << std::setw(8) << std::setfill('0') << (lastFFd9Offset & ~0xF) << ": ";
    for (size_t i = lastFFd9Offset & ~0xF; i < (lastFFd9Offset & ~0xF) + 16; ++i) {
        if (i < fileData.size()) {
            std::cout << std::hex << std::setw(2) << std::setfill('0') << static_cast<int>(fileData[i]) << " ";
        } else {
            std::cout << "   ";
        }
    }
    std::cout << "  ";
    for (size_t i = lastFFd9Offset & ~0xF; i < (lastFFd9Offset & ~0xF) + 16; ++i) {
        if (i < fileData.size()) {
            char c = static_cast<char>(fileData[i]);
            std::cout << (isprint(c) ? c : '.');
        } else {
            std::cout << " ";
        }
    }
    std::cout << std::endl;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <file path>" << std::endl;
        return 1;
    }

    const char *filePath = argv[1];

    // Call the function to display the last ffd9 marker and its offset
    displayLastFFd9Marker(filePath);

    return 0;
}