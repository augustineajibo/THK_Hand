import sys
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QFormLayout
from PySide6.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from HandControl import THK_Hand

class PlotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot_sensor_data(self, matrix):

        self.ax.clear()

        # Plot each row as a separate time series
        for i, row in enumerate(matrix):
            self.ax.plot(row, label=f'Series {i + 1}')
            #print(row)

        self.ax.set_title("Sensor Data Time Series")
        self.ax.set_ylabel("Sensor Value")
        self.ax.legend()

        # Refresh the canvas
        self.canvas.draw()


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sensor Data Visualization")

        # Create the plot widget
        self.plot_widget = PlotWidget()

        # Create other form elements (for demonstration)
        self.label = QLabel("Sensor Data Plot:")

        # Set up the layout
        form_layout = QFormLayout()
        form_layout.addRow(self.label)
        form_layout.addRow(self.plot_widget)
        self.setLayout(form_layout)

        # Set up a QTimer to update the plot
        self.timer = QTimer(self)

        self.timer.timeout.connect(self.update_plot)

        self.timer.start(1000)  # Update every second
        print("OK")

        # Initialize data
        #self.data = self.sensor_data()
    def sensor_data(self):
        sensor_value = [0x80, 0x00, 0x00, 0x00]

        while True:
            hand = THK_Hand()
            result = hand.get_data(sensor_value)
            data = np.array(result).reshape(4, 4)
            #print(data)
        return data

    def update_plot(self):
        data = self.sensor_data()
        print(data)
        self.plot_widget.plot_sensor_data(data)
        print("receiving data")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainForm()
    window.show()
    sys.exit(app.exec())
