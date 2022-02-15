from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QPainter, QPen, QColor, QRadialGradient
from PyQt5.QtCore import Qt, QPoint
from game import Gomoku


class GomokuWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.game = Gomoku()

        self.last_pos = (-1, -1)
        self.res = 0
        self.status = 0

    def init_ui(self):
        self.setObjectName('MainWindow')
        self.setWindowTitle('Gomoku')
        self.setFixedSize(650, 650)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap('image/wood.png')))
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
