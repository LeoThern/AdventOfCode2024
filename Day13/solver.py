from dataclasses import dataclass
import re

@dataclass
class ClawMachine:
	button_a : tuple[int, int]
	button_b : tuple[int, int]
	prize : tuple[int, int]


def find_min_b_tokens(machine:ClawMachine):
	max_b_count_x = machine.prize[0] // machine.button_b[0]
	max_b_count_y = machine.prize[1] // machine.button_b[1]
	max_b_count = min(100, max(max_b_count_x, max_b_count_y))

	while max_b_count > 0:
		missing_x = machine.prize[0] - machine.button_b[0] * max_b_count
		missing_y = machine.prize[1] - machine.button_b[1] * max_b_count

		if missing_x % machine.button_a[0] == 0 and missing_y % machine.button_a[1] == 0:
			if (a_count := missing_x / machine.button_a[0]) == missing_y / machine.button_a[1]:
				return a_count * 3 + max_b_count
		max_b_count -= 1
	return -1

machines = []

def part1():
	with open('input.txt') as file:
		file = file.read()

	pattern = re.compile(
	    r"Button A: X\+(\d+), Y\+(\d+)\s+"
	    r"Button B: X\+(\d+), Y\+(\d+)\s+"
	    r"Prize: X=(\d+), Y=(\d+)"
	)

	claw_machines = []
	for match in pattern.finditer(file):
	    button_a = (int(match.group(1)), int(match.group(2)))
	    button_b = (int(match.group(3)), int(match.group(4)))
	    prize = (int(match.group(5)), int(match.group(6)))
	    
	    claw_machines.append(ClawMachine(button_a, button_b, prize))

	total = 0
	for m in claw_machines:
		print(m)
		result = int(find_min_b_tokens(m))
		print(result)
		if result > 0:
			total += result
	print(total)

part1()