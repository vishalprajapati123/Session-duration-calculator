import sys
from collections import defaultdict
from datetime import datetime, time

def process_log_file(file_path):
    sessions = defaultdict(list)
    session_starts = defaultdict(list)
    min_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 23, 59, 59)
    max_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 0, 0, 0)
    time_format = "%H:%M:%S"

    with open(file_path, 'r') as log_file:
        for line in log_file:
            parts = line.strip().split(' ')
            if len(parts) != 3 or parts[2] not in ['Start', 'End']:
                continue

            time_str, user, action = parts
            time_obj = datetime.strptime(time_str, time_format)
            time_obj = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 
                                time_obj.hour, time_obj.minute, time_obj.second)
            min_time = min(min_time, time_obj)
            max_time = max(max_time, time_obj)

            if action == 'Start':
                session_starts[user].append(time_obj)
            elif action == 'End':
                if session_starts[user]:
                    start_time = session_starts[user].pop(0)  # take earliest start time
                else:
                    start_time = min_time  # no start time available, take earliest time in the file
                sessions[user].append((start_time, time_obj))

    # Process remaining sessions
    user_times = defaultdict(int)
    for user, logs in sessions.items():
        for start, end in logs:
            user_times[user] += (end - start).total_seconds()

    # Add max_time - start for all remaining starts
    for user, starts in session_starts.items():
        for start in starts:
            user_times[user] += (max_time - start).total_seconds()

    # Print results
    for user in sorted(user_times):
        total_time = user_times[user]
        session_count = len(sessions[user]) + len(session_starts[user])
        print(f"{user} {session_count} {int(total_time)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <log_file>")
        sys.exit(1)

    process_log_file(sys.argv[1])
