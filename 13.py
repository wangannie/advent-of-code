import math


def part1(data):
    arrival, buses = [n for n in data.splitlines()]
    arrival = int(arrival)
    buses = [int(bus) for bus in buses.split(',') if bus != 'x']

    shortest_wait = float('inf')
    best_bus = 0
    for bus in buses:
        wait = math.ceil(arrival / bus) * bus - arrival
        if wait < shortest_wait:
            shortest_wait = wait
            best_bus = bus
    return shortest_wait * best_bus


def part2(data):
    _, buses = [n for n in data.splitlines()]
    buses = buses.split(',')
    offsets = {}
    for i in range(len(buses)):
        if buses[i] != 'x':
            offsets[i] = int(buses[i])

    time_stamp = 0
    increment = 1
    for offset in offsets:
        bus_id = offsets[offset]
        while (time_stamp + offset) % bus_id != 0:
            time_stamp += increment
        increment *= bus_id
    return time_stamp
