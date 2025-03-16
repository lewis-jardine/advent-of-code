def distance_flown(speed: int, work_time: int, rest_time: int, given_time: int) -> int:
    """Calculate reindeers distance flown in given time, accounting for rest time"""
    period_distance = speed * work_time
    period_time = work_time + rest_time
    # Distance in whole periods
    distance = (given_time // period_time) * period_distance
    remainder_time = given_time % period_time
    # Distance in partial periods
    if remainder_time >= work_time:
        distance += period_distance
    else:
        distance += speed * remainder_time
    return distance


given_time = 2503
best_distance = 0

with open("input.txt") as f:
    lines = f.readlines()

for line in lines:
    line = line.split()
    speed, work_time, rest_time = int(line[3]), int(line[6]), int(line[13])
    distance = distance_flown(speed, work_time, rest_time, given_time)
    if distance > best_distance:
        best_distance = distance

print(best_distance)
