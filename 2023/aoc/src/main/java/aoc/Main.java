package aoc;

import aoc.days.Day1;
import aoc.days.Day2;
import aoc.days.Day3;
import aoc.days.Day4;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Day> days = List.of(new Day1(), new Day2(), new Day3(), new Day4());
        days.forEach(System.out::println);
    }
}