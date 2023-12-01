#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = 0
    for number in sys.argv[1:]:
        total += int(number)
    print("{:d}".format(total))
