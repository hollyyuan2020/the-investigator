from collections import defaultdict
from statistics import mean, pstdev

# Step 1: Open and read the traffic log file
with open("network_traffic.log", "r") as f:
    lines = f.readlines()


def to_seconds(hms):
    # Convert a "HH:MM:SS" timestamp into a raw second count for interval math
    h, m, s = (int(x) for x in hms.split(":"))
    return h * 3600 + m * 60 + s


# Step 2: Group every connection by its (source -> destination:port) pair,
# remembering the timestamps and payload sizes for each one.
flows = defaultdict(lambda: {"times": [], "sizes": []})
for line in lines:
    # Each line looks like: "09:00:01  10.0.0.15 -> 142.250.80.46:443  8421 bytes"
    parts = line.split()
    if len(parts) < 5:
        # Skip blank or malformed lines
        continue

    time = parts[0]              # e.g. "09:00:01"
    source = parts[1]            # e.g. "10.0.0.15"
    # parts[2] is the "->" arrow, which we don't need
    destination = parts[3]       # e.g. "142.250.80.46:443"
    size = int(parts[4])         # payload size in bytes

    pair = (source, destination)
    flows[pair]["times"].append(time)
    flows[pair]["sizes"].append(size)


def score_flow(times, sizes):
    # Step 3: Turn a flow's raw data into beaconing evidence.
    # Returns (score, interval_cv, size_cv, avg_interval, avg_size).
    # A beacon shows up as: many connections, very regular intervals,
    # and very consistent payload sizes.
    count = len(times)
    if count < 3:
        # Too few samples to call it a pattern
        return 0.0, None, None, None, mean(sizes)

    # Intervals between consecutive connections (seconds)
    secs = sorted(to_seconds(t) for t in times)
    intervals = [b - a for a, b in zip(secs, secs[1:])]
    avg_interval = mean(intervals)
    avg_size = mean(sizes)

    # Coefficient of variation = stddev / mean. Lower = more regular/consistent.
    interval_cv = (pstdev(intervals) / avg_interval) if avg_interval else 0.0
    size_cv = (pstdev(sizes) / avg_size) if avg_size else 0.0

    # Regularity scores: 1.0 = perfectly regular, 0.0 = very irregular.
    interval_regularity = max(0.0, 1.0 - interval_cv)
    size_regularity = max(0.0, 1.0 - size_cv)

    # Combine the signals, weighted by how many beacons we saw.
    score = interval_regularity * size_regularity * count
    return score, interval_cv, size_cv, avg_interval, avg_size


# Step 4: Score every flow and sort the most suspicious to the top.
ranked = []
for pair, data in flows.items():
    result = score_flow(data["times"], data["sizes"])
    ranked.append((pair, data, result))
ranked.sort(key=lambda item: item[2][0], reverse=True)

# Step 5: Report the top beaconing suspect in detail.
suspect, data, (score, interval_cv, size_cv, avg_interval, avg_size) = ranked[0]
source, destination = suspect

print("=== Beaconing Suspect ===")
print(f"{source} -> {destination}")
print(f"Connections: {len(data['times'])}")
if avg_interval is not None:
    # Show the evidence behind the verdict
    print(f"Avg interval: {avg_interval:.0f}s  (variation {interval_cv:.1%}  -> "
          f"{'highly regular' if interval_cv < 0.1 else 'irregular'})")
if size_cv is not None:
    print(f"Avg payload:  {avg_size:.0f} bytes  (variation {size_cv:.1%}  -> "
          f"{'very consistent' if size_cv < 0.1 else 'variable'})")
else:
    print(f"Avg payload:  {avg_size:.0f} bytes")
print(f"Suspicion score: {score:.1f}")
print("Timestamps:")
for t in data["times"]:
    print(f"  {t}")

# Step 6: Briefly summarize the other flows for context.
print("\n=== Other flows (for comparison) ===")
for pair, data, (score, interval_cv, size_cv, avg_interval, avg_size) in ranked[1:]:
    src, dst = pair
    cv_note = f"interval var {interval_cv:.0%}" if interval_cv is not None else "too few samples"
    print(f"{src} -> {dst}: {len(data['times'])} conns, "
          f"avg {avg_size:.0f} bytes, {cv_note}, score {score:.1f}")
