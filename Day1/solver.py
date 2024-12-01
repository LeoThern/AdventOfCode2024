def read_two_lists():
	a_list, b_list = [], []
	with open('input.txt') as file:
		for line in file:
			line = line.split(' ')
			a, b = line[0], line[-1]
			a, b = int(a), int(b)
			a_list.append(a)
			b_list.append(b)
	return a_list, b_list

def main():
	a_list, b_list = read_two_lists()
	
	a_list.sort()
	b_list.sort()

	total_distance, similarity_score = 0, 0

	for a, b in zip(a_list, b_list):
		similarity_score += a * b_list.count(a)
		total_distance += abs(a - b)
		print(f"{a} {b} distance:{abs(a - b)}")

	print('Total distance:',total_distance)
	print('Similarity score:',similarity_score)

main()