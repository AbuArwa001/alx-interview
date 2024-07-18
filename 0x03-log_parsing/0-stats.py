#!/usr/bin/env python3
"""
Script to read stdin line by line and compute metrics.
"""

import sys
import signal

# Initialize variables to keep track of metrics
total_size = 0
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}
line_count = 0


def print_statistics():
    """
    Function to print the statistics
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def signal_handler(sig, frame):
    """
    Signal handler to catch keyboard interruption and print statistics
    """
    print_statistics()
    sys.exit(0)


# Set up the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        # print(f"Line: {parts}")
        if len(parts) < 7:
            continue

        # Extracting the file size and status code from the line
        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
        except (ValueError, IndexError):
            continue

        # Updating metrics
        total_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1

        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Handle keyboard interruption gracefully
    print_statistics()
    sys.exit(0)
