
// g++ -std=c++17 -Wall -Wextra -o check_txt_files check_txt_files.cpp

#include <iostream>
#include <filesystem>
#include <fstream>
#include <sstream>
#include <algorithm>

namespace fs = std::filesystem;

const std::string targetContent = "62 47 56 32 5a 57 78 6c 5a 6d 5a 6c 59 33 52 37 5a 6d 46 72 5a 56 39 6d 62 47 46 6e 66 51 3d 3d";

void trim(std::string &str) {
    str.erase(str.begin(), std::find_if(str.begin(), str.end(), [](unsigned char ch) {
        return !std::isspace(ch);
    }));
    str.erase(std::find_if(str.rbegin(), str.rend(), [](unsigned char ch) {
        return !std::isspace(ch);
    }).base(), str.end());
}

/**
 * @brief Checks the content of a file against a target content.
 * 
 * This function opens the specified file and reads its content. It then trims the content
 * and compares it with the target content. If the content does not match the target content,
 * it prints the file path and the content to the console.
 * 
 * @param filePath The path to the file to be checked.
 */
void checkFileContent(const fs::path& filePath) {
    std::ifstream file(filePath);
    if (!file.is_open()) {
        std::cerr << "Failed to open file: " << filePath << std::endl;
        return;
    }

    std::ostringstream contentStream;
    contentStream << file.rdbuf();
    std::string content = contentStream.str();
    trim(content);

    if (content != targetContent) {
        std::cout << "File: " << filePath << std::endl;
        std::cout << "Content: " << content << std::endl;
    }
}

void traverseDirectory(const fs::path& directoryPath) {
    for (const auto& entry : fs::recursive_directory_iterator(directoryPath)) {
        if (entry.is_regular_file() && entry.path().extension() == ".txt") {
            checkFileContent(entry.path());
        }
    }
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <directory path>" << std::endl;
        return 1;
    }

    fs::path directoryPath = argv[1];
    if (!fs::exists(directoryPath) || !fs::is_directory(directoryPath)) {
        std::cerr << "Invalid directory path: " << directoryPath << std::endl;
        return 1;
    }

    traverseDirectory(directoryPath);

    return 0;
}