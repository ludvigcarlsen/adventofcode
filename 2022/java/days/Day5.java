package days;

import main.Day;
import java.util.*;
import java.util.stream.Collectors;

public class Day5 extends Day {
    ArrayList<List<String>> input;
    ArrayList<Stack<Character>> stacks;
    ArrayList<int[]> moves;

    public Day5() {
        super(5);
        this.input = inputStringsBlanks();
        this.stacks = initStacks(this.input.get(0));
        this.moves = extractMoves(this.input.get(1));
    }

    @Override
    public Object part1() {
        ArrayList<Stack<Character>> stacks1 = copyStacks();
        String topCrates = "";

        for (int[] move : this.moves) {
            int crates = move[0];
            int from = move[1];
            int to = move[2];
            
            // Rearrange crates according to moves
            for (int i = 0; i < crates; i++) {
                char c = stacks1.get(from).pop();
                stacks1.get(to).push(c);
            }
        }
        
        // Get crate on top of each stack, skip if stack if empty
        for (Stack<Character> s : stacks1) {
            if (s.empty()) continue;
            topCrates += s.peek();
        }

        return topCrates;
    }


    @Override 
    public Object part2() {
        ArrayList<Stack<Character>> stacks2 = copyStacks();
        Stack<Character> order = new Stack<>();
        String topCrates = "";

        for (int[] move : this.moves) {
            int crates = move[0];
            int from = move[1];
            int to = move[2];
            
            // Pop crates to temporary stack
            for (int i = 0; i < crates; i++) 
                order.push(stacks2.get(from).pop());
            
            // Push temporary to new location
            for (int i = 0; i < crates; i++) 
                stacks2.get(to).push(order.pop());
        }
        
        // Get crate on top of each stack, skip if stack if empty
        for (Stack<Character> s : stacks2) {
            if (s.empty()) continue;
            topCrates += s.peek();
        }

        return topCrates;
    }

    
    private ArrayList<Stack<Character>> initStacks(List<String> raw) {
        ArrayList<Stack<Character>> stacks = new ArrayList<Stack<Character>>();

        // total number of stacks
        int count = raw.get(0).length() / 3; 
       
        // Initialize stacks
        for (int i = 0; i < count; i++) {
           Stack<Character> s = new Stack<>();
           stacks.add(s);
        }
        
        // Loop through every row of crates, starting from bottom
        for (int i = raw.size()-2; i >= 0; i--) {
            String crates = raw.get(i);
            
            // Push crate as character to respective stack
            int stackNr = 0;
            for (int j = 1; j < crates.length(); j+=4) {
                char crate = crates.charAt(j);

                // No crate on current stack, continue
                if (crate == ' ') { stackNr++; continue; }
                stacks.get(stackNr).push(crates.charAt(j));
                stackNr++;
            }
        }

        return stacks;
    }


    private ArrayList<int[]> extractMoves(List<String> raw) {
        ArrayList<int[]> moves = new ArrayList<int[]>();

        for (String s : raw) {
            String[] parts = s.split(" ");
            
            // Parse to int and zero-index stack nrs for convenience
            int m1 = Integer.parseInt(parts[1]);
            int m2 = Integer.parseInt(parts[3]) -1;
            int m3 = Integer.parseInt(parts[5]) -1;
            int[] move = {m1, m2, m3};
            moves.add(move);
        }
        
        return moves;
    }


    private ArrayList<Stack<Character>> copyStacks() {
        ArrayList<Stack<Character>> copy = new ArrayList<>();
        
        for (Stack s : this.stacks) {
            Stack<Character> n = new Stack<Character>();
            n.addAll(s);
            copy.add(n);
        }
        return copy;
    }
}
