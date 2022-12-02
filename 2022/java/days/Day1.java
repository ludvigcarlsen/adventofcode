package days;

import main.Day;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;


public class Day1 extends Day {
    ArrayList<Integer> input;

    public Day1() {
        super(1);
        input = this.inputSumBlanks();
        input.sort(Collections.reverseOrder());
    }

    @Override
    public Object part1() {
        return input.get(0);
    }


    @Override
    public Object part2() {
        int calories = 0;

        for (int i = 0; i < 3; i++) {
            calories += input.get(i);
        }

        return calories; 
    }
}

        
