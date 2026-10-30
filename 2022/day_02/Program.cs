// See https://aka.ms/new-console-template for more information
Console.WriteLine("Day 2");
Console.WriteLine("");

// string PATH_FILE = "../data/day_2/test.txt";
string PATH_FILE = "../data/day_2/input.txt";

string[] GetFileContent(string path)
{
  var content = File.ReadLines(path);
  // Console.WriteLine(content.GetType());
  return content.ToArray();
}

int GetScore(string[] matchs)
{
  int score = 0;
  //
  foreach (var match in matchs)
  {
    var hands = match.Split(" ");
    score += GetResultMatch(hands[0], hands[1]);
    // Console.WriteLine($"had elf {hands[0]} had you {hands[1]}");
  }
  return score;
}

//A and X = Rock
//B and Y = Paper
//C and Z = Scissors
// Win is 6 
// Draw is 3 
// Lost is 0 
// Rock + 1
// Paper + 2
// Scissors + 3
int GetResultMatch(string elf, string you)
{
  int result = 0;

  if (elf == "A")
  {
    if (you == "X") return 3 + 1;
    if (you == "Y") return 6 + 2;
    if (you == "Z") return 0 + 3;
  }
  else if (elf == "B")
  {
    if (you == "X") return 0 + 1;
    if (you == "Y") return 3 + 2;
    if (you == "Z") return 6 + 3;
  }
  if (you == "X") return 6 + 1;
  if (you == "Y") return 0 + 2;
  if (you == "Z") return 3 + 3;

  return result;
}

//Part 2 
int GetRealStrategy(string[] matchs)
{
  int score = 0;
  //
  foreach (var match in matchs)
  {
    var hands = match.Split(" ");
    score += GetRealResult(hands[0], hands[1]);
  }
  return score;
}
//A = Rock
//B = Paper
//C = Scissors
// X Meas you need to lose
// Y Means you need to draw
// Z Means you need to Win
// Win is 6 
// Draw is 3 
// Lost is 0 
// Rock + 1
// Paper + 2
// Scissors + 3
int GetRealResult(string elf, string you)
{
  int result = 0;

  if (elf == "A")
  {
    if (you == "X") return 0 + 3;
    if (you == "Y") return 3 + 1;
    if (you == "Z") return 6 + 2;
  }
  else if (elf == "B")
  {
    if (you == "X") return 0 + 1;
    if (you == "Y") return 3 + 2;
    if (you == "Z") return 6 + 3;
  }
  if (you == "X") return 0 + 2;
  if (you == "Y") return 3 + 3;
  if (you == "Z") return 6 + 1;

  return result;
}

string[] content = GetFileContent(PATH_FILE);
int score = GetScore(content);
Console.WriteLine($"The answer for the first part is {score}");

int realScore = GetRealStrategy(content);
Console.WriteLine($"The answer for the second part is {realScore}");
