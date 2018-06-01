import re

from PyQt5 import uic, QtWidgets
import sys
from math import *
import numpy as np
from math import *
import datetime


class Ui(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Ui, self).__init__(parent)
        uic.loadUi('Window.ui', self)
        self.show()

        self.dataplot = self.plotView.addPlot(title="Approximate function")
        self.calculateButton.clicked.connect(self.calculate);

    def calculate(self):

        self.dataplot.clear()

        def f(formula, x, y):
            func = eval(formula)
            return func

        if (not self.functionInput.text()) or (not self.x0.text()) or (not self.y0.text()) or (not self.xf.text()) or (not self.n.text()):
            self.errorMessage.setText("Fill in every field!")
            return
        elif (re.search('[a-zA-Z]', self.x0.text())) or (re.search('[a-zA-Z]', self.y0.text())) or (re.search('[a-zA-Z]', self.xf.text())) or (re.search('[a-zA-Z]', self.n.text())):
            self.errorMessage.setText("Invalid input!")
            return

        x0 = int(self.x0.text())
        y0 = int(self.y0.text())
        xf = int(self.xf.text())
        n = int(self.n.text())+1
        dx = (xf - x0) / (n - 1)
        x = np.linspace(x0, xf, n)
        y = np.zeros([n])
        y[0] = y0

        for i in range(1, n):
            y[i] = dx * f(self.functionInput.text(), x[i - 1], y[i - 1]) + y[i - 1]

        result = "x=" + str(x[n - 1]) + "\n" + "y=" + str(y[n - 1])

        self.resultOutput.setPlainText(result)

        self.dataplot.plot(x, y)

        file_object = open("log.txt", "a")

        file_object.write(str(datetime.datetime.now()))
        file_object.write("\n")
        file_object.write("y' = " + self.functionInput.text())
        file_object.write("\n")
        file_object.write(result)
        file_object.write("\n")
        file_object.write("\n")

        file_object.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())
