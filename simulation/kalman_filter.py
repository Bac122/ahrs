import numpy as np
import matplotlib.pyplot as plt

# simulated data
t = np.arange(0, 10, 0.01)
dt = 0.01
amp = 30
freq = 0.1

true_angle = amp * np.sin(2 * np.pi * freq * t)
true_gyro = amp * 2 * np.pi * freq * np.cos(2 * np.pi * freq * t)

gyro_noise = np.random.normal(0, 0.1, len(t))
gyro_drift = 1.0
accel_noise = np.random.normal(0, 1, len(t))

noisy_gyro = true_gyro + gyro_noise + gyro_drift
noisy_accel = true_angle + accel_noise


# parameters
q_angle = 0.001
q_bias = 0.003
r_accel = 1.0

# Initial state
angle_est = 0.0
bias_est = 0.0
P = np.array([[1, 0],
              [0, 1]], dtype=float)