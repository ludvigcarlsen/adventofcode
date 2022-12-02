package days;

import main.Day;
import java.util.*;

public class Day2 extends Day {
    List<String> input;

    public Day2() {
        super(2);
        input = this.inputStrings();
    }
    

    @Override
    public Object part1() {
        Map<String, Integer> scoreMap = Map.of(
             // 0: loss
             "B X", 1, // 1 rock
             "C Y", 2, // 2 paper
             "A Z", 3, // 3 scissors 

             // 3: draw 
             "A X", 4, // 1 rock
             "B Y", 5, // 2 paper
             "C Z", 6, // 3 scissors 

             // 6: win
             "C X", 7, // 1 rock
             "A Y", 8, // 2 paper
             "B Z", 9  // 3 scissors
        );

        int score = 0;
        for (String round : input) {
            score += scoreMap.get(round);
        }

        return score;
    }



    public Object part2() {
        Map<String, Integer> scoreMap = Map.of(
             // 0: must lose
             "B X", 1, // 1: rock 
             "C X", 2, // 2: paper 
             "A X", 3, // 3: scissors

             // 3: must draw
             "A Y", 4, // 1: rock
             "B Y", 5, // 2: paper
             "C Y", 6, // 3: Scissors

             // 6: must win
             "C Z", 7, // 1: rock
             "A Z", 8, // 2: paper 
             "B Z", 9  // 3: scissors
        );

        int score = 0;
        for (String round : input) {
            score += scoreMap.get(round);
        }

        return score;
    }
}
