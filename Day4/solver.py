class Board:
    def __init__(self, input):
        self.board = input.split('\n')[:-1]
        self.x_size = len(self.board[0])
        self.y_size = len(self.board)

    def get_cell(self, x, y):
        if x < 0 or x >= self.x_size:
            return '-1'
        if y < 0 or y >= self.y_size:
            return '-1'
        return self.board[y][x]

    def get_NW_diagonal(self, x, y, n):
        cells = []
        for i in range(n):
            cells.append(self.get_cell(x-i, y+i))
        return cells

    def get_N_vertical(self, x, y, n):
        cells = []
        for i in range(n):
            cells.append(self.get_cell(x, y+i))
        return cells

    def get_NE_diagonal(self, x, y, n):
        cells = []
        for i in range(n):
            cells.append(self.get_cell(x+i, y+i))
        return cells

    def get_E_horizontal(self, x, y, n):
        cells = []
        for i in range(n):
            cells.append(self.get_cell(x+i, y))
        return cells

def main():
    with open('input.txt') as file:
        board = Board(file.read())

    xmas_count = 0
    x_mas_count = 0

    for y in range(board.y_size):
        for x in range(board.x_size):
            #Task 1 'XMAS'
            is_xmas = lambda str_list : ''.join(str_list) == 'XMAS' or ''.join(str_list)[::-1] == 'XMAS'

            if is_xmas(board.get_NW_diagonal(x, y, 4)):
                xmas_count += 1

            if is_xmas(board.get_N_vertical(x, y, 4)):
                xmas_count += 1

            if is_xmas(board.get_NE_diagonal(x, y, 4)):
                xmas_count += 1

            if is_xmas(board.get_E_horizontal(x, y, 4)):
                xmas_count += 1

            #Task 2 two MAS in X shape
            is_mas = lambda str_list : ''.join(str_list) == 'MAS' or ''.join(str_list)[::-1] == 'MAS'
            current_cell = board.get_cell(x, y)
            nw_cell = board.get_cell(x-1, y+1)
            ne_cell = board.get_cell(x+1, y+1)
            se_cell = board.get_cell(x+1, y-1)
            sw_cell = board.get_cell(x-1, y-1)

            if is_mas([nw_cell, current_cell, se_cell]) and is_mas([sw_cell, current_cell, ne_cell]):
                x_mas_count += 1

    print('XMAS count:',xmas_count)
    print('X-MAS count:',x_mas_count)

main()
