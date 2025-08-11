import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from classes.About import About
from classes.AdvancedCalculator import AdvancedCalculator
from classes.Converter import Converter
from classes.SimpleCalculator import SimpleCalculator

def updateWindowTitle(index):
    widget.setWindowTitle(titles[index])

if __name__ == '__main__':

    titles = ["Simple Calculator", "Advanced Calculator", "Unit Converter", "About Calculator"]

    app = QApplication(sys.argv)
    widget = QStackedWidget()

    simpleCalculator = SimpleCalculator(widget)
    advancedCalculator = AdvancedCalculator(widget)
    converter = Converter(widget)
    about = About(widget)

    widget.addWidget(simpleCalculator)
    widget.addWidget(advancedCalculator)
    widget.addWidget(converter)
    widget.addWidget(about)

    widget.setWindowTitle(titles[0])
    widget.currentChanged.connect(updateWindowTitle)

    widget.setCurrentIndex(0)
    widget.setFixedSize(372, 379)
    widget.show()
    sys.exit(app.exec_())