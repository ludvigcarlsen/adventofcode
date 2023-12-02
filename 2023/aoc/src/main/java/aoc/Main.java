package aoc;

import aoc.days.Day1;
import aoc.days.Day2;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Day> days = List.of(new Day1(), new Day2());
        days.forEach(System.out::println);
    }
}