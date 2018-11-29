import sys

def main():
    name = sys.argv[2]
    greeting = sys.argv[1]
    print "{} {}".format(greeting, name)

#---
main()
