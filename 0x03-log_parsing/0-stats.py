#!/usr/bin/python3
"""
Log parsing
"""

import sys
import re
import signal
from typing import Dict


def output(log: Dict[str, any]) -> None:
    """
    Helper function to display stats

    Args:
        log (dict): Dictionary containing log statistics.
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print("{}: {}".format(code, log["code_frequency"][code]))


def signal_handler(sig, frame):
    """
    Signal handler to catch keyboard interruption and print statistics
    """
    output(log)
    sys.exit(0)


if __name__ == "__main__":
    regex = re.compile(
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)')  # nopep8

    line_count = 0
    log = {
        "file_size": 0,
        "code_frequency": {
            str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]
        },
    }

    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.fullmatch(line)
            if match:
                line_count += 1
                code = match.group(1)
                file_size = int(match.group(2))

                # Update file size
                log["file_size"] += file_size

                # Update status code frequency
                if code in log["code_frequency"]:
                    log["code_frequency"][code] += 1

                # Print statistics every 10 lines
                if line_count % 10 == 0:
                    output(log)
    except KeyboardInterrupt:
        # Handle keyboard interruption gracefully
        output(log)
        sys.exit(0)
    finally:
        # Print statistics at the end
        output(log)
