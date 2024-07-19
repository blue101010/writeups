// script to analyse JPEG header called SOF0, SOF1...3
// g++ -o jpeg_SOFX jpeg_SOFX.cpp
// debug:: g++ -Wall -Wextra -Werror -O2 -o jpeg_SOFX3 jpeg_SOFX3.cpp

#include <iostream>
#include <fstream>
#include <cstdint>
#include <cstring>
#include <iomanip>
#include <vector>

#pragma pack(1)

// Define a structure to represent the SOF marker segment
struct SOFMarkerSegment {
    uint16_t length;
    uint8_t precision;
    uint16_t height;
    uint16_t width;
    // Additional fields can be added here if needed
};

enum Marker : uint8_t {
    TEM     = 0x01,
    SOF0    = 0xC0,
    SOF1    = 0xC1,
    SOF2    = 0xC2,
    SOF3    = 0xC3,
    DHT     = 0xC4,
    SOF5    = 0xC5,
    SOF6    = 0xC6,
    SOF7    = 0xC7,
    SOI     = 0xD8,
    EOI     = 0xD9,
    SOS     = 0xDA,
    DQT     = 0xDB,
    DNL     = 0xDC,
    DRI     = 0xDD,
    DHP     = 0xDE,
    APP0    = 0xE0,
    APP1    = 0xE1,
    APP2    = 0xE2,
    APP3    = 0xE3,
    APP4    = 0xE4,
    APP5    = 0xE5,
    APP6    = 0xE6,
    APP7    = 0xE7,
    APP8    = 0xE8,
    APP9    = 0xE9,
    APP10   = 0xEA,
    APP11   = 0xEB,
    APP12   = 0xEC,
    APP13   = 0xED,
    APP14   = 0xEE,
    APP15   = 0xEF,
    COM     = 0xFE
};

bool isValidMarker(uint8_t byte) {
    switch (byte) {
        case TEM:
        case SOF0:
        case SOF1:
        case SOF2:
        case SOF3:
        case DHT:
        case SOF5:
        case SOF6:
        case SOF7:
        case SOI:
        case EOI:
        case SOS:
        case DQT:
        case DNL:
        case DRI:
        case DHP:
        case APP0:
        case APP1:
        case APP2:
        case APP3:
        case APP4:
        case APP5:
        case APP6:
        case APP7:
        case APP8:
        case APP9:
        case APP10:
        case APP11:
        case APP12:
        case APP13:
        case APP14:
        case APP15:
        case COM:
            return true;
        default:
            return false;
    }
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <JPEG file path>" << std::endl;
        return 1;
    }

    const char *jpegFilePath = argv[1];
    std::ifstream jpegFile(jpegFilePath, std::ios::binary);

    if (!jpegFile.is_open()) {
        std::cerr << "Failed to open the JPEG file." << std::endl;
        return 1;
    }

    std::vector<uint8_t> fileData((std::istreambuf_iterator<char>(jpegFile)), std::istreambuf_iterator<char>());
    jpegFile.close();

    bool eoiFound = false;
    size_t extraneousBytesCount = 0;

    for (size_t i = 0; i < fileData.size(); ++i) {
        if (fileData[i] == 0xFF && i + 1 < fileData.size() && fileData[i + 1] == 0xD9) {
            eoiFound = true;
            // Check for extraneous bytes before the EOI marker
            for (size_t j = i - 1; j > 0; --j) {
                if (fileData[j] == 0xFF && isValidMarker(fileData[j + 1])) {
                    break;
                }
                extraneousBytesCount++;
            }
            break;
        }
    }

    if (eoiFound) {
        if (extraneousBytesCount > 0) {
            std::cout << "JPEG Information:" << std::endl;
            std::cout << extraneousBytesCount << " extraneous bytes found before marker 0xD9" << std::endl;
        } else {
            std::cout << "JPEG Information:" << std::endl;
            std::cout << "No extraneous bytes before marker 0xD9" << std::endl;
        }
    } else {
        std::cerr << "EOI marker not found in the JPEG file." << std::endl;
    }

    // Analyze JPEG header
    jpegFile.open(jpegFilePath, std::ios::binary);
    if (!jpegFile.is_open()) {
        std::cerr << "Failed to reopen the JPEG file." << std::endl;
        return 1;
    }

    while (!jpegFile.eof()) {
        uint8_t marker;
        jpegFile.read(reinterpret_cast<char *>(&marker), sizeof(marker));

        if (marker == 0xFF) {
            jpegFile.read(reinterpret_cast<char *>(&marker), sizeof(marker));

            if (marker == 0xC0 || marker == 0xC1 || marker == 0xC2 || marker == 0xC3) {
                uint16_t length;
                jpegFile.read(reinterpret_cast<char *>(&length), sizeof(length));

                uint8_t precision;
                jpegFile.read(reinterpret_cast<char *>(&precision), sizeof(precision));

                uint16_t height;
                jpegFile.read(reinterpret_cast<char *>(&height), sizeof(height));

                uint16_t width;
                jpegFile.read(reinterpret_cast<char *>(&width), sizeof(width));

                std::cout << "Marker: 0x" << std::hex << std::setw(2) << std::setfill('0') << static_cast<int>(marker) << std::dec << std::endl;
                std::cout << "Width: " << width << " pixels" << std::endl;
                std::cout << "Height: " << height << " pixels" << std::endl;
                std::cout << "Precision: " << static_cast<int>(precision) << " bits" << std::endl;

                std::cout << "Raw Data:" << std::endl;
                std::cout << "Length: " << length << " bytes" << std::endl;
                std::cout << "Precision: " << static_cast<int>(precision) << std::endl;
                std::cout << "Height: " << height << std::endl;
                std::cout << "Width: " << width << std::endl;

                std::streampos pos = jpegFile.tellg();
                std::cout << "Width HEX: 0x" << std::hex << std::setw(4) << std::setfill('0') << width << std::dec << std::endl;
                std::cout << "Height HEX: 0x" << std::hex << std::setw(4) << std::setfill('0') << height << std::dec << std::endl;
                std::cout << "Width Offset: " << pos - static_cast<std::streamoff>(2) << std::endl;
                std::cout << "Height Offset: " << pos - static_cast<std::streamoff>(4) << std::endl;


                std::cout << std::dec << std::endl;
            } 
            else if (marker == 0xD9) // EOI marker
            {
                eoiFound = true;
                std::streampos pos = jpegFile.tellg();
                std::cout << "EOI marker found at position: " << pos << " (0x" << std::hex << pos << std::dec << ")" << std::endl;
                break;
            }
        }
    }

    jpegFile.close();
    return 0;
}