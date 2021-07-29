import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QPushButton, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import subprocess

class App(QWidget):

	def __init__(self):
		super().__init__()
		
		self.initUI()
	
	def initUI(self):
	
		self.container = QVBoxLayout()

		# Create username textbox
		userlabel = QLabel("Username: ", self)
		self.usertextbox = QLineEdit(self)

		# Create password textbox
		passlabel = QLabel("Password: ", self)
		self.passtextbox = QLineEdit(self)
		self.passtextbox.setEchoMode(QLineEdit.Password)
		
		# Create a button in the window
		button = QPushButton('Connect', self)
		
		# connect button to function on_click
		button.clicked.connect(self.on_click)

		self.container.addWidget(userlabel)
		self.container.addWidget(self.usertextbox)
		self.container.addSpacing(20)
		self.container.addWidget(passlabel)
		self.container.addWidget(self.passtextbox)
		self.container.addSpacing(20)
		self.container.addWidget(button)

		self.setLayout(self.container)
		self.resize(400, 150)
		self.setWindowTitle('Carleton Courses Directory Mounter')
		self.show()

	def clearScreen(self):
		if self.container.count() > 2:
			while self.container.count():
				item = self.container.takeAt(0)
				widget = item.widget()
				if widget is not None:
					#two ways to delete widgets
					#widget.setParent(None)
					widget.deleteLater()
				else:
					self.clearScreen()
		else:
			pass

	def successScreen(self):
		self.clearScreen()
		successlabel = QLabel("Success.", self)
		instructionlabel = QLabel("Courses can be viewed in your File Explorer or by typing 'H:' into your command prompt.", self)
		exitInstructionlabel = QLabel("To unmount Courses, go to command prompt and enter 'net use h: /delete'.", self)
		closeLabel = QLabel("Close this screen.", self)
		self.container.addWidget(successlabel)
		self.container.addSpacing(10)
		self.container.addWidget(instructionlabel)
		self.container.addSpacing(10)
		self.container.addWidget(exitInstructionlabel)
		self.container.addSpacing(10)
		self.container.addWidget(closeLabel)

	@pyqtSlot()
	def on_click(self):
		usertextboxValue = self.usertextbox.text()
		passtextboxValue = self.passtextbox.text()
		
		success = True

		try:
			mountCourses = subprocess.check_output(['C:/etc/scripts/mount.bat', usertextboxValue, passtextboxValue])
			#\\courses.ads.carleton.edu\courses /user:ads.carleton.edu\%user% %pass%
			#mountCourses = subprocess.check_output(['net', 'use', 'h:', '\\courses.ads.carleton.edu\courses', '/user:ads.carleton.edu\{}'.format(usertextboxValue), passtextboxValue])
		except subprocess.CalledProcessError:
			print("error")
			success = False
			QMessageBox.question(self, 'Error Message', "Error.", QMessageBox.Ok, QMessageBox.Ok)
	
		self.passtextbox.setText("")
		
		if success == True:
			self.successScreen()
	
		
		
def main():
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
