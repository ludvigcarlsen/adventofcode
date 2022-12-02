package main;

import java.util.*;
import java.nio.file.*;
import java.io.File;
import java.io.FileNotFoundException;

public abstract class Day {
    protected final int day;
    protected final String inputPath;

    public Day(int day) {
        this.day = day;
        this.inputPath = String.format("main/data/day%s.txt", day);
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

        try {
            Path p = Paths.get(this.inputPath);
            data = Files.readAllLines(p);
        }

        catch (Exception e) { e.printStackTrace(); }
        return data;
    }


    protected ArrayList<Integer> inputIntegers() {
        List<String> raw = this.inputStrings();
        ArrayList<Integer> data = new ArrayList<Integer>();
            
        for (String s : raw) {
            try { data.add(Integer.parseInt(s)); }
            catch (NumberFormatException e) { }
        }

        return data;
    }


    protected ArrayList<Integer> inputSumBlanks() {
        List<String> raw = this.inputStrings();
        ArrayList<Integer> data = new ArrayList<Integer>();
        int sum = 0;

        for (String s : raw) {
            try { sum += Integer.parseInt(s); }

            catch (NumberFormatException e) {
                data.add(sum);
                sum = 0;
            }
        }

        return data;
    }


    protected Scanner getInput() {
        Scanner s = null;
        try {
            s = new Scanner(new File(this.inputPath));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        return s;
    }
}
