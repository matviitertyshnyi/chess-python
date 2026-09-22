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
        self.selected_square = None
        self.piece_possible_moves = {
            "p": [(0, 1), (0,2), ],
            "P":[(0, -1), (0,-2),]
            }
        self.current_possible_moves = [],
        
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
    #function that reads the chessboard matrix
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
            if piece != ".":
                painter.drawText((j*64)+27, (i*64)+27, f"{piece}")
        painter.end()
        self.label.setPixmap(canvas)
        
    def mousePressEvent(self, event):
        x = int(event.position().x())
        y = int(event.position().y())
        
        col = (x // 64)
        row = (y // 64)
        
        if event.button() == Qt.MouseButton.LeftButton:
            # handling the memory
            
            
            chosen_piece = self.board_state[row][col]
            if self.selected_square == None:
                # if memory is empty and empty square is clicked -> do nothing
                if chosen_piece == ".":
                    return
                
                # if memory is empty but piece is clicked -> save coords to memory
                self.selected_square = (row, row)
                
                # redraw the chessboard so the possible moves cannot stack, rendering
                self.draw_chessboard()
                self.draw_chess_pieces()
                
                print(f"u just clicked {row, col, chosen_piece}")
                
                self.calculate_possible_moves(row, col, chosen_piece)
                
                canvas = self.label.pixmap()
                painter = QtGui.QPainter(canvas)
                painter.setBrush(QtGui.QBrush(Qt.GlobalColor.black))
                painter.end()
                self.label.setPixmap(canvas)
            # we try to move a piece here  
            else: 
                self.move_piece(row, col, chosen_piece)
            
            
    def calculate_possible_moves(self, row, col, piece):
        
        self.current_possible_moves.clear()
        
        for possible_x, possible_y in self.piece_possible_moves[piece]:
            
            final_x = row + possible_x
            final_y = col + possible_y
            
            print(f"Moves available for the {piece} are: {final_x}, {final_y}")
            self.current_possible_moves.append((final_x, final_y))
            canvas = self.label.pixmap()
            painter = QtGui.QPainter(canvas)
            painter.setBrush(QtGui.QBrush(Qt.GlobalColor.black))
            painter.drawEllipse((((final_x)*64)+27), (((final_y)*64)+27), 10,10)
            painter.end()
            self.label.setPixmap(canvas)
            
    def move_piece(self, row, col, piece):
            for x, y in self.calculate_possible_moves(self, row, col, piece):
                available_x = x
                available_y = y
                return
                
        

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
window.draw_chess_pieces()
app.exec()