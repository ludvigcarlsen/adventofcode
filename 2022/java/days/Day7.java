package days;

import main.Day;
import java.util.*;

public class Day7 extends Day {
    List<String> input;
    Dir root;

    public Day7() {
        super(7);
        this.input = inputStrings();
        this.root = new Dir("/", null);
    }

    @Override
    public Object part1() {
        Dir current = this.root;
        
        for (int i = 1; i < input.size(); i++) {
            String[] parts = input.get(i).split(" ");
            
            // Change directory
            if (parts[1].equals("cd")) 
                current = current.cd(parts[2]);
            
            // list content, does nothing
            else if (parts[1].equals("ls")) 
                continue;
            
            // Add directory to current
            else if (parts[0].equals("dir"))
                current.addDir(new Dir(parts[1], current));
            
            // Add file to current
            else current.addFile(parts[1], Integer.parseInt(parts[0]));
        }

        // sum directories with total size less than 100000
        return root.sumLessthan(100000);
    }


    @Override
    public Object part2() {
        Dir current = this.root;

        int total     = 70000000;
        int required  = 30000000;
        int unused    = total - root.totalSize();
        int remainder = required - unused;
        
        // get size of directory closest to, but greater than remaining space
        return root.closestTo(remainder, total);
    }


    private class Dir {
        String id;
        Dir parent;
        ArrayList<Dir> subs;
        HashMap<String, Integer> files;

        public Dir(String id, Dir parent) {
            this.id = id;
            this.parent = parent;
            this.subs = new ArrayList<Dir>();
            this.files = new HashMap<String, Integer>();
        }

        public String getId() { return this.id; } 

        public Dir getParent() { return this.parent; }

        public ArrayList<Dir> subs() { return this.subs; }

        public void addDir(Dir d) {
            this.subs.add(d);
        }

        public void addFile(String id, int size) {
            this.files.put(id, size); 
        }

        private Dir cd(String arg) {
            if (arg.equals("..")) return this.getParent();
            else return this.findSub(arg);
        }

        public Dir findSub(String id) {
            for (Dir d : this.subs) {
                if (d.getId().equals(id)) return d;
            }
            return null;
        }

        public int localSize() {
            int size = 0;
            for (String id : this.files.keySet()) {
                size += this.files.get(id);
            }
            return size;
        }

        public int totalSize() {
            int size = this.localSize();

            for (Dir sub : this.subs) {
                size += sub.totalSize();
            }
            return size;
        }

        /* Task 1 */
        public int sumLessthan(int target) {
            int size = this.totalSize();
            if (size > target) size = 0;

            for (Dir s : this.subs) {
                size += s.sumLessthan(target);
            }
            return size;
        }

        /* Task 2 */
        public int closestTo(int target, int record) {
            int size = this.totalSize();

            if (size >= target && size < record)
                record = size;

            for (Dir s : this.subs) {
                record = s.closestTo(target, record);
            }
            return record;
        }
    }
}
