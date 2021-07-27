import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
    
        layout = QVBoxLayout()

        # Create username textbox
        userlabel = QLabel("Username: ", self)
        self.usertextbox = QLineEdit(self)

        # Create password textbox
        passlabel = QLabel("Password: ", self)
        self.passtextbox = QLineEdit(self)
        self.passtextbox.setEchoMode(QLineEdit.Password)
        
        # Create a button in the window
        button = QPushButton('Show text', self)
        
        # connect button to function on_click
        button.clicked.connect(self.on_click)

        layout.addWidget(userlabel)
        layout.addSpacing(20)
        layout.addWidget(self.usertextbox)
        layout.addSpacing(20)
        layout.addWidget(passlabel)
        layout.addSpacing(20)
        layout.addWidget(self.passtextbox)
        layout.addSpacing(20)
        layout.addWidget(button)

        self.setLayout(layout)
        self.resize(400, 400)
        self.setWindowTitle('Carleton Courses Directory Mounter')
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.usertextbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.usertextbox.setText("")

def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()