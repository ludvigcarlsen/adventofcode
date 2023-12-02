package aoc.days;

import aoc.Day;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Day2 extends Day {
    private final List<String> data = readFile();

    public Day2() {
        super(2, "Cube Conundrum");
    }

    @Override
    public Object task1() {
        int sum = 0;

        for (String record : data) {
            String[] s = record.split(":");
            String[] sets = s[1].split(";");

            for (int i = 0; i < sets.length; i++) {
                String set = sets[i];
                String[] colors = set.split(",");

                Map<String, Integer> cubes = new HashMap<>(Map.of("red", 0, "green", 0, "blue", 0));

                for (String color : colors) {
                    String[] s1 = color.trim().split(" ");
                    cubes.put(s1[1], cubes.get(s1[1]) + Integer.parseInt(s1[0]));
                }

                if (cubes.get("red") > 12 || cubes.get("green") > 13 || cubes.get("blue") > 14) {
                    break;
                }

                if (i == sets.length-1) {
                    int gameId = Integer.parseInt(s[0].split(" ")[1]);
                    sum += gameId;
                }
            }
        }
        return sum;
    }

    @Override
    public Object task2() {
        int sum = 0;

        for (String record : data) {
            String[] s = record.split(":");
            String[] sets = s[1].split(";");

            Map<String, Integer> cubes = new HashMap<>(Map.of("red", 0, "green", 0, "blue", 0));

            for (String set : sets) {
                String[] colors = set.split(",");

                for (String color : colors) {
                    String[] s1 = color.trim().split(" ");
                    cubes.put(s1[1], Math.max(cubes.get(s1[1]), Integer.parseInt(s1[0])));
                }
            }

            sum += cubes.values().stream().reduce(1, (a, b) -> a * b);
        }
        return sum;
    }
}
