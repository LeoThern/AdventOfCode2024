from dataclasses import dataclass

class OutOfBoundsException(Exception):
    pass

@dataclass(frozen=True)
class Location:
    x: int
    y: int

class Map:
    def __init__(self, input):
        self.board = input.split('\n')[:-1]
        self.x_size = len(self.board[0])
        self.y_size = len(self.board)

    def get_cell(self, location:Location):
        if location.x < 0 or location.x >= self.x_size:
            raise OutOfBoundsException()
        if location.y < 0 or location.y >= self.y_size:
            raise OutOfBoundsException()
        return self.board[location.y][location.x]

    def iter_all_cells(self):
        for y in range(self.y_size):
            for x in range(self.x_size):
                yield Location(x, y)

    def count_paths_till_9(self, start:Location, current_index=0):
        try:
            value = int(self.get_cell(start))
        except OutOfBoundsException:
            return 0
        if value != current_index:
            return 0
        if current_index == 9 and value == 9:
            return 1
        counter = 0
        counter += self.count_paths_till_9(Location(start.x, start.y - 1), current_index + 1)
        counter += self.count_paths_till_9(Location(start.x + 1, start.y), current_index + 1)
        counter += self.count_paths_till_9(Location(start.x - 1, start.y), current_index + 1)
        counter += self.count_paths_till_9(Location(start.x, start.y + 1), current_index + 1)
        return counter

    def score_trailhead(self, start:Location, current_index=0):
        try:
            value = int(self.get_cell(start))
        except OutOfBoundsException:
            return []
        if value != current_index:
            return []
        if current_index == 9 and value == 9:
            return [start]
        destinations = []
        destinations.extend(self.score_trailhead(Location(start.x, start.y - 1), current_index + 1))
        destinations.extend(self.score_trailhead(Location(start.x + 1, start.y), current_index + 1))
        destinations.extend(self.score_trailhead(Location(start.x - 1, start.y), current_index + 1))
        destinations.extend(self.score_trailhead(Location(start.x, start.y + 1), current_index + 1))
        return destinations

def main():
    with open('input.txt') as file:
        map = Map(file.read())

    possible_trailheads = [location for location in map.iter_all_cells() if map.get_cell(location) == '0']

    total_paths = 0
    total_score = 0
    for head in possible_trailheads:
        total_score += len(set(map.score_trailhead(head)))
        total_paths += map.count_paths_till_9(head)
    print("Total Score:", total_score)
    print("Total Paths:", total_paths)

main()
