namespace Application.Days
{
    class Day1 : Day
    {
        private List<List<int>> input;

    
        public Day1() : base(1) {
            input = GroupAdjacentNumbers();
        }

    
        public override object Part1()
        {
            List<int> listOfSums = new();

            // Sum all groups of numbers            
            for (int i = 0; i < input.Count; i++)
            {
                List<int> listOfNumbers = input[i];
                int sum = SumNumbers(listOfNumbers);
                listOfSums.Add(sum);
            }

            int largestSum = 0;

            // Find the largest sum
            for (int i = 0; i < listOfSums.Count; i++)
            {
                int sum = listOfSums[i];
                
                if (sum > largestSum) {
                    largestSum = sum;
                }
            }

            return largestSum;
        }

        public override object Part2()
        {
            return null;
        }



         private int SumNumbers(List<int> numbers) {
            int sum = 0;

            for (int i = 0; i < numbers.Count; i++)
            {
                int number = numbers[i];
                sum = sum + number;                
            }

            return sum;
        }

    }
}