package main;

import java.util.*;
import java.nio.file.*;
import java.io.File;
import java.io.FileNotFoundException;

public abstract class Day {
    protected final int day;
    protected final List<String> input;

    public Day(int day) {
        this.day = day;
        this.input = this.inputStrings();
    }

    public Object part1() {
        return null;
    }
    
    public Object part2() {
        return null;
    }

    public void printParts() {
        System.out.println(this.part1());
        System.out.println(this.part2());
    }
    
    protected List<String> inputStrings() {
        List<String> data = null;
        String path = String.format("main/data/day%s.txt", this.day);

        try {
            Path p = Paths.get(path);
            data = Files.readAllLines(p);
        }

        catch (Exception e) { e.printStackTrace(); }
        return data;
    }


    protected ArrayList<Integer> inputIntegers() {
        ArrayList<Integer> data = new ArrayList<Integer>();
            
        for (String s : this.input) {
            try { data.add(Integer.parseInt(s)); }
            catch (NumberFormatException e) { }
        }

        return data;
    }


    protected ArrayList<Integer> inputSumBlanks() {
        ArrayList<Integer> data = new ArrayList<Integer>();
        int sum = 0;

        for (String s : this.input) {
            try { sum += Integer.parseInt(s); }

            catch (NumberFormatException e) {
                data.add(sum);
                sum = 0;
            }
        }

        return data;
    }
}
