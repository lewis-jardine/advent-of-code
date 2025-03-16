given_time = 2503
stats = []

with open("input.txt") as f:
    lines = f.readlines()

for line in lines:
    line = line.split()
    speed, work_time, rest_time = int(line[3]), int(line[6]), int(line[13])
    stats.append(
        {
            "speed": speed,
            "work_time": work_time,
            "rest_time": rest_time,
            "distance": 0,
            "points": 0,
        }
    )

for time in range(given_time):
    best_distance = {"distance": 0, "holders": []}
    for id, stat in enumerate(stats):
        # Remainder will show wether reindeer should be moving or not
        remainder_time = time % (stat["work_time"] + stat["rest_time"])
        if remainder_time < stat["work_time"]:
            stat["distance"] += stat["speed"]
        if stat["distance"] > best_distance["distance"]:
            best_distance["distance"] = stat["distance"]
            best_distance["holders"] = [id]
        elif stat["distance"] == best_distance["distance"]:
            best_distance["holders"].append(id)
    for id in best_distance["holders"]:
        stats[id]["points"] += 1

# Find winning deer
winning_points = 0
for stat in stats:
    if stat["points"] > winning_points:
        winning_points = stat["points"]

print(winning_points)
