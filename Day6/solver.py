from enum import IntEnum, auto

class Direction(IntEnum):
    N = auto()
    E = auto()
    S = auto()
    W = auto()

    def rotate_right(self):
        match self.value:
            case Direction.N:
                return Direction.E
            case Direction.E:
                return Direction.S
            case Direction.S:
                return Direction.W
            case Direction.W:
                return Direction.N
            case _:
                raise ValueError()

def new_position(x, y, direction:Direction):
    match direction:
        case Direction.N:
            return (x, y - 1)
        case Direction.E:
            return (x + 1, y)
        case Direction.S:
            return (x, y + 1)
        case Direction.W:
            return (x - 1, y)


class Board:
    def __init__(self, input):
        self.board = [[char for char in string] for string in input.split('\n')[:-1]]
        self.x_size = len(self.board[0])
        self.y_size = len(self.board)
        self.guard_direction: Direction = Direction.N
        for y in range(self.y_size):
            for x in range(self.x_size):
                if self.get_cell(x, y) == '^':
                     self.guard_pos = {'x':x, 'y':y}

    def count_cells(self, value):
        count = 0
        for y in range(self.y_size):
            for x in range(self.x_size):
                if self.get_cell(x, y) == value:
                    count += 1
        return count

    def get_cell(self, x, y):
        if x < 0 or x >= self.x_size:
            raise ValueError('X out of bounds')
        if y < 0 or y >= self.y_size:
            raise ValueError('Y out of bounds')
        return self.board[y][x]

    def set_cell(self, x, y, value):
        if x < 0 or x >= self.x_size:
            raise ValueError('X out of bounds')
        if y < 0 or y >= self.y_size:
            raise ValueError('Y out of bounds')
        self.board[y][x] = value

    def print_board(self, filename):
        with open(filename,'w') as file:
            for line in self.board:
                file.write(''.join(line))
                file.write('\n')

    def move_guard(self):
        new_x, new_y = new_position(self.guard_pos['x'], self.guard_pos['y'], self.guard_direction)
        new_pos = {'x':new_x, 'y':new_y}

        try:
            new_pos_value = self.get_cell(new_pos['x'], new_pos['y'])
        except ValueError:
            self.set_cell(self.guard_pos['x'], self.guard_pos['y'], 'V')
            return -1
        #set previous cell to V (Visited)
        if new_pos_value != '#':
            self.set_cell(self.guard_pos['x'], self.guard_pos['y'], 'V')
            self.guard_pos['x'] = new_pos['x']
            self.guard_pos['y'] = new_pos['y']
        else:
            self.guard_direction = self.guard_direction.rotate_right()
        return 1


def main():
    with open('input.txt') as file:
        board = Board(file.read())

    while True:
        if board.move_guard() == -1:
            break
    print(board.count_cells('V'))
    #board.print_board('output.txt')
main()
