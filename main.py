import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import subprocess

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
		self.resize(400, 200)
		self.setWindowTitle('Carleton Courses Directory Mounter')
		self.show()
	
	@pyqtSlot()
	def on_click(self):
		usertextboxValue = self.usertextbox.text()
		passtextboxValue = self.passtextbox.text()
		
		QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + usertextboxValue + " " + passtextboxValue, QMessageBox.Ok, QMessageBox.Ok)
		mountCourses = subprocess.Popen(['bash', 'mount.sh', usertextboxValue, passtextboxValue], stdout=subprocess.PIPE)
		for line in read_history.stdout:
			print(line)	
		self.usertextbox.setText("")
		self.passtextbox.setText("")

def main():
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
