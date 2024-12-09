from dataclasses import dataclass

class OutOfBoundsException(Exception):
    pass

@dataclass(frozen=True)
class Location:
    x: int
    y: int
    value: str = ''

class Map:
    def __init__(self, input):
        self.board = input.split('\n')[:-1]
        self.x_size = len(self.board[0])
        self.y_size = len(self.board)

    def get_cell(self, x, y):
        if x < 0 or x >= self.x_size:
            raise OutOfBoundsException()
        if y < 0 or y >= self.y_size:
            raise OutOfBoundsException()
        return self.board[y][x]

    def iter_all_cells(self):
        for y in range(self.y_size):
            for x in range(self.x_size):
                yield Location(x, y, self.get_cell(x, y))


def main():
    with open('input.txt') as file:
        map = Map(file.read())

    all_frequencies = set([location.value for location in map.iter_all_cells()])
    all_frequencies.remove('.')

    antinodes = set()
    for frequency in all_frequencies:
        all_antenna_locations = [location for location in map.iter_all_cells() if location.value == frequency]

        for i in range(len(all_antenna_locations)):
                for j in range(i + 1, len(all_antenna_locations)):
                    antenna_i, antenna_j = all_antenna_locations[i], all_antenna_locations[j]
                    dx, dy = antenna_j.x - antenna_i.x, antenna_j.y - antenna_i.y
                    antinode1 = Location(antenna_i.x - dx, antenna_i.y - dy)
                    antinode2 = Location(antenna_j.x + dx, antenna_j.y + dy)
                    antinodes.add(antinode1)
                    antinodes.add(antinode2)

    inbound_antinodes = []
    for node in antinodes:
        try:
            map.get_cell(node.x, node.y)
        except OutOfBoundsException:
            continue
        else:
            inbound_antinodes.append(node)

    print(len(inbound_antinodes))

main()
