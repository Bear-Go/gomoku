class Gomoku:

    def __init__(self):
        self.board = [[0 for _ in range(15)] for _ in range(15)]
        self.cur_step = 0

    def player1(self, input_by_window=False, pos_x=None, pos_y=None):
        while True:
            try:
                if not input_by_window:
                    pos_x = int(input('x: '))
                    pos_y = int(input('y: '))
                if 0 <= pos_x <= 14 and 0 <= pos_y <= 14:
                    if self.board[pos_x][pos_y] == 0:
                        self.board[pos_x][pos_y] = 1
                        self.cur_step += 1
                        return
            except ValueError:
                continue

    def player2(self):
        for x in range(15):
            for y in range(15):
                if self.board[x][y] == 0:
                    self.board[x][y] = 2
                    self.cur_step += 1
                    return

    def check(self):
        # 横
        for x in range(11):
            for y in range(15):
                if self.board[x][y] == 1 and \
                        self.board[x + 1][y] == 1 and \
                        self.board[x + 2][y] == 1 and \
                        self.board[x + 3][y] == 1 and \
                        self.board[x + 4][y] == 1:
                    return 1
                if self.board[x][y] == 2 and \
                        self.board[x + 1][y] == 2 and \
                        self.board[x + 2][y] == 2 and \
                        self.board[x + 3][y] == 2 and \
                        self.board[x + 4][y] == 2:
                    return 2
        # 纵
        for x in range(15):
            for y in range(11):
                if self.board[x][y] == 1 and \
                        self.board[x][y + 1] == 1 and \
                        self.board[x][y + 2] == 1 and \
                        self.board[x][y + 3] == 1 and \
                        self.board[x][y + 4] == 1:
                    return 1
                if self.board[x][y] == 2 and \
                        self.board[x][y + 1] == 2 and \
                        self.board[x][y + 2] == 2 and \
                        self.board[x][y + 3] == 2 and \
                        self.board[x][y + 4] == 2:
                    return 2
        # 左上右下
        for x in range(11):
            for y in range(11):
                if self.board[x][y] == 1 and \
                        self.board[x + 1][y + 1] == 1 and \
                        self.board[x + 2][y + 2] == 1 and \
                        self.board[x + 3][y + 3] == 1 and \
                        self.board[x + 4][y + 4] == 1:
                    return 1
                if self.board[x][y] == 2 and \
                        self.board[x + 1][y + 1] == 2 and \
                        self.board[x + 2][y + 2] == 2 and \
                        self.board[x + 3][y + 3] == 2 and \
                        self.board[x + 4][y + 4] == 2:
                    return 2
        # 左下右上
        for x in range(11):
            for y in range(11):
                if self.board[x + 4][y] == 1 and \
                        self.board[x + 3][y + 1] == 1 and \
                        self.board[x + 2][y + 2] == 1 and \
                        self.board[x + 1][y + 3] == 1 and \
                        self.board[x][y + 4] == 1:
                    return 1
                if self.board[x + 4][y] == 2 and \
                        self.board[x + 3][y + 1] == 2 and \
                        self.board[x + 2][y + 2] == 2 and \
                        self.board[x + 1][y + 3] == 2 and \
                        self.board[x][y + 4] == 2:
                    return 2
        # 平
        for x in range(15):
            for y in range(15):
                if self.board[x][y] == 0:
                    return 0
        # 无胜负
        return 3

    def show(self, res):
        for y in range(15):
            for x in range(15):
                if self.board[x][y] == 0:
                    print(' ', end='')
                elif self.board[x][y] == 1:
                    print('A', end='')
                elif self.board[x][y] == 2:
                    print('B', end='')

                if x != 14:
                    print('-', end='')
            print('\n', end='')
            for x in range(15):
                print('| ', end='')
            print('\n', end='')

        if res == 1:
            print('player1 win')
        elif res == 2:
            print('player2 win')
        elif res == 3:
            print('draw')

    def play(self):
        while True:
            self.player1()
            res = self.check()
            if res != 0:
                self.show(res)
                return
            self.player2()
            res = self.check()
            if res != 0:
                self.show(res)
                return
            self.show(0)
