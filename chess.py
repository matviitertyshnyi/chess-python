import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent, QPaintEvent, QPainter


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(512, 512)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_chessboard()
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
            painter.drawEllipse(x, y, 10,10)
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
        
    

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

