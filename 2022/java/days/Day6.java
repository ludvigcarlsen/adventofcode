package days;

import main.Day;
import java.util.*;

public class Day6 extends Day {
    String input;

    public Day6() {
        super(6);
        input = this.inputSingleString();
    }

    @Override
    public Object part1() {
        int markerSize = 4;

        for (int i = 0; i < input.length(); i++) {
            char[] seq = input.substring(i, i+markerSize).toCharArray();
            Arrays.sort(seq);
            
            for (int j = 1; j < seq.length; j++) {
                if (seq[j-1] == seq[j]) break;
                if (j == seq.length-1) return i+markerSize;
            }
        }

        return 0;
    }

    @Override
    public Object part2() {
        int markerSize = 14;

        for (int i = 0; i < input.length(); i++) {
            char[] seq = input.substring(i, i+markerSize).toCharArray();
            Arrays.sort(seq);
            
            for (int j = 1; j < seq.length; j++) {
                if (seq[j-1] == seq[j]) break;
                if (j == seq.length-1) return i+markerSize;
            }
        }

        return 0;
    }
}
