#include <filesystem>
#include <iostream>
#include <string>
namespace fs = std::filesystem;

void solveA(std::string filePath) {}

int main(int argc, char *argv[]) {
  std::cout << "\033[1m\033[32m\nChallenge A of day 01: \033[0m\n\n";
  const auto &files = fs::directory_iterator("./");
  const bool isTestting = std::string(argv[1]) == "--test";

  for (const auto &file : fs::directory_iterator("./")) {
    std::string path = std::string(file.path());

    if (isTestting) {

    } else {
      if (path.star())
    }
  }

  std::cout << std::endl;
  return 0;
}
