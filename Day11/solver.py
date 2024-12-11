from functools import cache #Credit to https://github.com/thomasjevskij/advent_of_code/blob/master/2024/aoc11/day11.py for part 2

def calculate_stones(stone) -> list[int]:
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        middle = len(str(stone)) // 2
        a, b = int(str(stone)[:middle]), int(str(stone)[middle:])
        return [a, b]
    return [stone*2024]

@cache
def count_stones(stone, blinks):
    if blinks == 0:
        return 1
    return sum(count_stones(new_stone, blinks - 1) for new_stone in calculate_stones(stone))

def main():
    with open('input.txt') as file:
        stones = file.read().strip().split(' ')
        stones = [int(stone) for stone in stones]

    print(sum(count_stones(stone, 15) for stone in stones))
    print(sum(count_stones(stone, 75) for stone in stones))

main()
