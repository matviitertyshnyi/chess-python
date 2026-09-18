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
    '''   
    def mousePressEvent(self, event: QMouseEvent):

        self.previous_pos = event.position().toPoint()
        QWidget.mousePressEvent(self, event)
    ''' 
    ''''
    def mouseMoveEvent(self, event: QMouseEvent):

        current_pos = event.position().toPoint()
        self.painter.begin(self.pixmap)
        self.painter.setRenderHints(QPainter.RenderHint.Antialiasing, True)
        self.painter.setPen(self.pen)
        self.painter.drawLine(self.previous_pos, current_pos)
        self.painter.end()

        self.previous_pos = current_pos
        self.update()

        QWidget.mouseMoveEvent(self, event)
    '''    
    
    def mousePressEvent(self, event):
        x = int(event.position().x())
        y = int(event.position().y())
        
        col = x // 64
        row = y // 64
        if event.button() == Qt.MouseButton.LeftButton:
            print(f"u just left clicked {col, row}")
            canvas = self.label.pixmap()
            painter = QtGui.QPainter(canvas)
            painter.setBrush(QtGui.QBrush(Qt.GlobalColor.black))
            painter.drawEllipse(((col*64)+27), ((row*64)+27), 10,10)
            painter.end()
            self.label.setPixmap(canvas)

    '''
    def mouseReleaseEvent(self, event: QMouseEvent):
        self.previous_pos = None
        QWidget.mouseReleaseEvent(self, event)
    '''
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
        
    def get_all_pieces(p):
        for piece, value in p.items():
            yield piece
            if isinstance(value, dict):
                yield from get_all_pieces(value)

    def draw_chess_pieces(self):
        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        painter.setPen(QPen(Qt.GlobalColor.black))
        font = QFont("Arial", 20, QFont.Weight.Bold)
        painter.setFont(font)
        for x in self.get_all_pieces(self.board_state):
            painter.drawText((x*64)+27, (x*64)+27, f"{self.board_state[(x)]}")
        painter.end()
        self.label.setPixmap(canvas)
    

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
window.draw_chess_pieces()
app.exec()


