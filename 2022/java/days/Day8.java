package days;

import main.Day;
import java.util.*;

public class Day8 extends Day {
    List<List<Integer>> input;

    public Day8() {
        super(8);
        this.input = inputIntegerMatrix();
    }

    @Override 
    public Object part1() {
        int sum = (this.input.get(0).size() * 2);

        for (int y = 1; y < input.size()-1; y++) {
            List<Integer> row = input.get(y);
            
            for (int x = 0; x < row.size(); x++) {
                if (x == 0 || x == row.size()-1) { sum++; continue; }
                sum += treeVisible(y, x, row);
            }
        }
        return sum; 
    }


    @Override 
    public Object part2() {
        int highest = 0;

        for (int y = 1; y < input.size()-1; y++) {
            List<Integer> row = input.get(y);
            
            for (int x = 0; x < row.size(); x++) {
                if (x == 0 || x == row.size()-1) continue;
    
                int tree = row.get(x);
                int left = 1, right = 1, up = 1, down = 1;

                // left
                for (int l = x-1; l >= 0; l--) {
                    if (row.get(l) >= tree) { left = x-l; break; }
                    if (l == 0) left = x-l;
                }

                // right
                for (int r = x+1; r < row.size(); r++) {
                    if (row.get(r) >= tree) { right = r-x; break; }
                    if (r == row.size()-1) right = r-x;
                }

                //up
                for (int u = y-1; u >= 0; u--) {
                    if (this.input.get(u).get(x) >= tree) { up = y-u; break; }
                    if (u == 0) up = y-u;
                }
                
                // down
                for (int d = y+1; d < input.size(); d++) {
                    if (this.input.get(d).get(x) >= tree) { down = d-y; break; }
                    if (d == this.input.size()-1) down = d-y;
                }

                int score = left * right * up * down;
                if (score > highest) highest = score;
            }
        }

        return highest;
    }


    private int treeVisible(int y, int x, List<Integer> row) { 
        int tree = row.get(x);
        if (tree == 0) return 0;
        
        // left
        for (int l = x-1; l >= 0; l--) {
            if (row.get(l) >= tree) break;
            if (l == 0) return 1;
        }

        // right
        for (int r = x+1; r < row.size(); r++) {
            if (row.get(r) >= tree) break;
            if (r == row.size()-1) return 1;
        } 
        
        // up
        for (int u = y-1; u >= 0; u--) {
            if (this.input.get(u).get(x) >= tree) break;
            if (u == 0) return 1;
        }

        // down
        for (int d = y+1; d < input.size(); d++) {
            if (this.input.get(d).get(x) >= tree) break;
            if (d == this.input.size()-1) return 1;
        }

        // not visible
        return 0;
    }
}
