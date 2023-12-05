package aoc.days;

import aoc.Day;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Day5 extends Day {
    List<String> data;
    List<ResourceMap> resources;

    public Day5() {
        super(5, "If You Give A Seed A Fertilizer");
        this.data = readFile();
        this.resources = parseResources();
    }

    @Override
    public Object task1() {
        List<Long> seeds = Arrays.stream(data.get(0).split(":")[1].trim().split(" ")).map(Long::parseLong).toList();
        List<Long> locations = seeds.stream().map(s -> getLocation(resources, s)).toList();
        return Collections.min(locations);
    }

    @Override
    public Object task2() {
        Long lowestLocation = Long.MAX_VALUE;
        List<Long> seeds = Arrays.stream(data.get(0).split(":")[1].trim().split(" ")).map(Long::parseLong).toList();
        for (int i = 0; i < seeds.size(); i+=2) {
            Long seedStart = seeds.get(i);
            Long range = seeds.get(i+1);

            for (Long j = seedStart; j < seedStart + range; j++) {
                lowestLocation = Math.min(lowestLocation, getLocation(resources, j));
            }
        }
        return lowestLocation;
    }


    private List<ResourceMap> parseResources() {
        List<ResourceMap> resources = new ArrayList<>(7);
        List<ResourceMapEntry> currentEntries = new ArrayList<>();
        int resourceIndex = 0;

        for (int i = 3; i < data.size(); i++) {
            String line = data.get(i);

            if (!line.isEmpty() || i == data.size()-1) {
                List<Long> entryData = Arrays.stream(line.split(" ")).map(Long::parseLong).toList();
                currentEntries.add(new ResourceMapEntry(entryData));
            }

            if (line.isEmpty() || i == data.size()-1) {
                resources.add(resourceIndex, new ResourceMap(new ArrayList<>(currentEntries)));
                currentEntries.clear();
                i ++; resourceIndex++;
            }
        }
        return resources;
    }

    private Long getLocation(List<ResourceMap> resources, Long seed) {
        Long currentSource = seed;

        for (ResourceMap r : resources) {
            currentSource = r.get(currentSource);
        }
        return currentSource;
    }

    private class ResourceMap {
        List<ResourceMapEntry> entries;

        public ResourceMap(List<ResourceMapEntry> entries) {
            this.entries = entries;
        }

        public Long get(Long source) {
            for (ResourceMapEntry e : entries) {
                if (e.isMapped(source)) return e.get(source);
            }
            return source;
        }
    }

    private static class ResourceMapEntry {
        Long destinationRangeStart;
        Long sourceRangeStart;
        Long sourceRangeEnd;
        Long rangeLength;
        Long difference;

        public ResourceMapEntry(List<Long> entryData) {
            this.destinationRangeStart = entryData.get(0);
            this.sourceRangeStart = entryData.get(1);
            this.rangeLength = entryData.get(2);
            this.sourceRangeEnd = sourceRangeStart + rangeLength;
            this.difference = sourceRangeStart - destinationRangeStart;
        }

        boolean isMapped(Long source) {
            return source >= sourceRangeStart && source <= sourceRangeEnd;
        }

        public Long get(Long source) {
            if (isMapped(source)) {
                return source - difference;
            }
            return source;
        }
    }
}
