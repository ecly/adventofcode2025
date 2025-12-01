import sys


def run(filename: str):
    dial: int = 50
    lines = open(filename).read().strip().split("\n")
    ended_at_zero = 0
    total_crossed_zero = 0
    for line in lines:
        amount = int(line[1:])
        if not amount:
            continue

        intermediate = dial - amount if line[0] == "L" else dial + amount
        new_dial = intermediate % 100
        if new_dial == 0:
            ended_at_zero += 1

        crossed_zero = 0
        # Edge case of starting at 0, to avoid double counting
        if dial == 0 and intermediate < 0:
            crossed_zero = abs(intermediate) // 100
        elif intermediate <= 0:
            crossed_zero = 1 + abs(intermediate) // 100
        elif intermediate >= 100:
            crossed_zero = intermediate // 100

        total_crossed_zero += crossed_zero
        dial = new_dial

    print(ended_at_zero)
    print(total_crossed_zero)


filename = sys.argv[1] if len(sys.argv) > 1 else "test"
run(filename)
