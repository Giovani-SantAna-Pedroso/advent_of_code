// See https://aka.ms/new-console-template for more information

Console.WriteLine("Day 1");
Console.WriteLine("");

// Convert to arguments of 
// string PATH_FILE = "../data/day_1/test.txt";
string PATH_FILE = "../data/day_1/input.txt";

string GetFileContent()
{
  try
  {
    string content = File.ReadAllText(PATH_FILE);
    return content;
    // Console.WriteLine(content);

  }
  catch (Exception e)
  {
    Console.WriteLine(e.Message);
    return e.Message;
  }
}

List<List<int>> GetCaloriesElfes(string content)
{
  var tmp = content.Split("\n\n");
  List<List<int>> elfs = new List<List<int>>();
  foreach (var x in tmp)
  {
    string[] calories = x.Split("\n");

    List<int> calorie = new List<int>();
    foreach (var y in calories)
    {
      if (y != "")
      {
        calorie.Add(int.Parse(y));
      }
    }
    elfs.Add(calorie);
  }
  return elfs;
}

List<int> GetTotalCalories(List<List<int>> efls)
{

  List<int> totals = new List<int>();
  // Console.WriteLine(efls);
  foreach (var elf in efls)
  {
    int total = 0;
    foreach (var m in elf)
    {
      total += m;
    }
    totals.Add(total);
  }
  return totals;
}

int[] GetTopCalories(List<int> totlas)
{
  int[] top = new int[3];
  totlas.Sort();
  totlas.Reverse();

  top[0] = totlas[0];
  top[1] = totlas[1];
  top[2] = totlas[2];

  return top;
}

string content = GetFileContent();
var elfes = GetCaloriesElfes(content);
var totlas = GetTotalCalories(elfes);
var top = GetTopCalories(totlas);
Console.WriteLine($"The answer for the first part is: {top[0]}");
Console.WriteLine($"The answer for the second part is: {top[0] + top[1] + top[2]}");


