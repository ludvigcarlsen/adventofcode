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


def day4():

    """Day 4: Passport Processing

    You arrive at the airport only to realize that you grabbed your North Pole
    Credentials instead of your passport. While these documents are extremely
    similar, North Pole Credentials aren't issued by a country and therefore
    aren't actually valid documentation for travel in most of the world.

    It seems like you're not the only one having problems, though; a very long
    line has formed for the automatic passport scanners, and the delay could
    upset your travel itinerary.

    Due to some questionable network security, you realize you might be able to
    solve both of these problems at the same time.

    The automatic passport scanners are slow because they're having trouble
    detecting which passports have all required fields. The expected fields are
    as follows:

        byr (Birth Year)
        iyr (Issue Year)
        eyr (Expiration Year)
        hgt (Height)
        hcl (Hair Color)
        ecl (Eye Color)
        pid (Passport ID)
        cid (Country ID)

    Passport data is validated in batch files (your puzzle input). Each passport
    is represented as a sequence of key:value pairs separated by spaces or
    newlines. Passports are separated by blank lines.

    Here is an example batch file containing four passports:

    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    byr:1937 iyr:2017 cid:147 hgt:183cm

    iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    hcl:#cfa07d byr:1929

    hcl:#ae17e1 iyr:2013
    eyr:2024
    ecl:brn pid:760753108 byr:1931
    hgt:179cm

    hcl:#cfa07d eyr:2025 pid:166559648
    iyr:2011 ecl:brn hgt:59in

    The first passport is valid - all eight fields are present. The second
    passport is invalid - it is missing hgt (the Height field).

    The third passport is interesting; the only missing field is cid, so it
    looks like data from North Pole Credentials, not a passport at all! Surely,
    nobody would mind if you made the system temporarily ignore missing cid
    fields. Treat this "passport" as valid.

    The fourth passport is missing two fields, cid and byr. Missing cid is fine,
    but missing any other field is not, so this passport is invalid.

    According to the above rules, your improved system would report 2 valid passports.
    Count the number of valid passports - those that have all required fields.
    Treat cid as optional. In your batch file, how many passports are valid?
    """


    """--- Part Two ---
    The line is moving more quickly now, but you overhear airport security
    talking about how passports with invalid data are getting through. Better
    add some data validation, quick!

    You can continue to ignore the cid field, but each other field has strict
    rules about what values are valid for automatic validation:

        byr (Birth Year) - four digits; at least 1920 and at most 2002.
        iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        hgt (Height) - a number followed by either cm or in:
            If cm, the number must be at least 150 and at most 193.
            If in, the number must be at least 59 and at most 76.
        hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        pid (Passport ID) - a nine-digit number, including leading zeroes.
        cid (Country ID) - ignored, missing or not.

    Your job is to count the passports where all required fields are both
    present and valid according to the above rules. Here are some example
    values:

    byr valid:   2002
    byr invalid: 2003

    hgt valid:   60in
    hgt valid:   190cm
    hgt invalid: 190in
    hgt invalid: 190

    hcl valid:   #123abc
    hcl invalid: #123abz
    hcl invalid: 123abc

    ecl valid:   brn
    ecl invalid: wat

    pid valid:   000000001
    pid invalid: 0123456789

    Here are some invalid passports:

    eyr:1972 cid:100
    hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

    iyr:2019
    hcl:#602927 eyr:1967 hgt:170cm
    ecl:grn pid:012533040 byr:1946

    hcl:dab227 iyr:2012
    ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

    hgt:59cm ecl:zzz
    eyr:2038 hcl:74454a iyr:2023
    pid:3556412378 byr:2007

    Here are some valid passports:

    pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
    hcl:#623a2f

    eyr:2029 ecl:blu cid:129 byr:1989
    iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

    hcl:#888785
    hgt:164cm byr:2001 iyr:2015 cid:88
    pid:545766238 ecl:hzl
    eyr:2022

    iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719

    Count the number of valid passports - those that have all required fields
    and valid values. Continue to treat cid as optional. In your batch file,
    how many passports are valid?
    """


    print("\n--- DAY 4 ---")

    passport_data = set() # Stores all lines of data for a given passport

    def check_hgt(value):
        height = 0
        if (value[:-2]).isnumeric():
            height = int(value[:-2])

        if value[-1] == 'm':
            if height < 150 or height > 193:
                return False

        elif value[-1] == 'n':
            if height < 59 or height > 76:
                return False

        else:
            return False
        return True


    def check_hcl(value):
        valid_letters = {'a','b','c','d','e','f'}

        if value[0] != '#' or len(value) != 7:
            return False

        else:
            for char in value[1:]:
                if char.isnumeric() or char in valid_letters:
                    continue
                else:
                    return False
            return True


    def check_ecl(ecl):
        valid_ecls = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
        if ecl in valid_ecls:
            return True
        return False


    def check_pid(pid):
        if pid.isnumeric() and len(pid) == 9:
            return True
        return False


    def check_value(value, min, max):
        value = int(value)
        if value < min or value > max:
            return False
        return True

    # Switch case for data type
    def validate_data(data):
        valid = True
        temp  = data.split(':')
        key   = temp[0]
        value = temp[1]

        if   key == 'byr':
            valid = check_value(value, 1920, 2002)
        elif key == 'iyr':
            valid = check_value(value, 2010, 2020)
        elif key == 'eyr':
            valid = check_value(value, 2020, 2030)
        elif key == 'hgt':
            valid = check_hgt(value)
        elif key == 'hcl':
            valid = check_hcl(value)
        elif key == 'ecl':
            valid = check_ecl(value)
        elif key == 'pid':
            valid = check_pid(value)

        return valid

    # Help function to loop through every piece of passport data
    def validate_values():
        for data in passport_data:
            if validate_data(data):
                continue
            else:
                return 0
        return 1

    # Main function. Determines validity of passport by keys (4.1),
    # then by data if keys are valid
    def validate_passports():
        valid_passports_1 = 0 # 4.1 - Valid passports by key
        valid_passports_2 = 0 # 4.2 - Valid passports by key and value

        with open("data/day4.txt") as puzzle_input:
            lines = puzzle_input.readlines()
            for line in lines:
                parts = line.split()

                if (line is lines[-1]):
                    passport_data.update(parts)

                if (len(parts) == 0 or line is lines[-1]): # No more passport data
                    if (len(passport_data) == 8):
                        valid_passports_1 += 1
                        valid_passports_2 += validate_values() # Further eval

                    elif (len(passport_data) == 7):
                        valid = True
                        for x in passport_data:
                            key = x.split(':')
                            if key[0] == "cid":
                                valid = False
                                break
                        if valid:
                            valid_passports_1 += 1
                            valid_passports_2 += validate_values()

                    passport_data.clear()

                else: # Add passport data
                    passport_data.update(parts)

        print(f"4.1. There are {valid_passports_1} valid passports.")
        print(f"4.2. There are {valid_passports_2} valid passports.")

    validate_passports()


def main():
    #day1()
    #day2()
    #day3()
    day4()


if __name__ == "__main__":
    main()
