from tkinter import filedialog

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget

class Canvas(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(16, 16), dpi=100)
        super().__init__(fig)
        self.setParent(parent)

        # matplotlib script
        """t = np.arange(0.0, 2.0, 0.01)
        s = 1 + np.sin(2 * np.pi * t)"""

    def plot_graph(self, t, s):

        self.ax.plot(t, s)

        self.ax.set(xlabel='time (s)', ylabel='power (w)', title='power chart')
        self.ax.grid()

    def open_file(self):
        file_path = filedialog.askopenfilename()
        print(file_path)
        with open(file_path, 'r') as reader:
            data = reader.readlines()

        data2 = []
        for i in range(len(data)):
            datapoint = []
            new = ""
            for ch in data[i]:
                if ch == "," or ch == "\n":
                    datapoint.append(new)
                    new = ""
                else:
                    new += ch
            datapoint.append(new)
            data2.append(datapoint)
        return data2

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1000, 800)

# time, moving, distance, watts, heart rate, cadence, velocity_smooth, lat, lng, temp, alt
        data = Canvas(self).open_file()
        time = []
        for i in range(1, len(data)):
            point = data[i][8]
            time.append(float(point))
        power = []
        for i in range(1, len(data)):
            point = data[i][7]
            if " " in point:
                point = 0
            power.append(float(point))
        chart = Canvas(self).plot_graph(time, power)



app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())

