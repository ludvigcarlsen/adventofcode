package days;

import main.Day;
import java.util.*;

public class Day3 extends Day {
    List<String> input;

    public Day3() {
        super(3);
        input = this.inputStrings();
    }

    @Override
    public Object part1() {
        int sum = 0;

        for (String sack : input) {
            int priority = 0;
            int size = sack.length();
            char common = '\0';

            String comp1 = sack.substring(0, size/2);
            String comp2 = sack.substring(size/2, size);
           
            for (int i = 0; i < size; i++) {
                char item = comp2.charAt(i);

                if (comp1.contains("" + item)) {
                    common = item;
                    break;
                }
            }

            if (Character.isUpperCase(common)) priority = common - 38;
            else priority = common - 96;            
            sum += priority;
        }

        return sum;
    }


    @Override
    public Object part2() {
        int sum = 0;

        for (int i = 0; i < input.size(); i+=3) {
            int priority = 0;
            char common = '\0';

            String sack1 = input.get(i);
            String sack2 = input.get(i+1);
            String sack3 = input.get(i+2);

            for (int j = 0; j < sack1.length() ; j++) {
                String item = "" + sack1.charAt(j);

                if (sack2.contains(item) && sack3.contains(item)) {
                    common = sack1.charAt(j);
                    break;
                }
            }

            if (Character.isUpperCase(common)) priority = common - 38;
            else priority = common - 96;            
            sum += priority;
        }

        return sum;
    }
}
