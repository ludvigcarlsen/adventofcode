package aoc.days;

import aoc.Day;

import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day1 extends Day {
    private final List<String> data = readFile();

    public Day1() {
        super(1, "Trebuchet?!");
    }

    @Override
    public Object task1() {
        int sum = 0;

        for (String line : data) {
            char[] digits = line.replaceAll("\\D", "").toCharArray();
            sum += Integer.parseInt(digits[0] + "" + digits[digits.length-1]);
        }

        return sum;
    }

    @Override
    public Object task2() {
        int sum = 0;

        Map<String, String> wordToDigit = Map.of("one", "1", "two", "2", "three", "3", "four", "4", "five", "5", "six", "6", "seven", "7", "eight", "8", "nine", "9");
        Map<String, String> wordToDigitReversed = Map.of("eno", "1", "owt", "2", "eerht", "3", "ruof", "4", "evif", "5", "xis", "6", "neves","7", "thgie", "8", "enin", "9");

        String r1 = String.join("|", wordToDigit.keySet()) + "|\\d";
        String r2 = String.join("|", wordToDigitReversed.keySet()) + "|\\d";

        Pattern p1 = Pattern.compile(r1);
        Pattern p2 = Pattern.compile(r2);

        for (String line : data) {
            Matcher m1 = p1.matcher(line);
            Matcher m2 = p2.matcher(new StringBuilder(line).reverse().toString());

            String digitOrLetter1 = null;
            String digitOrLetter2 = null;

            if (m1.find()) { digitOrLetter1 = m1.group(); }
            if (m2.find()) { digitOrLetter2 = m2.group(); }

            String digit1 = wordToDigit.getOrDefault(digitOrLetter1, digitOrLetter1);
            String digit2 = wordToDigitReversed.getOrDefault(digitOrLetter2, digitOrLetter2);

            sum += Integer.parseInt(digit1 + digit2);
        }
        return sum;
    }
}
