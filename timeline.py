# Step 1: List the log files we want to merge into one timeline
log_files = ["auth_events.log", "file_events.log"]

# Step 2: Read every line from both files into a single list
events = []
for path in log_files:
    with open(path, "r") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.strip():
                # Keep non-empty lines only
                events.append(line)

# Step 3: Sort all events chronologically.
# Each line starts with "YYYY-MM-DD HH:MM:SS", which sorts correctly
# as plain text, so the first 19 characters make a reliable sort key.
events.sort(key=lambda line: line[:19])

# Step 4: Define what makes an event noteworthy
KEY_MARKERS = ("SUCCESS LOGIN", ".locked", "READ_ME")

# Step 5: Print the merged timeline, flagging the key events
print("=== Incident Timeline ===")
for line in events:
    # Mark the line if it contains any of the suspicious markers
    if any(marker in line for marker in KEY_MARKERS):
        print(f"{line}   *** KEY EVENT ***")
    else:
        print(line)
