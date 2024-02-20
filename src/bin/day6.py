# dur = duration
# t   = time
# d   = distance
# tot = total dist travelled
# spd = dur

# distance = (time - duration) * duration

import numpy as np


def distance(duration_held, race_time):
    return (race_time - duration_held) * duration_held


def number_of_ways_to_beat(race_time, record):
    ways = 0
    for i in range(0, race_time + 1):
        if distance(i, race_time) > record:
            ways += 1
    return ways


times = """
55826490
""".split()
dists = """
246144110121111
""".split()
times = [int(i) for i in times]
dists = [int(i) for i in dists]
results = []
for race in list(zip(times, dists)):
    results.append(number_of_ways_to_beat(race[0], race[1]))

np.product(results)

number_of_ways_to_beat(55826490, 246144110121111)
