package aoc;

import aoc.days.*;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Day> days = List.of(
        //        new Day1(),
        //        new Day2(),
        //        new Day3(),
        //        new Day4(),
        //        new Day5(),
                new Day6()
        );
        days.forEach(System.out::println);
    }
}