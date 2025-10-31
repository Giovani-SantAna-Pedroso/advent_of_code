#include <fstream>
#include <iostream>

using namespace std;

int getSequencySum(string &line) {
  int sum = 0;
  for (int i = 0; i < line.length() - 1; i++) {

    if (line[i] == line[i + 1])
      sum += (line[i] - '0');
  }
  if (line[0] == line[line.length() - 1])
    sum += (line[0] - '0');

  return sum;
}

int getSequencySumHalfwayAround(string &line) {
  int sum = 0;
  int sizeLine = line.length();
  int halfSizeLine = sizeLine / 2;

  for (int i = 0, j = halfSizeLine; i < halfSizeLine; i++, j++) {
    if (line[i] == line[j])
      sum += (line[i] - '0');
  }
  // for (int i = halfSizeLine, j = 0; j < sizeLine; i++, j++) {
  //   if (line[i] == line[j])
  //     sum += (line[i] - '0');
  // }

  return sum * 2;
}

int main(int argc, char *argv[]) {
  // char *[] inputFilePath = argv[1];

  // cout << "Day 1 -> " << inputFilePath << endl;

  ifstream inputFile;

  inputFile.open(argv[1]);
  int ans1 = 0;
  int ans2 = 0;

  if (inputFile.is_open()) {

    string line;
    cout << "f" << endl;
    while (getline(inputFile, line)) {
      int seqSum = getSequencySum(line);
      int seqHalfAroundSum = getSequencySumHalfwayAround(line);
      ans1 += seqSum;
      ans2 += seqHalfAroundSum;
      cout << line << " -> " << seqSum << " -> " << seqHalfAroundSum << endl;
    }

    inputFile.close();
  }
  cout << "ans1: " << ans1 << endl;
  cout << "ans2: " << ans2 << endl;
  // inputFile.open(inputFilePath);
  return 0;
}
