import re
from dataclasses import dataclass

@dataclass
class Robot:
    velocity: tuple[int, int]

class Map:
    def __init__(self, x_size, y_size):
        self.board = [[[] for _ in range(x_size)] for _ in range(y_size)]
        self.x_size = x_size
        self.y_size = y_size

    def move_robots(self):
        new_board = [[[] for _ in range(self.x_size)] for _ in range(self.y_size)]
        for location, robots in self.iter_all_locations():
            for robot in robots:
                new_x = location[0] + robot.velocity[0]
                new_x = self.x_size + new_x if new_x < 0 else new_x % self.x_size
                new_y = location[1] + robot.velocity[1]
                new_y = self.y_size + new_y if new_y < 0 else new_y % self.y_size
                new_board[new_y][new_x].append(robot)
        self.board = new_board

    def iter_all_locations(self):
        for y in range(self.y_size):
            for x in range(self.x_size):
                yield (x, y), self.board[y][x]

    def count_quadrants(self):
        first, second, third, fourth = 0,0,0,0
        for x in range(0, self.x_size // 2):
            for y in range(0, self.y_size // 2):
                first += len(self.board[y][x])

        for x in range(self.x_size // 2 + 1, self.x_size):
            for y in range(0, self.y_size // 2):
                second += len(self.board[y][x])

        for x in range(0, self.x_size // 2):
            for y in range(self.y_size // 2 + 1, self.y_size):
                third += len(self.board[y][x])

        for x in range(self.x_size // 2 + 1, self.x_size):
            for y in range(self.y_size // 2 + 1, self.y_size):
                fourth += len(self.board[y][x])

        return first, second, third, fourth

    def print_board(self):
        for line in self.board:
            for cell in line:
                char = str(len(cell))
                print(char if char != '0' else '.', end='')
            print('\n', end='')


def main():
    bathroom = Map(101, 103)

    pattern = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")

    with open('input.txt') as file:
        for line in file.readlines():
            match = pattern.search(line)
            if match:
                px, py, vx, vy = map(int, match.groups())
                bathroom.board[py][px].append(Robot((vx, vy)))

    for _ in range(100):
        bathroom.move_robots()

    first, second, third, fourth = bathroom.count_quadrants()
    safety_factor = first * second * third * fourth
    print("Safety Factor:",safety_factor)

    print("Simulating...")

    first_pattern_vertical = 68
    first_pattern_horizontal = 43

    for i in range(100, 10000):
        if i % 101 == 68 and i % 103 == 43:
            print("Seconds:", i)
            bathroom.print_board()
            break
        bathroom.move_robots()


main()