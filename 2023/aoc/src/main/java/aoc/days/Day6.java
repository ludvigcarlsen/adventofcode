package aoc.days;

import aoc.Day;

import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

public class Day6 extends Day {
    List<String> data = readFile();

    public Day6() {
        super(6, "Wait For It");
    }

    @Override
    public Object task1() {
        List<Integer> times = Arrays.stream(data.getFirst().split(":")[1].trim().split("\\s+")).map(Integer::parseInt).toList();
        List<Integer> distances = Arrays.stream(data.getLast().split(":")[1].trim().split("\\s+")).map(Integer::parseInt).toList();
        List<Race> races = IntStream.range(0, times.size()).mapToObj(i -> new Race(times.get(i), distances.get(i))).toList();

        int sum = 1;

        for (Race race : races) {
            int numWays = 0;
            int holdTime = (int) Math.ceil((double) race.time / 2);

            while (holdTime * (race.time - holdTime) > race.distance) {
                numWays++; holdTime++;
            }
            sum *= numWays * 2 - ((race.time % 2 != 0) ? 0 : 1);
        }
        return sum;
    }

    @Override
    public Object task2() {
        long raceTime = Long.parseLong(data.getFirst().split(":")[1].replaceAll("\\s", ""));
        long raceDistance = Long.parseLong(data.getLast().split(":")[1].replaceAll("\\s", ""));

        int numWays = 0;
        long holdTime = (long) Math.ceil((double) raceTime / 2);

        while (holdTime * (raceTime - holdTime) > raceDistance) {
            numWays++; holdTime++;
        }
        return numWays * 2 - ((raceTime % 2 != 0) ? 0 : 1);
    }

    private record Race(int time, int distance) {}
}
