from PyQt5.QtWidgets import QMainWindow
from gui.SimpleCalculator_ui import Ui_SimpleCalculator

class SimpleCalculator(QMainWindow, Ui_SimpleCalculator):

    def __init__(self, widget):
        super().__init__()
        self.setupUi(self)
        self.widget = widget
        self.setFixedSize(372, 379)
        self.setWindowTitle("Simple Calculator")

        self.buttonDotPressed = False
        self.operation = None
        self.number1 = None
        self.number2 = None

        self.actionAdvanced.triggered.connect(self.gotoAdvanced)
        self.menuConverter.aboutToShow.connect(self.gotoConverter)
        self.menuAbout.aboutToShow.connect(self.gotoAbout)

        self.button1.clicked.connect(lambda x: self.updateTextResult(self.button1.text()))
        self.button2.clicked.connect(lambda x: self.updateTextResult(self.button2.text()))
        self.button3.clicked.connect(lambda x: self.updateTextResult(self.button3.text()))
        self.button4.clicked.connect(lambda x: self.updateTextResult(self.button4.text()))
        self.button5.clicked.connect(lambda x: self.updateTextResult(self.button5.text()))
        self.button6.clicked.connect(lambda x: self.updateTextResult(self.button6.text()))
        self.button7.clicked.connect(lambda x: self.updateTextResult(self.button7.text()))
        self.button8.clicked.connect(lambda x: self.updateTextResult(self.button8.text()))
        self.button9.clicked.connect(lambda x: self.updateTextResult(self.button9.text()))
        self.button0.clicked.connect(lambda x: self.updateTextResult(self.button0.text()))
        self.buttonDot.clicked.connect(lambda x: self.updateTextResult(self.buttonDot.text()))

        self.buttonSum.clicked.connect(lambda x: self.chosenOperation(self.buttonSum.text()))
        self.buttonSubtract.clicked.connect(lambda x: self.chosenOperation(self.buttonSubtract.text()))
        self.buttonMultiply.clicked.connect(lambda x: self.chosenOperation(self.buttonMultiply.text()))
        self.buttonDivide.clicked.connect(lambda x: self.chosenOperation(self.buttonDivide.text()))

        self.buttonClear.clicked.connect(self.clearTextResult)
        self.buttonEquals.clicked.connect(self.calculate)

    def gotoSimple(self):
        self.widget.setFixedSize(372, 379)
        self.widget.setCurrentIndex(0)

    def gotoAdvanced(self):
        self.widget.setFixedSize(372, 565)
        self.widget.setCurrentIndex(1)

    def gotoConverter(self):
        self.widget.setFixedSize(630, 246)
        self.widget.setCurrentIndex(2)

    def gotoAbout(self):
        self.widget.setFixedSize(346, 204)
        self.widget.setCurrentIndex(3)

    def updateTextResult(self, number):
        previousText = self.textResult.text()

        if previousText == "ERROR":
            previousText = ""
            self.buttonDotPressed = False

        if previousText == "0":
            previousText = ""

        if number == "." and not self.buttonDotPressed:
            self.textResult.setText(previousText + ".")
            self.buttonDotPressed = True
        elif number == "." and self.buttonDotPressed:
            self.textResult.setText(previousText)
        else:
            self.textResult.setText(previousText + str(number))

    def chosenOperation(self, operation):
        self.operation = operation
        self.number1 = self.textResult.text()
        self.textResult.setText("")
        self.buttonDotPressed = False

    def clearTextResult(self):
        self.textResult.setText("")
        self.buttonDotPressed = False

    def calculate(self):
        self.number2 = self.textResult.text()

        try:
            a = float(self.number1)
            b = float(self.number2)

            if self.operation == "+":
                result = round(a + b, 14)
            elif self.operation == "-":
                result = round(a - b, 14)
            elif self.operation == "/":
                result = round(a / b, 14)
            elif self.operation == "*":
                result = round(a * b, 14)
        except Exception:
            result = "ERROR"

        self.textResult.setText(str(result))
        self.buttonDotPressed = False