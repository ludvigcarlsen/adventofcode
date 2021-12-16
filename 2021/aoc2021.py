
"""
You're minding your own business on a ship at sea when the overboard alarm goes off! You rush to see if you can help. Apparently, one of the Elves tripped and accidentally sent the sleigh keys flying into the ocean!

Before you know it, you're inside a submarine the Elves keep ready for situations like this. It's covered in Christmas lights (because of course it is), and it even has an experimental antenna that should be able to track the keys if you can boost its signal strength high enough; there's a little meter that indicates the antenna's signal strength by displaying 0-50 stars.
Your instincts tell you that in order to save Christmas, you'll need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
"""



def day1():
    print("\n--- Day 1: Sonar Sweep ---")

    depths = list()
    with open("data/day1.txt") as file:
        for line in file:
            depths.append(int(line))


    # Puzzle 1
    increases = 0
    previous = depths[0]

    for i in range(1, len(depths)):
        if depths[i] > previous:
            increases += 1
        previous = depths[i]

    print(f"1.1. Number of increases: {increases}")


    # Puzzle 2
    increases = 0

    for i in range(0, len(depths)):
        if (i+3 >= len(depths)): break

        sumA = depths[i]+depths[i+1]+depths[i+2]
        sumB = depths[i+1]+depths[i+2]+depths[i+3]

        if sumB > sumA:
            increases += 1

    print(f"1.2. Number of increases: {increases}")
    depths = list()
    with open("data/day1.txt") as file:
        for line in file:
            depths.append(int(line))


def day2():
    print("\n--- Day 2: Dive! ---")

    directions = list()
    with open("data/day2.txt") as file:
        for line in file:
            parts = line.split()
            directions.append(parts)


    # Puzzle 1

    depth = 0
    forward = 0

    for i in range(0, len(directions)):
        dir = directions[i][0]
        value = int(directions[i][1])

        if dir == "forward":
            forward += value

        elif dir == "down":
            depth += value

        elif dir == "up":
            depth -= value

    sum = depth * forward

    print(f"2.1. Final horizontal position and depth multiplied is {sum}")


    # Puzzle 2

    depth = 0
    forward = 0
    aim = 0

    for i in range(0, len(directions)):
        dir = directions[i][0]
        value = int(directions[i][1])

        if dir == "forward":
            forward += value
            depth += aim * value

        elif dir == "down":
            aim += value

        elif dir == "up":
            aim -= value

    sum = depth * forward

    print(f"2.2. Final horizontal position and depth multiplied is {sum}")


def day3():
    print("\n--- Day 3: Binary Diagnostic ---")

    diagnostics = list()

    with open("data/day3.txt") as file:
        for line in file:
            diagnostics.append(line.strip())


    # Puzzle 1

    gamma = ""
    epsilon = ""

    arrLength = len(diagnostics)
    binLength = len(diagnostics[0])

    for x in range(binLength):
        bitcount = 0

        for y in range(arrLength):
            bitcount += int(diagnostics[y][x])

        if (bitcount > arrLength/2):
            gamma += '1'
            epsilon += '0'

        else:
            gamma += '0'
            epsilon += '1'


    # Convert binary strings to integer, and multiply
    result = (int(gamma, 2) * int(epsilon, 2))
    print(f"3.1. The power consumption of the submarine is {result}")



    # Puzzle 2

    def rec(array, bitIdx):
        positives = list()
        negatives = list()

        #Terminal case
        if len(array) == 1:
            return

        elif len(array) == 0: return

        # Split values into arrays by bit value at idx
        for y in range(len(array)):
            bit = int(array[y][bitIdx])

            if bit:
                positives.append(array[y])
            else:
                negatives.append(array[y])
        bitIdx += 1

        # Recursive calls on respective arrays
        if len(positives) >= len(negatives):
            rec(positives, bitIdx) # oxygen
            rec(negatives, bitIdx) # co2
            return

        else:
            rec(negatives, bitIdx) # oxygen
            rec(positives, bitIdx) # co2
            return

    ratings = rec(diagnostics, 0)

    #lsr = oxyRating * co2rating
    #print(f"3.2. The life support rating is of the submarine is {lsr}")


def day4():
    print("\n--- Day 4: Giant Squid ---")

    numbers = []
    boards = []

    # Read file
    with open("data/day4.txt") as file:
        numbers = list(map(int, file.readline().strip().split(',')))
        board = []

        lines = file.readlines()
        for i, line in enumerate(lines):
             # Skip first empty line
            if (i == 0): continue

            # Check for last line
            if (line is lines[-1]):
                board.append(list(map(int, line.split())))
                boards.append(board[:])

            # End of board reached, add to list and clear
            line = line.strip()
            if (not line):
                boards.append(board[:])
                board.clear()

            # Add row to current board
            else:
                board.append(list(map(int, line.split())))


    # Function to check for win on board
    def checkWin(board, x, y):
        # Check marked row
        row = board[x]
        rowWin = all(i == -1 for i in row)

        # Check marked column
        column = [row[y] for row in board]
        colWin = all(i == -1 for i in column)
        return (rowWin or colWin)


    # Function to calculate score on winning board
    def calculateScore(board, winNum, puzzleNr):
        sum = 0

        for x, row in enumerate(board):
            for y, col in enumerate(row):
                if board[x][y] == -1: continue

                sum += board[x][y]
        score = sum * winNum

        print(f"{puzzleNr} The final score is {score}")


    def playBingo():
        firstWin = True
        boardsLeft = len(boards)

        for n in numbers:
            for board in boards:

                if not board: continue
                for x, row in enumerate(board):
                    if not board: break
                    for y, col in enumerate(row):
                        if not board: break

                        # Continue if no match
                        if not n == col: continue

                        # Set to -1 to mark it
                        board[x][y] = -1

                        # Continue of no win
                        if not checkWin(board, x, y):
                            continue

                        # First winning board found
                        if firstWin:
                            calculateScore(board, n, "4.1.")
                            firstWin = False

                        # Last winning board found
                        if boardsLeft == 1:
                            calculateScore(board, n, "4.2.")
                            return

                        # Mark board as completed
                        board.clear()
                        boardsLeft -= 1

    playBingo();


def day5():
    print("\n--- Day 5: Hydrothermal Venture ---")

    ventData = []

    with open("data/day5.txt") as file:
        for line in file:
            vent = line.strip().split(' -> ')
            point1 = list(map(int, vent[0].split(',')))
            point2 = list(map(int, vent[1].split(',')))

            ventData.append([point1, point2])


    def checkDanger(value):
        return value == 2


    def drawHorizontal(matrix, xs, xe, y):
        dangerCount = 0

        if xs > xe:
            xs, xe = xe, xs

        for x in range(xs, xe+1):
            matrix[y][x] += 1
            if (checkDanger(matrix[y][x])): dangerCount += 1
        return dangerCount


    def drawVertical(matrix, ys, ye, x):
        dangerCount = 0

        if ys > ye:
            ys, ye = ye, ys

        for y in range(ys, ye+1):
            matrix[y][x] += 1
            if (checkDanger(matrix[y][x])): dangerCount += 1
        return dangerCount


    def drawDiagonal(matrix, xs, ys, xe, ye):
        dangerCount = 0
        dir = 1

        # Always start from left
        if xs > xe:
            xs, xe = xe, xs
            ys, ye = ye, ys

        # Decide if y should increase or decrease
        if ys > ye:
            dir = -1

        x = xs
        y = ys

        for i in range(xs, xe+1):
            matrix[y][x] += 1

            if (checkDanger(matrix[y][x])): dangerCount += 1

            x += 1
            y += dir
        return dangerCount


    def puzzle1(matrix):
        dangerCount = 0

        for line in ventData:
            x1 = line[0][0]
            y1 = line[0][1]
            x2 = line[1][0]
            y2 = line[1][1]

            # Vertical line
            if x1 == x2:
                dangerCount += drawVertical(matrix, y1, y2, x1)

            # Horizontal line
            elif y1 == y2:
                dangerCount += drawHorizontal(matrix, x1, x2, y1)
        return dangerCount


    def puzzle2(matrix):
        dangerCount = 0
        for line in ventData:

            x1 = line[0][0]
            y1 = line[0][1]
            x2 = line[1][0]
            y2 = line[1][1]

            # Vertical line
            if x1 == x2:
                dangerCount += drawVertical(matrix, y1, y2, x1)

            # Horizontal line
            elif y1 == y2:
                dangerCount += drawHorizontal(matrix, x1, x2, y1)

            # Diagonal (from left to right)
            elif abs(x1-x2) == abs(y1-y2):
                dangerCount += drawDiagonal(matrix, x1, y1, x2, y2)
        return dangerCount


    size = 1000
    ventDiagram1 = [[0 for col in range(size)] for row in range(size)]
    ventDiagram2 = [row[:] for row in ventDiagram1]

    dangerCount1 = puzzle1(ventDiagram1)
    dangerCount2 = puzzle2(ventDiagram2)


    print(f"5.1. The number of dangerous points is {dangerCount1}")
    print(f"5.2. The number of dangerous points is {dangerCount2}")


def day6():
    print("\n--- Day 6: Lanternfish ---")

    data = []

    with open("data/day6.txt") as file:
        content = file.read()
        numbers = content.split(',')
        data = list(map(int, numbers))


    def simulate(fishes, days):
        for d in range(0, days):
            for f in range(0, len(fishes)):


                # Fish timer has reached 0
                if not fishes[f]:
                    fishes[f] = 6
                    fishes.append(8)

                else:
                    fishes[f] -= 1
        return len(fishes)


    def count_fishes(fishes, days):
        print(fishes)
        fish_counts = [fishes.count(i) for i in range(9)]

        for day in range(days):
            fish_reproducing = fish_counts[0]
            fish_counts[0] = 0
            for i in range(8):
                fish_counts[i] = fish_counts[i+1]
            fish_counts[8] = fish_reproducing
            fish_counts[6] += fish_reproducing

        return sum(fish_counts)


    print(f"6.1. There are {simulate(data[:], 80)} lanternfish after {80} days")
    print(f"6.2. There are {count_fishes(data, 256)} lanternfish after {256} days")


def day7():
    print("\n--- Day 7: The Treachery of Whales ---")

    data = []
    exampleData = [16,1,2,0,4,2,7,1,2,14]

    with open("data/day7.txt") as file:
        content = file.read()
        numbers = content.split(',')
        data = list(map(int, numbers))


    def puzzle1(data):

        lowestFuel = float('inf')
        highestPos = max(data)

        for pos in range(1, highestPos):
            fuelCost = sum(abs(crab-pos) for crab in data)
            lowestFuel = min(lowestFuel, fuelCost)

        return lowestFuel


    def puzzle2(data):

        lowestFuel = float('inf')
        highestPos = max(data)

        for pos in range(1, highestPos):
            fuelCost = 0
            for crab in data:
                steps = abs(crab-pos)
                fuelCost += (steps * (steps+1)) / 2

            lowestFuel = min(lowestFuel, fuelCost)
        return lowestFuel

    print(puzzle1(data))
    print(puzzle2(data))





def main():
    #day1()
    #day2()
    #day3()
    #day4()
    #day5()
    #day6()
    day7()


if __name__ == "__main__":
    main()
