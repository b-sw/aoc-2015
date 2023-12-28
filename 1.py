import sys

instructions = open(sys.argv[1], 'r').read()
floor = 0
for i, step in enumerate(instructions):
    if step == '(':
        floor += 1
    elif step == ')':
        floor -= 1
    # part 2
    if floor == -1:
        print('Santa entered the basement at step:', i + 1)

print(floor)