#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    # Get the number of arguments (excluding the script name)
    num_arguments = len(sys.argv) - 1
    
    # Print the list of arguments
    if num_arguments > 1:
        print("{} arguments:".format(num_arguments))
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
    elif num_arguments == 0:
        print("{} arguments.".format(num_arguments))
    elif num_arguments == 1:
        print("{} argument:".format(num_arguments))
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
    else:
        print("0 arguments.")
