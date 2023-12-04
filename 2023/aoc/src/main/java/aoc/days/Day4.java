package aoc.days;

import aoc.Day;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Day4 extends Day {
    List<String> data = readFile();

    public Day4() {
        super(4, "Scratchcards");
    }

    @Override
    public Object task1() {
        int sum = 0;

        for (String game : data) {
            long matches = getMatches(game);
            sum += (int) Math.pow(2, matches-1);
        }
        return sum;
    }

    @Override
    public Object task2() {
        Map<Integer, Integer> gameCopies = new HashMap<>();
        int currentCard = 1;

        for (String game : data) {
            long matches = getMatches(game);
            Integer currentGameCopies = gameCopies.getOrDefault(currentCard, 0);

            for (int i = ++currentCard; i < matches + currentCard; i++) {
                Integer g = gameCopies.getOrDefault(i, 0);
                gameCopies.put(i, g + 1 + currentGameCopies);
            }
        }
        return gameCopies.values().stream().mapToInt(Integer::intValue).sum() + data.size();
    }

    private long getMatches(String game) {
        String[] s1 = game.split(":");
        String[] numbers = s1[1].split("\\|");

        List<Integer> winningNumbers = Arrays.stream(numbers[0].trim().split("\\s+")).map(Integer::parseInt).toList();
        List<Integer> yourNumbers = Arrays.stream(numbers[1].trim().split("\\s+")).map(Integer::parseInt).toList();
        return winningNumbers.stream().filter(yourNumbers::contains).count();
    }
}
