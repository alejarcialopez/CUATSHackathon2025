import sys
import math
from os import path

# forgot what this does
if sys.gettrace() is not None:
    sys.stdin = open("./Tests/input.txt", 'r')
    sys.stdout = open("./Tests/output.txt", 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_int_list():
    return [int(x) for x in sys.stdin.readline().strip().split()]

result = []
cases = get_int()

for _ in range(cases):
    ans = []

    result.append(ans)

for item in result:
    for x in item:
        sys.stdout.write(str(x))
        sys.stdout.write('\n')