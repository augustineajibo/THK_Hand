import sys
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFormLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from HandControl import THK_Hand


class PlotWidget(QWidget):
    def __init__(self, data, parent=None):
        super().__init__(parent)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.plot_sensor_data(data)

    def plot_sensor_data(self, data):
        sensor_value = [0x80, 0x00, 0x00, 0x00]

        while True:
            hand = THK_Hand()
            result = hand.get_data(sensor_value)

        # Convert the list to a 4x4 numpy array
            matrix = np.array(result).reshape(4, 4)
            print(matrix)


        # Plot each row as a separate time series
            for i, row in enumerate(matrix):
                #print(row)
                self.ax.plot(row, label=f'Series {i + 1}')

            self.ax.set_title("Sensor Data Time Series")
            self.ax.set_xlabel("Time")
            self.ax.set_ylabel("Sensor Value")
            self.ax.legend()

            # Refresh the canvas
            self.canvas.draw()


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sensor Data Visualization")

        # Original list of length 16
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

        # Create the plot widget with the data
        self.plot_widget = PlotWidget(data)

        # Create other form elements (for demonstration)
        self.label = QLabel("Sensor Data Plot:")

        # Set up the layout
        form_layout = QFormLayout()
        form_layout.addRow(self.label)
        form_layout.addRow(self.plot_widget)

        self.setLayout(form_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainForm()
    window.show()
    sys.exit(app.exec())
