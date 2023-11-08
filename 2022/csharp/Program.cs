using Application.Days;

namespace Application
{
    class Program
    {
        static void Main(string[] args)
        {
            List<Day> days = new()
            {
                new Day1()
            };


            foreach (Day day in days)
            {
               day.PrintParts();
            }
        }
    }
}