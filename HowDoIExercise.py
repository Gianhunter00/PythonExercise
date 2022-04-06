import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit,
                               QVBoxLayout, QHBoxLayout,
                               QWidget, QTextEdit)
from PySide2.QtCore import Qt
from PySide2.QtGui import QKeyEvent
from howdoi import howdoi


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("How Do I Exercise")
        self.setFixedSize(800, 400)
        self.question = QLineEdit()

        self.question_label = QLabel()
        self.question_label.setText("Question:")

        self.answer = QTextEdit()
        self.answer.setAlignment(Qt.AlignTop)
        self.answer.setReadOnly(True)

        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self.question_label)
        horizontal_layout.addWidget(self.question)

        vertical_layout = QVBoxLayout()
        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addWidget(self.answer)

        window_layout = QWidget()
        window_layout.setLayout(vertical_layout)

        self.setCentralWidget(window_layout)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() in (Qt.Key_Enter, Qt.Key_Return):
            self.receive_answer()

    def receive_answer(self):
        question = self.question.text()
        if question != "":
            self.answer.setText(howdoi.howdoi(question))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
