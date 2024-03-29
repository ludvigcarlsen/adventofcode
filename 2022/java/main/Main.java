package main;

import days.*;
import java.util.*;

public class Main {    
    public static void main(String[] args) {
        List<Day> days = Arrays.asList (
                new Day1(),
                new Day2(),
                new Day3(),
                new Day4(),
                new Day5(),
                new Day6(),
                new Day7(),
                new Day8(),
                new Day9(),
                new Day10()
        );

        for (Day day : days) {
            System.out.println(String.format("Day %s:", day.day));
            day.printParts();
            System.out.println();
        }
    }    
}





