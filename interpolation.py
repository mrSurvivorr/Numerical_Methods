import re

from scipy.interpolate import interp1d
from PyQt5 import uic, QtWidgets, QtCore
import sys
import numpy as np
from math import *


class Ui(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Ui, self).__init__(parent)
        uic.loadUi('Window2.ui', self)
        self.show()

        self.dataplot = self.plotView.addPlot(title="Interpolation")
        self.calculateButton.clicked.connect(self.calculate);
        self.clearButton.clicked.connect(self.clear);
        self.fileImportButton.clicked.connect(self.importFile);

    def calculate(self):
        
        self.errorMessage.clear()

        self.dataplot.clear()

        xstring = self.xInput.text()
        ystring = self.yInput.text()

        xp = np.fromstring(xstring, dtype=float, sep=' ')

        yp = np.fromstring(ystring, dtype=float, sep=' ')

        if (not self.xInput.text()) or (not self.yInput.text()) or (not self.step.text()):
            self.errorMessage.setText("Fill in every field!")
            return
        elif not len(xp) == len(yp):
            self.errorMessage.setText("Arrays must be of equal length!")
            return
        elif (re.search('[a-wzA-WZ]', self.xInput.text())) or (re.search('[a-zA-Z]', self.yInput.text())) or (re.search('[a-zA-Z]', self.step.text())):
            self.errorMessage.setText("Invalid input!")
            return

        x_step = float(self.step.text())

        n = int(abs((xp[len(xp)-1] - xp[0])/x_step))

        x = np.linspace(xp[0], xp[len(xp)-1], n+1)

        y = interp1d(xp, yp, kind='cubic')

        result = ""

        for i in range(0, len(x)):
            result = result + str(x[i]) + "   " + str(y(x)[i]) + "\n"

        self.resultOutput.setPlainText(result)

        self.dataplot.plot(x, y(x))

    def clear(self):

        self.dataplot.clear()
        self.xInput.clear()
        self.yInput.clear()
        self.step.clear()
        self.resultOutput.clear()
        self.errorMessage.clear()

    def importFile(self):
        file_object1 = open("xImport.txt", "r")
        file_object2 = open("yImport.txt", "r")

        s1 = (file_object1.read())
        s2 = (file_object2.read())

        print(s1)
        print(s2)

        self.xInput.setText(s1)
        self.yInput.setText(s2)

        file_object1.close()
        file_object2.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())
