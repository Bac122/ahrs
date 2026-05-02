import serial
import time
import pyqtgraph as qtg
import numpy as np

def update():
    line = ser.readline().decode('utf-8', errors='ignore').strip()
    data = {}
    for chunk in line.split():
        parts = chunk.split(':')
        if len(parts) == 2:
            try:
                data[parts[0]] = int(parts[1])
            except ValueError:
                pass
    
    if 'CX' in data and 'AY' in data:
        accel_data[:-1] = accel_data[1:]
        accel_data[-1] = data['AY'] / 10.0

        comp_data[:-1] = comp_data[1:]
        comp_data[-1] = data['CX']
        
        curve_accel.setData(accel_data)
        curve_comp.setData(comp_data)




app = qtg.mkQApp()
win = qtg.GraphicsLayoutWidget(title="IMU Visualizer")
win.show()
plot = win.addPlot(title="Attitude Angles")
plot.addLegend()
plot.setYRange(-90, 90)

curve_accel = plot.plot(pen='r', name='Accel Angle')
curve_comp = plot.plot(pen='b', name='Complementary Filter')

MAX_POINTS = 200
accel_data = np.zeros(MAX_POINTS)
comp_data = np.zeros(MAX_POINTS)



ser = serial.Serial("COM3", 115200, timeout=1)



timer = qtg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(10)

qtg.exec()



