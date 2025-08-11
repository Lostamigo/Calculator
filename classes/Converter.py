from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QMainWindow
from gui.Converter_ui import Ui_Converter

class Converter(QMainWindow, Ui_Converter):
    def __init__(self, widget):
        super().__init__()
        self.setupUi(self)
        self.widget = widget
        self.setFixedSize(630, 246)
        self.setWindowTitle("Unit Converter")

        self.validator = QDoubleValidator(0.0, float('inf'), 10, self)
        self.validator.setNotation(QDoubleValidator.StandardNotation)
        self.qLineEditLimitInput()

        self.lengthFactors = {"mm": 1e-3, "cm": 1e-2, "dm": 1e-1, "m": 1.0, "dam": 1e1, "hm": 1e2, "km": 1e3}
        self.massFactors = {"mg": 1e-3, "cg": 1e-2, "dg": 1e-1, "g": 1.0, "dag": 1e1, "hg": 1e2, "kg": 1e3}
        self.timeFactors = {"s": 1, "min": 60, "h": 3600, "day": 86400}

        self.actionSimple.triggered.connect(self.gotoSimple)
        self.actionAdvanced.triggered.connect(self.gotoAdvanced)
        self.menuAbout.aboutToShow.connect(self.gotoAbout)

        self.inputBox1.textEdited.connect(self.lengthChanged1)
        self.inputBox2.textEdited.connect(self.lengthChanged2)
        self.inputBox3.textEdited.connect(self.massChanged1)
        self.inputBox4.textEdited.connect(self.massChanged2)
        self.inputBox5.textEdited.connect(self.temperatureChanged1)
        self.inputBox6.textEdited.connect(self.temperatureChanged2)
        self.inputBox7.textEdited.connect(self.timeChanged1)
        self.inputBox8.textEdited.connect(self.timeChanged2)

    def gotoSimple(self):
        self.widget.setFixedSize(372, 379)
        self.widget.setCurrentIndex(0)

    def gotoAdvanced(self):
        self.widget.setFixedSize(372, 565)
        self.widget.setCurrentIndex(1)

    def gotoAbout(self):
        self.widget.setFixedSize(346, 204)
        self.widget.setCurrentIndex(3)

    def qLineEditLimitInput(self):
        self.inputBox1.setValidator(self.validator)
        self.inputBox2.setValidator(self.validator)
        self.inputBox3.setValidator(self.validator)
        self.inputBox4.setValidator(self.validator)
        self.inputBox5.setValidator(self.validator)
        self.inputBox6.setValidator(self.validator)
        self.inputBox7.setValidator(self.validator)
        self.inputBox8.setValidator(self.validator)

    def lengthChanged1(self):
        if self.inputBox1.text() == "":
            self.inputBox2.setText("")
            return

        unit1 = self.comboBox1.currentText()
        unit2 = self.comboBox2.currentText()

        meters = float(self.inputBox1.text()) * self.lengthFactors[unit1]
        result = round(meters / self.lengthFactors[unit2], 4)
        self.inputBox2.setText(str(result))

    def lengthChanged2(self):
        if self.inputBox2.text() == "":
            self.inputBox1.setText("")
            return

        unit1 = self.comboBox1.currentText()
        unit2 = self.comboBox2.currentText()

        meters = float(self.inputBox2.text()) * self.lengthFactors[unit2]
        result = round(meters / self.lengthFactors[unit1], 4)
        self.inputBox1.setText(str(result))

    def massChanged1(self):
        if self.inputBox3.text() == "":
            self.inputBox4.setText("")
            return

        unit1 = self.comboBox3.currentText()
        unit2 = self.comboBox4.currentText()

        grams = float(self.inputBox3.text()) * self.massFactors[unit1]
        result = round(grams / self.massFactors[unit2], 4)
        self.inputBox4.setText(str(result))

    def massChanged2(self):
        if self.inputBox4.text() == "":
            self.inputBox3.setText("")
            return

        unit1 = self.comboBox3.currentText()
        unit2 = self.comboBox4.currentText()

        grams = float(self.inputBox4.text()) * self.massFactors[unit2]
        result = round(grams / self.massFactors[unit1], 4)
        self.inputBox3.setText(str(result))

    def temperatureChanged1(self):
        if self.inputBox5.text() == "":
            self.inputBox6.setText("")
            return

        unit1 = self.comboBox5.currentText()
        unit2 = self.comboBox6.currentText()

        if unit1 == "°C":
            if unit2 == "°C":
                self.inputBox6.setText(self.inputBox5.text())
            elif unit2 == "°F":
                self.inputBox6.setText(str(round(float(self.inputBox5.text()) * 9 / 5 + 32, 4)))
            elif unit2 == "K":
                self.inputBox6.setText(str(round(float(self.inputBox5.text()) + 273.15, 4)))

        elif unit1 == "°F":
            if unit2 == "°C":
                self.inputBox6.setText(str(round((float(self.inputBox5.text()) - 32) * 5 / 9, 4)))
            elif unit2 == "°F":
                self.inputBox6.setText(str(self.inputBox5.text()))
            elif unit2 == "K":
                self.inputBox6.setText(str(round((float(self.inputBox5.text()) - 32) * 5 / 9 + 273.15, 4)))

        elif unit1 == "K":
            if unit2 == "°C":
                self.inputBox6.setText(str(round(float(self.inputBox5.text()) - 273.15, 4)))
            elif unit2 == "°F":
                self.inputBox6.setText(str(round((float(self.inputBox5.text()) - 273.15) * 9 / 5 + 32, 4)))
            elif unit2 == "K":
                self.inputBox6.setText(self.inputBox5.text())

    def temperatureChanged2(self):
        if self.inputBox6.text() == "":
            self.inputBox5.setText("")
            return

        unit1 = self.comboBox5.currentText()
        unit2 = self.comboBox6.currentText()

        if unit2 == "°C":
            if unit1 == "°C":
                self.inputBox5.setText(self.inputBox6.text())
            elif unit1 == "°F":
                self.inputBox5.setText(str(round(float(self.inputBox6.text()) * 9 / 5 + 32, 4)))
            elif unit1 == "K":
                self.inputBox5.setText(str(round(float(self.inputBox6.text()) + 273.15, 4)))

        elif unit2 == "°F":
            if unit1 == "°C":
                self.inputBox5.setText(str(round((float(self.inputBox6.text()) - 32) * 5 / 9, 4)))
            elif unit1 == "°F":
                self.inputBox5.setText(str(self.inputBox6.text()))
            elif unit1 == "K":
                self.inputBox5.setText(str(round((float(self.inputBox6.text()) - 32) * 5 / 9 + 273.15, 4)))

        elif unit2 == "K":
            if unit1 == "°C":
                self.inputBox5.setText(str(round(float(self.inputBox6.text()) - 273.15, 4)))
            elif unit1 == "°F":
                self.inputBox5.setText(str(round((float(self.inputBox6.text()) - 273.15) * 9 / 5 + 32, 4)))
            elif unit1 == "K":
                self.inputBox5.setText(self.inputBox6.text())

    def timeChanged1(self):
        if self.inputBox7.text() == "":
            self.inputBox8.setText("")
            return

        unit1 = self.comboBox7.currentText()
        unit2 = self.comboBox8.currentText()

        seconds = float(self.inputBox7.text()) * self.timeFactors[unit1]
        result = round(seconds / self.timeFactors[unit2], 4)
        self.inputBox8.setText(str(result))

    def timeChanged2(self):
        if self.inputBox8.text() == "":
            self.inputBox7.setText("")
            return

        unit1 = self.comboBox7.currentText()
        unit2 = self.comboBox8.currentText()

        seconds = float(self.inputBox8.text()) * self.timeFactors[unit2]
        result = round(seconds / self.timeFactors[unit1], 4)
        self.inputBox7.setText(str(result))