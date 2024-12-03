import re

def find_all_mul_operands(text:str):
	mul_pattern = 'mul\((\d{1,3}),(\d{1,3})\)'
	matches = re.findall(mul_pattern, text)
	return matches


def main():
	with open('input.txt') as file:
		memory = file.read()

	# Task 1
	matches = find_all_mul_operands(memory)
	total = sum([int(a) * int(b) for a, b in matches])

	print('Total mul operations:',total)

	# Task 2
	# find deactivated parts by index range
	dont_do_parts = []

	dont_index = memory.find('don\'t()')
	while dont_index != -1:
		next_do_index = memory.find('do()', dont_index + 1)
		dont_do_parts.append((dont_index, next_do_index))
		dont_index = memory.find('don\'t()', next_do_index + 1)

	# remove deactivated parts in reverse so indexing doesnt change
	for start, end in reversed(dont_do_parts):
		memory = memory[:start] + memory[end:]

	matches = find_all_mul_operands(memory)
	total = sum([int(a) * int(b) for a, b in matches])

	print('Total active mul operations:',total)

main()
