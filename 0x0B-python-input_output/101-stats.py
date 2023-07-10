#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count_num = 0

    try:
        for line_check in sys.stdin:
            if count_num == 10:
                print_stats(size, status_codes)
                count_num = 1
            else:
                count_num += 1

            line_check = line_check.split()

            try:
                size += int(line_check[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line_check[-2] in codes:
                    if status_codes.get(line_check[-2], -1) == -1:
                        status_codes[line_check[-2]] = 1
                    else:
                        status_codes[line_check[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
