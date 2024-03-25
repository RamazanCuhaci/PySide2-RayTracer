# Assignment 1: PyTrace


import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from view import*
from scene import Scene


if __name__ == "__main__":
	# setup a QApplication
	qApp = QApplication(sys.argv)
	qApp.setOrganizationName("CENG488")
	qApp.setOrganizationDomain("cavevfx.com")
	qApp.setApplicationName("PyTrace")

	# setup main ui
	width = 800
	height = 600

	mainScene = Scene("scene.json")

	mainWindow = PyTraceMainWindow(qApp, width, height,mainScene)
	mainWindow.setupUi()
	mainWindow.show()

	mainWindow.renderScene()

	# enter event loop
	sys.exit(qApp.exec_())