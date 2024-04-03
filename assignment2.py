# CENG 488 Assignment2 by
# Ramazan Cuhaci
# StudentId: 240201047
# Month Year: 04 / 2024

import sys
sys.dont_write_bytecode = True
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from world.view import PyTraceMainWindow
from world.scene import Scene


# I disabled the pycache with sys.dont_write_bytecode = True
# Because I want to benchmark the code with the same conditions.

if __name__ == "__main__":
	# setup a QApplication
	qApp = QApplication(sys.argv)
	qApp.setOrganizationName("CENG488")
	qApp.setOrganizationDomain("cavevfx.com")
	qApp.setApplicationName("PyTrace")

	mainScene = Scene("scene.json")

	mainWindow = PyTraceMainWindow(qApp, mainScene)
	mainWindow.setupUi()
	mainWindow.show()


	mainWindow.renderScene()
	# enter event loop
	sys.exit(qApp.exec_())