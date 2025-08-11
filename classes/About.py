from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QMainWindow
from gui.About_ui import Ui_About

class About(QMainWindow, Ui_About):
    def __init__(self, widget):
        super().__init__()
        self.setupUi(self)
        self.widget = widget
        self.setFixedSize(346, 204)
        self.setWindowTitle("About Calculator")

        self.actionSimple.triggered.connect(self.gotoSimple)
        self.actionAdvanced.triggered.connect(self.gotoAdvanced)
        self.menuConverter.aboutToShow.connect(self.gotoConverter)

        self.buttonVisitLinkedin.clicked.connect(self.openLinkedIn)
        self.buttonVisitGithub.clicked.connect(self.openGitHub)

    def gotoSimple(self):
        self.widget.setFixedSize(372, 379)
        self.widget.setCurrentIndex(0)

    def gotoAdvanced(self):
        self.widget.setFixedSize(372, 565)
        self.widget.setCurrentIndex(1)

    def gotoConverter(self):
        self.widget.setFixedSize(630, 246)
        self.widget.setCurrentIndex(2)

    def openLinkedIn(self):
        url = QUrl("https://www.linkedin.com/in/filip-juracic")
        QDesktopServices.openUrl(url)

    def openGitHub(self):
        url = QUrl("https://github.com/GingerCRO")
        QDesktopServices.openUrl(url)