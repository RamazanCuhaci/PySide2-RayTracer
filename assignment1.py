# CENG 488 Assignment7 by
# Ramazan Cuhaci
# StudentId: 240201047
# Month Year: 03 / 2024


import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from world.view import PyTraceMainWindow
from world.scene import Scene


# Fixed aspect ratio issue by using the aspect ratio of the camera in the calculation of the pixel_ndc_x and pixel_ndc_y values.

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