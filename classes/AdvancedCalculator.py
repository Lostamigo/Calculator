import math
from PyQt5.QtWidgets import QMainWindow
from gui.AdvancedCalculator_ui import Ui_AdvancedCalculator

class AdvancedCalculator(QMainWindow, Ui_AdvancedCalculator):
    def __init__(self, widget):
        super().__init__()
        self.setupUi(self)
        self.widget = widget
        self.setFixedSize(372, 565)
        self.setWindowTitle("Advanced Calculator")

        self.buttonDotPressed = False
        self.operation = None
        self.number1 = None
        self.number2 = None

        self.actionSimple.triggered.connect(self.gotoSimple)
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

        self.buttonSin.clicked.connect(lambda x: self.calculateImmediately(self.buttonSin.text()))
        self.buttonCos.clicked.connect(lambda x: self.calculateImmediately(self.buttonCos.text()))
        self.buttonTan.clicked.connect(lambda x: self.calculateImmediately(self.buttonTan.text()))
        self.buttonCot.clicked.connect(lambda x: self.calculateImmediately(self.buttonCot.text()))
        self.buttonXSquared.clicked.connect(lambda x: self.calculateImmediately(self.buttonXSquared.text()))
        self.buttonSqrtX.clicked.connect(lambda x: self.calculateImmediately(self.buttonSqrtX.text()))
        self.buttonFactorial.clicked.connect(lambda x: self.calculateImmediately(self.buttonFactorial.text()))
        self.button1x.clicked.connect(lambda x: self.calculateImmediately(self.button1x.text()))
        self.buttonLog.clicked.connect(lambda x: self.calculateImmediately(self.buttonLog.text()))
        self.buttonLn.clicked.connect(lambda x: self.calculateImmediately(self.buttonLn.text()))
        self.buttonEX.clicked.connect(lambda x: self.calculateImmediately(self.buttonEX.text()))

        self.buttonClear.clicked.connect(self.clearTextResult)
        self.buttonEquals.clicked.connect(self.calculate)

    def gotoSimple(self):
        self.widget.setFixedSize(372, 379)
        self.widget.setCurrentIndex(0)

    def gotoConverter(self):
        self.widget.setFixedSize(630, 246)
        self.widget.setCurrentIndex(2)

    def gotoAbout(self):
        self.widget.setFixedSize(346, 204)
        self.widget.setCurrentIndex(3)

    def updateTextResult(self, number):
        previousText = self.textResult.text()

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
                result = a + b
            elif self.operation == "-":
                result = a - b
            elif self.operation == "/":
                result = a / b
            elif self.operation == "*":
                result = a * b
            elif self.operation.lower() == "sin x":
                result = math.sin(math.radians(b))
        except Exception:
            result = "ERROR"

        self.textResult.setText(str(result))
        self.buttonDotPressed = False

    def calculateImmediately(self, operationText):
        number = self.textResult.text()

        try:

            if operationText == "sin x":
                result = round(math.sin(float(number)), 14)

            elif operationText == "cos x":
                result = round(math.cos(float(number)), 14)

            elif operationText == "tan x":
                result = round(math.tan(float(number)), 14)

            elif operationText == "cot x":
                result = math.tan(float(number))
                result = round(1 / result, 14)

            elif operationText == "x²":
                result = round(math.pow(float(number), 2), 14)

            elif operationText == "√x":
                result = round(math.sqrt(float(number)), 14)

            elif operationText == "x!":
                result = round(math.factorial(float(number)), 14)

            elif operationText == "1/x":
                result = round(1 / float(number), 14)

            elif operationText == "log x":
                result = round(math.log(float(number)), 14)

            elif operationText == "ln x":
                result = round(math.log(float(number), math.e), 14)

            elif operationText == "e^x":
                result = round(math.pow(math.e, float(number)), 14)

        except Exception:
            result = "ERROR"

        self.textResult.setText(str(result))
        self.buttonDotPressed = False