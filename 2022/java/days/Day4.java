package days;

import main.Day;
import java.util.*;

public class Day4 extends Day {
    List<String> input;

    public Day4() {
        super(4);
        input = this.inputStrings();
    }

    @Override
    public Object part1() {
        int sum = 0;

        for (String s : input) {
            String[] sections = s.split(",");
            String[] range1 = sections[0].split("-"); 
            String[] range2 = sections[1].split("-");
            
            int min1 = Integer.parseInt(range1[0]);    
            int max1 = Integer.parseInt(range1[1]);
            int min2 = Integer.parseInt(range2[0]);
            int max2 = Integer.parseInt(range2[1]);

            if      (min1 >= min2 && max1 <= max2) sum += 1;
            else if (min2 >= min1 && max2 <= max1) sum += 1;

        }

        return sum;
    }

    @Override
    public Object part2() {
        int sum = 0;

        for (String s : input) {
            String[] sections = s.split(",");
            String[] range1 = sections[0].split("-");
            String[] range2 = sections[1].split("-");
            
            int min1 = Integer.parseInt(range1[0]);    
            int max1 = Integer.parseInt(range1[1]);
            int min2 = Integer.parseInt(range2[0]);
            int max2 = Integer.parseInt(range2[1]);

            if ((min1 >= min2 && min1 <= max2) || (max1 >= min2 && max1 <= max2))
                sum += 1;

            else if ((min2 >= min1 && min2 <= max1) || (max2 >= min1 && max2 <= max1))
                sum += 1;
        }

        return sum;
    }
}
