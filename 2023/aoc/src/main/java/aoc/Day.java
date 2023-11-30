package aoc;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.List;

public abstract class Day {
    private Integer day;

    public Day(Integer day) {
        this.day = day;
    }

    public abstract Object task1();
    public abstract Object task2();

    public List<String> readFile() {
        ClassLoader classLoader = getClass().getClassLoader();
        File file = new File(classLoader.getResource("data/day%s.txt".formatted(day)).getFile());
        try {
            return Files.readAllLines(file.toPath());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public String toString() {
        return "%s\n%s\n".formatted(task1(), task2());
    }
}
