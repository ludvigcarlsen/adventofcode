package aoc.days;

import aoc.Day;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day3 extends Day {
    List<String> data = readFile();
    char[][] schematic = parseData(data);

    public Day3() {
        super(3, "Gear Ratios");
    }

    @Override
    public Object task1() {
        int sum = 0;
        List<Entry> entries = new ArrayList<>();
        Pattern p = Pattern.compile("\\d+");

        for (int i = 0; i < data.size(); i++) {
            Matcher m = p.matcher(data.get(i));

            while (m.find()) {
                entries.add(new Entry(Integer.parseInt(m.group()), i, m.start(), m.end()-1));
            }
        }

        for (var entry : entries) {
            if (isAdjacentToSymbol(entry)) {
                sum += entry.value;
            }
        }

        return sum;
    }

    @Override
    public Object task2() {

        Map<Pair, ArrayList<Integer>> potentialGears = new HashMap<>();
        List<Entry> entries = new ArrayList<>();
        Pattern p = Pattern.compile("\\d+");

        for (int i = 0; i < data.size(); i++) {
            Matcher m = p.matcher(data.get(i));

            while (m.find()) {
                entries.add(new Entry(Integer.parseInt(m.group()), i, m.start(), m.end()-1));
            }
        }

        for (var entry : entries) {
            List<Pair> asterisks = getAdjacentAsterisks(entry);

            for(Pair asterisk : asterisks) {
                potentialGears.computeIfAbsent(asterisk, k -> new ArrayList<>()).add(entry.value);
            }
        }

        return potentialGears.values().stream()
                .filter(g -> g.size() == 2)
                .mapToLong(entry -> entry.get(0) * entry.get(1))
                .sum();
    }

    char[][] parseData(List<String> data) {
        char[][] matrix = new char[data.get(0).length()][data.size()];

        for (int i = 0; i < data.size(); i++) {
            String line = data.get(i);
            matrix[i] = line.toCharArray();
        }

        return matrix;
    }

    private boolean isAdjacentToSymbol(Entry entry) {
        for (int x = Math.max(0, entry.row-1); x <= Math.min(data.size()-1, entry.row+1); x++) {
            for (int y = Math.max(0, entry.xStart-1); y <= Math.min(data.get(0).length()-1, entry.xEnd+1); y++) {
                if (isSymbol(schematic[x][y])) {
                    return true;
                }
            }
        }
        return false;
    }

    private List<Pair> getAdjacentAsterisks(Entry entry) {
        List<Pair> asterisks = new ArrayList<>();

        for (int x = Math.max(0, entry.row-1); x <= Math.min(data.size()-1, entry.row+1); x++) {
            for (int y = Math.max(0, entry.xStart-1); y <= Math.min(data.get(0).length()-1, entry.xEnd+1); y++) {
                if (isGear(schematic[x][y])) {
                    asterisks.add(new Pair(x, y));
                }
            }
        }
        return asterisks;
    }

    private boolean isSymbol(char c) {
        return c != '.' && !Character.isDigit(c);
    }

    private boolean isGear(char c) {
        return c == '*';
    }

    private record Entry(int value, int row, int xStart, int xEnd) {}
    private record Pair(int x, int y) {}
}
