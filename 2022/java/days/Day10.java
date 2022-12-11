package days;

import main.Day;
import java.util.*;

public class Day10 extends Day {
    List<String> input;

    public Day10() {
        super(10);
        this.input = inputStrings();
    }


    @Override
    public Object part1() {
        int[] targets = new int[] {20, 60, 100, 140, 180, 220};
        int sum = 0, current = 0, cycle = 0, X = 1;

        for (String s : this.input) {
            String[] instr = s.split(" ");
            
            // increase cycle, continue
            if (instr[0].equals("noop")) { cycle++; continue; } 
            int value = Integer.parseInt(instr[1]);
            
            // calculate strength if target cycle reached
            if (cycle + 2 >= targets[current]) {
                sum += targets[current] * X;

                // go to next target, break if last target reached
                if (++current == targets.length) break;
            }
            
            // update register and cycles
            X += value;
            cycle += 2;
        }

        return sum;
    }


    @Override
    public Object part2() {
        int pos = 0, X = 1;
        int[] sprite = new int[] {0, 2};
        int[] pixels = new int[] {40, 6};

        StringBuilder CRT = new StringBuilder();

        for (String s : this.input) {
            String[] instr = s.split(" ");
            if (pos == 40) { CRT.append("\n"); pos = 0; }
            
            // draw pixel for one cycle
            if (instr[0].equals("noop")) {
                CRT.append(draw(pos, sprite)); pos++;
                continue;
            }
            
            // draw pixels for two cycles
            for (int c = 0; c < 2; c++) {
                CRT.append(draw(pos, sprite)); pos++;
                if (pos == 40) { CRT.append("\n"); pos = 0; }
            }
            
            // update register and cycles
            X += Integer.parseInt(instr[1]);

            // update sprite position 
            sprite[0] = X-1; sprite[1] = X+1;
        }

        return CRT;
    }


    private String draw(int pos, int[] sprite) {
        if (pos >= sprite[0] && pos <= sprite[1])
            return "#";
        return ".";
    }
}
