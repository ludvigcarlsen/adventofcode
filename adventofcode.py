def day1():

    """ Day 1: Report Repair

    After saving Christmas five years in a row, you've decided to take a vacation
    at a nice resort on a tropical island. Surely, Christmas will go on without you.
    The tropical island has its own currency and is entirely cash-only. The gold
    coins used there have a little picture of a starfish; the locals just call them
    stars. None of the currency exchanges seem to have heard of them, but somehow,
    you'll need to find fifty of these coins by the time you arrive so you can pay
    the deposit on your room.

    To save your vacation, you need to get all fifty stars by December 25th.
    Collect stars by solving puzzles. Two puzzles will be made available on each day
    in the Advent calendar; the second puzzle is unlocked when you complete the
    first. Each puzzle grants one star. Good luck!

    Before you leave, the Elves in accounting just need you to fix your expense
    report (your puzzle input); apparently, something isn't quite adding up.
    Specifically, they need you to find the two entries that sum to 2020 and then
    multiply those two numbers together.
    """

    print("\n--- DAY 1 ---")
    numbers = list()

    with open("data/day1.txt") as file:
        for line in file:
            numbers.append(int(line))

    for i in numbers:
        for j in numbers:
            if i + j == 2020:
                result = i * j
                print(f"1.1. The product of the two entries that sum to 2020 is {result}")
                break
        else:
            continue
        break


    """--- Part Two ---
    The Elves in accounting are thankful for your help; one of them even offers
    you a starfish coin they had left over from a past vacation. They offer you
    a second one if you can find three numbers in your expense report that meet
    the same criteria.

    In your expense report, what is the product of the three entries that sum to 2020?
    """

    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i + j + k == 2020:
                    result = i * j * k
                    print(f"1.2. The product of the tree entries that sum to 2020 is {result}")
                    return


def day2():

    """Day 2: Password Philosophy
    Your flight departs in a few days from the coastal airport; the easiest way
    down to the coast from here is via toboggan. The shopkeeper at the North Pole
    Toboggan Rental Shop is having a bad day. "Something's wrong with our computers;
    we can't log in!" You ask if you can take a look. Their password database seems
    to be a little corrupted: some of the passwords wouldn't have been allowed by
    the Official Toboggan Corporate Policy that was in effect when they were chosen.
    To try to debug the problem, they have created a list (your puzzle input) of
    passwords (according to the corrupted database) and the corporate policy when
    that password was set.

    For example, suppose you have the following list:

    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc

    Each line gives the password policy and then the password. The password policy
    indicates the lowest and highest number of times a given letter must appear for
    the password to be valid. For example, 1-3 a means that the password must
    contain a at least 1 time and at most 3 times. In the above example, 2 passwords
    are valid. The middle password, cdefg, is not; it contains no instances of b,
    but needs at least 1. The first and third passwords are valid: they contain one
    a or nine c, both within the limits of their respective policies.

    How many passwords are valid according to their policies?


    --- Part Two ---
    While it appears you validated the passwords correctly, they don't seem to be
    what the Official Toboggan Corporate Authentication System is expecting.
    The shopkeeper suddenly realizes that he just accidentally explained the
    password policy rules from his old job at the sled rental place down the
    street! The Official Toboggan Corporate Policy actually works a little
    differently.

    Each policy actually describes two positions in the password, where 1 means
    the first character, 2 means the second character, and so on. (Be careful;
    Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of
    these positions must contain the given letter. Other occurrences of the
    letter are irrelevant for the purposes of policy enforcement.

    Given the same example list from above:

        1-3 a: abcde is valid: position 1 contains a and position 3 does not.
        1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
        2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

    How many passwords are valid according to the new interpretation of the policies?
    """

    print("\n--- DAY 2 ---")
    sum_valid_pws1 = 0
    sum_valid_pws2 = 0

    puzzle_input = open("data/day2.txt")

    for line in puzzle_input:
        parts = line.split(' ')
        constraints = parts[0].split('-')
        constraints[0] = int(constraints[0])
        constraints[1] = int(constraints[1])

        letter = parts[1].replace(":", "")
        letter_count = parts[2].count(letter)

        # PART ONE
        if letter_count >= constraints[0] and letter_count <= constraints[1]:
            sum_valid_pws1 += 1

        # PART TWO
        password = parts[2]
        if ((password[constraints[0]-1] == letter and password[constraints[1]-1] != letter) or
           (password[constraints[0]-1] != letter and password[constraints[1]-1] == letter)):
           sum_valid_pws2 += 1

    print(f"2.1. There are {sum_valid_pws1} valid passwords.")
    print(f"2.2. There are {sum_valid_pws2} valid passwords.")


def day3():
    """Day 3: Toboggan Trajectory
    With the toboggan login problems resolved, you set off toward the airport.
    While travel by toboggan might be easy, it's certainly not safe: there's
    very minimal steering and the area is covered in trees. You'll need to see
    which angles will take you near the fewest trees.

    Due to the local geology, trees in this area only grow on exact integer
    coordinates in a grid. You make a map (your puzzle input) of the open
    squares (.) and trees (#) you can see. For example:

    ..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#

    These aren't the only trees, though; due to something you read about once
    involving arboreal genetics and biome stability, the same pattern repeats
    to the right many times:

    ..##.........##.........##.........##.........##.........##.......  --->
    #...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
    .#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
    ..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
    .#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
    ..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
    .#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
    .#........#.#........#.#........#.#........#.#........#.#........#
    #.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
    #...##....##...##....##...##....##...##....##...##....##...##....#
    .#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

    You start on the open square (.) in the top-left corner and need to reach
    the bottom (below the bottom-most row on your map).

    The toboggan can only follow a few specific slopes (you opted for a cheaper
    model that prefers rational numbers); start by counting all the trees you
    would encounter for the slope right 3, down 1:

    From your starting position at the top-left, check the position that is
    right 3 and down 1. Then, check the position that is right 3 and down 1
    from there, and so on until you go past the bottom of the map.

    The locations you'd check in the above example are marked here with O where
    there was an open square and X where there was a tree:

    ..##....... ..##....... ..##.........##.........##.........##.......  --->
    #..O#...#.. #...#...#.. #...#...#..#...#...#..#...#...#..#...#...#..
    .#....X..#. .#....#..#. .#....#..#..#....#..#..#....#..#..#....#..#.
    ..#.#...#O# ..#.#...#.# ..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
    .#...##..#. .X...##..#. .#...##..#..#...##..#..#...##..#..#...##..#.
    ..#.##..... ..#.X#..... ..#.##.......#.##.......#.##.......#.##.....  --->
    .#.#.#....# .#.#.#.O..# .#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
    .#........# .#........X .#........#.#........#.#........#.#........#
    #.##...#... #.##...#... #.X#...#...#.##...#...#.##...#...#.##...#...
    #...##....# #...##....# #...#X....##...##....##...##....##...##....#
    .#..#...#.# .#..#...#.# .#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

    In this example, traversing the map using this slope would cause you to
    encounter 7 trees.

    Starting at the top-left corner of your map and following a slope of right 3
    and down 1, how many trees would you encounter?
    """

    print("\n--- DAY 3 ---")

    # Determines number of trees encountered for a given path
    def travel(right, down):
        tree_count = 0
        xpos = 0

        with open("data/day3.txt") as puzzle_input:
            for count, line in enumerate(puzzle_input, start=0):
                if count % down == 0:   # Skips lines depending on the value of down
                    if xpos > len(line)-2:
                        xpos -= len(line)-1 # Start over from the left

                    if line[xpos] == '#':
                        tree_count += 1

                    xpos += right
            return tree_count

    tree_count = travel(3, 1)
    print(f"3.1. Trees encountered: {tree_count}")


    """--- Part Two ---
    Time to check the rest of the slopes - you need to minimize the probability
    of a sudden arboreal stop, after all.

    Determine the number of trees you would encounter if, for each of the
    following slopes, you start at the top-left corner and traverse the map all
    the way to the bottom:

        Right 1, down 1.
        Right 3, down 1. (This is the slope you already checked.)
        Right 5, down 1.
        Right 7, down 1.
        Right 1, down 2.

    In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s)
    respectively; multiplied together, these produce the answer 336.

    What do you get if you multiply together the number of trees encountered on
    each of the listed slopes?
    """

    slope_1 = travel(1, 1)
    slope_2 = travel(3, 1)
    slope_3 = travel(5, 1)
    slope_4 = travel(7, 1)
    slope_5 = travel(1, 2)

    sum_tree_count = slope_1*slope_2*slope_3*slope_4*slope_5
    print(f"3.2. Trees encountered: {sum_tree_count}")





def main():
    #day1()
    #day2()
    day3()


if __name__ == "__main__":
    main()
