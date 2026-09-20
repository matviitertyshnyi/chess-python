import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent, QPaintEvent, QPainter, QPen, QFont


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(512, 512)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_chessboard()
        self.board_state = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]
    def draw_chessboard(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        painter.setBrush(QtGui.QBrush(Qt.GlobalColor.black))
        
        square_size = 64
        
        for row in range(8):
            
            for col in range(8):
                
                if (row+col) % 2 ==0:
                    painter.setBrush(QtGui.QBrush(QtGui.QColor("#eeeed2")))
                else:
                    painter.setBrush(QtGui.QBrush(QtGui.QColor("#769656")))
                x = col * square_size
                y = row * square_size
                
                painter.drawRect(x, y, square_size, square_size)
        painter.end()
        self.label.setPixmap(canvas)
        
    def get_all_pieces(self):
        for i in range(len(self.board_state)):
            for j in range(len(self.board_state[i])):
                yield i, j, self.board_state[i][j]

    def draw_chess_pieces(self):
        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        painter.setPen(QPen(Qt.GlobalColor.black))
        font = QFont("Arial", 20, QFont.Weight.Bold)
        painter.setFont(font)
        for i, j, piece in self.get_all_pieces():
            painter.drawText((j*64)+27, (i*64)+27, f"{piece}")
        painter.end()
        self.label.setPixmap(canvas)
        
    def mousePressEvent(self, event):
        x = int(event.position().x())
        y = int(event.position().y())
        
        col = (x // 64)+1
        row = (y // 64)+1
        if event.button() == Qt.MouseButton.LeftButton:
            for i, j, piece in self.get_all_pieces():
                if(self.board_state[col-1][row-1] == piece): 
                    print(f"u just left clicked {col, row, piece}")
            canvas = self.label.pixmap()
            painter = QtGui.QPainter(canvas)
            painter.setBrush(QtGui.QBrush(Qt.GlobalColor.black))
            painter.drawEllipse((((col-1)*64)+27), (((row-1)*64)+27), 10,10)
            painter.end()
            self.label.setPixmap(canvas)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
window.draw_chess_pieces()
app.exec()