from dataclasses import dataclass


def day5():
    print("=== Day 5: Scratchcards ===")
    with open("input/day5.txt") as f:
        data = f.read().replace("\r\n", "\n")

    seeds = list(parse_seeds(data))
    maps = list(parse_maps(data))

    print("-- Part 1: --")
    lowests = map(lambda start: locate_end(maps, start), seeds)
    lowest = min(lowests)
    print("Lowest possible location is ", lowest)

    print("\n-- Part 2: --")
    for i in range(0, len(seeds), 2):
        locs = [SeedRange(seeds[i], seeds[i] + seeds[i + 1])]
        for m in range(len(maps)):
            next_locs = []
            for l in range(len(locs)):
                result = map_range_to_ranges(maps[m], locs[l])
                for r in range(len(result)):
                    next_locs.append(result[r])
            locs = next_locs
    lowest = min(list(map(lambda l: l.start, locs)))

    print("If we treat the seeds as ranges, the lowest possible location is ", lowest)


def locate_end(maps, start):
    loc = start
    for m in range(len(maps)):
        loc = lookup_location(maps[m], loc)
    return loc


def map_range_to_ranges(maps, r):
    output = []
    while True:
        mapper = next(filter(lambda m: m.source_start <= r.start < m.source_start + m.length, maps), None)
        if mapper is None:
            after = list(map(lambda m: m.source_start, filter(lambda m: m.source_start > r.start, maps)))
            if len(after) == 0:
                end = 0
            else:
                end = min(after)
            if end > r.end or end == 0:
                output.append(r)
                return output
            output.append(SeedRange(r.start, end - 1))
            r = SeedRange(end, r.end)
        else:
            if r.start - mapper.source_start + r.end - r.start <= mapper.length:
                output.append(SeedRange(r.start + mapper.translation, r.end + mapper.translation))
                return output
            output.append(SeedRange(r.start + mapper.translation, mapper.source_start + mapper.length\
                                    + mapper.translation))
            r = SeedRange(mapper.source_start + mapper.length, r.end)


def lookup_location(mappers, loc):
    mapper = next(filter(lambda m: m.source_start <= loc < m.source_start + m.length, mappers), None)
    if mapper is None:
        return loc
    else:
        return loc + mapper.translation


def parse_seeds(data):
    return map(int, data.split("\n")[0][7::].split(" "))


def parse_maps(data):
    parts = data.split("\n\n")[1::]
    maps = []
    for i in range(len(parts)):
        maps.append(parse_single_map(parts[i]))
    return maps


def parse_single_map(data):
    maps = []
    for m in data.split("\n")[1::]:
        values = m.split(" ")
        maps.append(Mapping(int(values[1]), int(values[0]) - int(values[1]), int(values[2])))
    return maps


@dataclass
class Mapping:
    source_start: int
    translation: int
    length: int


@dataclass
class SeedRange:
    start: int
    end: int
