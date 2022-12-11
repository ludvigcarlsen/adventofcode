package days;

import main.Day;
import java.util.*;

public class Day9 extends Day {
    List<String> input;
    Map<Character, int[]> directions;
    
    public Day9() {
        super(9);
        this.input = inputStrings();
        this.directions = Map.of(
        // DIRECTION         X  Y
            'L', new int[] {-1, 0},
            'R', new int[] { 1, 0},
            'U', new int[] { 0, 1},
            'D', new int[] { 0,-1}
        );
    }
    
    @Override
    public Object part1() {
        Set<List<Integer>> visited = new HashSet<List<Integer>>();
        int hx = 0, hy = 0; // head current
        int px = 0, py = 0; // head previous
        int tx = 0, ty = 0; // tail

        for (String move : this.input) {
            int steps = Integer.parseInt(move.substring(2, move.length()));
            int[] offsets = this.directions.get(move.charAt(0));
              
            for (int i = 0; i < steps; i++) {
                hx += offsets[0]; hy += offsets[1]; // Update head
                if (Math.abs(hx - tx) > 1 || Math.abs(hy - ty) > 1) {
                    tx = px; ty = py; // Update tail if no longer adjacent
                }
                px = hx; py = hy;
                visited.add(Arrays.asList(tx, ty)); // Add tail if new position
            }
        }

        return visited.size();
    }


    @Override
    public Object part2() {
        Set<List<Integer>> visited = new HashSet<List<Integer>>();
        int[][] knots = new int[10][2];

        for (String move : this.input) {
            int steps = Integer.parseInt(move.substring(2, move.length()));
            int[] offsets = this.directions.get(move.charAt(0));
              
            for (int i = 0; i < steps; i++) {

                // update head
                knots[0][0] += offsets[0]; knots[0][1] += offsets[1];
                
                // Update knots
                for (int k = 1; k < knots.length; k++) {
                    
                    int diffx = knots[k-1][0] - knots[k][0];
                    int diffy = knots[k-1][1] - knots[k][1];
                    int absx = Math.abs(diffx);
                    int absy = Math.abs(diffy);
                    
                    // knots are adjacent, no need to update further
                    if (absx < 2 && absy < 2) break;
                    
                    // move directly left, right, up or down
                    if (absx + absy == 0 && (absx == 2 || absy == 2)) {
                        knots[k][0] += offsets[0]; knots[k][1] += offsets[1];
                    }
                    
                    // move diagonally towards knot ahead
                    else if (absx == 2 || absy == 2) {
                         int offx = (int)Math.signum(diffx);
                         int offy = (int)Math.signum(diffy);
                         knots[k][0] += offx;
                         knots[k][1] += offy;
                    }
                }

                visited.add(Arrays.asList(knots[9][0], knots[9][1]));
            }
        }

        return visited.size();
    }
}




