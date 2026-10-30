// See https://aka.ms/new-console-template for more information
Console.WriteLine("Day 3");
Console.WriteLine("");

// const string PATH_FILE = "../data/day_3/test.txt";
const string PATH_FILE = "../data/day_3/input.txt";

string[] GetFileContent(string path)
{
  var content = File.ReadLines(path);
  // Console.WriteLine(content.GetType());
  return content.ToArray();
}

char GetRucksack(string rucksack)
{
  // Console.WriteLine(rucksack);
  int rucksackLengh = rucksack.Length;
  int rucksackLenghHalf = (rucksack.Length / 2) - 1;
  // Console.WriteLine(rucksackLengh);

  for (int i = 0; i <= rucksackLenghHalf; i++)
  {
    // Console.WriteLine(rucksack[i]);
    // Console.WriteLine("--------");
    for (int j = rucksackLenghHalf + 1; j < rucksackLengh; j++)
    {

      // Console.WriteLine(rucksack[j]);
      if (rucksack[i] == rucksack[j])
      {
        return rucksack[i];
      };
    }
  }

  return 'z';

}

char[] GetRepeatedItems(string[] x)
{
  int length = x.Length;
  char[] repeatedItems = new char[length];

  for (int i = 0; i < length; i++)
  {
    char tmp = GetRucksack(x[i]);
    repeatedItems[i] = tmp;
  }

  return repeatedItems;
}

// Lowercase item types a through z have priorities 1 through 26.
// Uppercase item types A through Z have priorities 27 through 52.
int GetSumOfPriorities(char[] items)
{
  int sum = 0;

  foreach (var i in items)
  {
    // Console.WriteLine($"The prioritie of {i} is {prioritie}");
    sum += GetPriority(i);
  }

  return sum;
}

int GetPriority(char item)
{
  int prioritie = 0;
  int asciiValue = (int)item;
  if (asciiValue >= 97) prioritie = asciiValue - 96;
  else prioritie = asciiValue - 38;
  return prioritie;
}

//Functions for the part 2
List<List<char[]>> GetGroupsOf3(string[] content)
{
  var groups = new List<List<char[]>>();
  for (int i = 0; i < content.Length; i += 3)
  {
    List<char[]> group = new List<char[]>();
    group.Add(content[i].ToCharArray());
    group.Add(content[i + 1].ToCharArray());
    group.Add(content[i + 2].ToCharArray());

    groups.Add(group);
  }
  return groups;
}

char FindCommunItemInGroup(List<char[]> group)
{
  foreach (var i in group[0])
  {
    // Console.WriteLine(i);
    if (IsLetterInArray(i, group[1]))
    {
      if (IsLetterInArray(i, group[2]))
      {
        // Console.WriteLine($"The common letter is {i}");
        return i;
      }
    }
  }
  return 'a';
}

bool IsLetterInArray(char letter, char[] arrayToSearch)
{
  foreach (var i in arrayToSearch)
  {
    if (i == letter) return true;
  }
  return false;
}

int GetSumOfBadges(List<List<char[]>> groups)
{
  int sum = 0;
  foreach (var i in groups)
  {
    char badgedLetter = FindCommunItemInGroup(i);
    sum += GetPriority(badgedLetter);
  }

  return sum;
}




var content = GetFileContent(PATH_FILE);
char[] repeatedItems = GetRepeatedItems(content);
int sumOfPriorities = GetSumOfPriorities(repeatedItems);
Console.WriteLine($"The answer of the first part is: {sumOfPriorities}");

var groupsOf3 = GetGroupsOf3(content);
var sumOfBadges = GetSumOfBadges(groupsOf3);
Console.WriteLine($"The answer of the second part is: {sumOfBadges}");

