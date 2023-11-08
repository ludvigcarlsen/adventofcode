using System.Reflection.Metadata.Ecma335;

namespace Application 
{

    abstract class Day
    {
        protected readonly int day;
        protected readonly List<string> data;
        
        public Day(int day) {
            this.day = day;
            this.data = ReadFile();
        }

        public abstract Object Part1();
        public abstract Object Part2();

        public void PrintParts() {
            Console.WriteLine(Part1());
            Console.WriteLine(Part2());
        }

        /*
        Groups lines that are separated by empty lines
        */
        protected List<List<int>> GroupAdjacentNumbers() {
            List<List<int>> result = new();
            List<int> currentGroup = new();

            foreach (string line in data)
            {
                if (string.IsNullOrWhiteSpace(line))
                {
                    result.Add(currentGroup);
                    currentGroup = new List<int>();
                }
                else {
                    currentGroup.Add(int.Parse(line));
                }
            }
            return result;
        }  

        /*
        Returns lines as a single, continous string
        */
        protected string InputSingleString() 
        {
            return string.Join("", data);
        }

         /*
        Reads file into a list of strings
        */
        private List<string> ReadFile() {
            string relativePath = "data/day" + day + ".txt";
            string fullPath = Path.Combine(Environment.CurrentDirectory, relativePath);

            try {
                return new List<string>(File.ReadAllLines(fullPath));
            }
            catch(Exception e) 
            {
                Console.WriteLine(e.Message);
                throw new ApplicationException("Error reading file", e);
            }
        }
    }
}