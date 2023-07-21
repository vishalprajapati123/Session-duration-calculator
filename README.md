# Fair Billing

## Problem Statement

You work for a hosted application provider that charges for the use of its application based on the duration of sessions. The charge is calculated per second of usage. You have a log file that contains the start and end times of sessions, along with the username and the action (start or end) of each session. However, the log file may have missing or incomplete information, and there may be sessions that overlap the time boundaries of the log file. Your task is to process the log file and generate a report that includes the following information for each user:
- Username
- Number of sessions
- Minimum possible total duration of sessions in seconds, consistent with the data in the file

## Solution

### Approach

To solve this problem, the following approach is used:

1. Initialize necessary variables, including dictionaries to store session starts and session durations for each user, and variables to track the earliest and latest time recorded in the log file.
2. Read the log file line by line.
3. For each line, validate the format and extract the timestamp, username, and action (start or end) of the session.
4. Update the earliest and latest times if necessary.
5. If it's a session start, add the session start time to the session starts dictionary.
6. If it's a session end, check if there is a matching start time in the session starts dictionary. If found, calculate the duration of the session and store it in the session durations dictionary.
7. After processing all lines, handle any remaining session starts (with no matching end time) by assuming the latest time as the end time and calculate the duration accordingly.
8. Finally, print the report for each user, including the number of sessions and the minimum possible total duration of their sessions.

### Code Flow

The code follows these main steps:

1. Import necessary modules and define helper functions.
2. Parse the command line argument to get the path of the log file.
3. Initialize variables and data structures.
4. Open the log file.
5. Read each line from the log file.
6. Split the line into timestamp, username, and action.
7. Validate the line format and ignore invalid lines.
8. Convert the timestamp to a datetime object and update the earliest and latest times.
9. Process the start or end action accordingly.
10. Handle remaining session starts with no matching end time.
11. Calculate the total duration for each user.
12. Print the report for each user.
13. Close the log file.

## Prerequisites

- Python 3.x

### How to Run

1. Clone the repository: 
   ```sh
   git clone <repository_url>
   ```
2. Navigate to the cloned directory:
   ```sh
   cd <repository_directory>
   ```
3. Run the code with the log file path as a command line argument:
   ```sh
   python session_duration_calculator.py <log_file_path>
   ```

### Input Example

Assuming a log file named `logfile.txt` with the following content:

```
14:02:03 ALICE99 Start
14:02:05 CHARLIE End
14:02:34 ALICE99 End
14:02:58 ALICE99 Start
14:03:02 CHARLIE Start
14:03:33 ALICE99 Start
14:03:35 ALICE99 End
14:03:37 CHARLIE End
14:04:05 ALICE99 End
14:04:23 ALICE99 End
14:04:41 CHARLIE Start
```

### Output Example (Terminal)

Running the code with the provided log file would produce the following output:

```
ALICE99 4 240
CHARLIE 3 37
```

### Further Notes

- Ensure that the log file path is provided as a command line argument.
- The log file should be in the specified format (timestamp, username, action) for each line.
- Lines that do not conform to the specified format will be ignored.
- The code assumes that all log records are from within a single day and are correctly

 ordered chronologically.
- Invalid or irrelevant data within the file will be silently ignored and not included in calculations.

