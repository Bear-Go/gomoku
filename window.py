from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QPainter, QPen, QColor, QRadialGradient, QIcon
from PyQt5.QtCore import Qt, QPoint
from game import Gomoku


class GomokuWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.game = Gomoku()
        self.res = 0

    def init_ui(self):
        self.setObjectName('MainWindow')
        self.setWindowTitle('Gomoku')
        self.setWindowIcon(QIcon('image/G.ico'))
        self.setFixedSize(650, 650)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap('image/wood.jpg')))
        self.setPalette(palette)
        self.show()

    def paintEvent(self, e):

        def draw_board():
            qp.setPen(QPen(QColor(0, 0, 0), 2, Qt.SolidLine))
            for x in range(15):
                qp.drawLine(40 * (x + 1), 40, 40 * (x + 1), 600)
            for y in range(15):
                qp.drawLine(40, 40 * (y + 1), 600, 40 * (y + 1))
            qp.setBrush(QColor(0, 0, 0))
            points = [(4, 4), (12, 4), (4, 12), (12, 12), (8, 8)]
            for p in points:
                qp.drawEllipse(QPoint(40 * p[0], 40 * p[1]), 5, 5)

        def draw_pieces():

            qp.setPen(QPen(QColor(0, 0, 0), 1, Qt.SolidLine))
            for x in range(15):
                for y in range(15):
                    if self.game.board[x][y] == 1:
                        radial = QRadialGradient(40 * (x + 1), 40 * (y + 1), 15, 40 * x + 35, 40 * y + 35)
                        radial.setColorAt(0, QColor(96, 96, 96))
                        radial.setColorAt(1, QColor(0, 0, 0))
                        qp.setBrush(QBrush(radial))
                        qp.drawEllipse(QPoint(40 * (x + 1), 40 * (y + 1)), 15, 15)

            qp.setPen(QPen(QColor(160, 160, 160), 1, Qt.SolidLine))
            for x in range(15):
                for y in range(15):
                    if self.game.board[x][y] == 2:
                        radial = QRadialGradient(40 * (x + 1), 40 * (y + 1), 15, 40 * x + 35, 40 * y + 35)
                        radial.setColorAt(0, QColor(255, 255, 255))
                        radial.setColorAt(1, QColor(160, 160, 160))
                        qp.setBrush(QBrush(radial))
                        qp.drawEllipse(QPoint(40 * (x + 1), 40 * (y + 1)), 15, 15)

        if hasattr(self, 'game'):
            qp = QPainter()
            qp.begin(self)
            draw_board()
            draw_pieces()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            mouse_x = e.windowPos().x()
            mouse_y = e.windowPos().y()
            if (mouse_x % 40 <= 15 or mouse_x % 40 >= 25) and (mouse_y % 40 <= 15 or mouse_y % 40 >= 25):
                game_x = int((mouse_x + 15) // 40) - 1
                game_y = int((mouse_y + 15) // 40) - 1
            else:
                return
            self.game.player1(True, game_x, game_y)

        res = self.game.check()
        if res != 0:
            self.repaint(0, 0, 650, 650)
            self.restart(res)
            return
        self.game.player2()
        res = self.game.check()
        if res != 0:
            self.repaint(0, 0, 650, 650)
            self.restart(res)
            return
        self.repaint(0, 0, 650, 650)

    def restart(self, res):
        if res == 1:
            QMessageBox.about(self, 'END', 'player1-win')
        elif res == 2:
            QMessageBox.about(self, 'END', 'player2-win')
        elif res == 3:
            QMessageBox.about(self, 'END', 'draw')
        else:
            raise ValueError('Wrong value of res')
        self.res = 0
        self.game = Gomoku()
        self.repaint(0, 0, 650, 650)
