import re
from collections import Counter

# Step 1: Open and read the log file
with open("server_access.log", "r") as f:
    lines = f.readlines()

# Step 2: Keep only the lines that mention a failed login
failed_lines = [line for line in lines if "FAILED LOGIN" in line]

# Step 3: Pull the IP address out of each failed-login line
counts = Counter()
for line in failed_lines:
    # Match an IPv4 address (four groups of 1-3 digits)
    match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
    if match:
        # Step 4: Tally each IP we find
        counts[match.group()] += 1

# Step 5: Print a clean summary, most attempts first
print("=== Failed Login Summary ===")
for ip, count in counts.most_common():
    print(f"{ip} - {count} failed attempts")
