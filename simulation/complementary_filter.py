# Complementary Filter
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.01)
dt = 0.01
amp = 30
freq = .1

true_angle = amp * np.sin(2 * np.pi * freq * t)
true_gyro = amp * 2 * np.pi * freq * np.cos(2 * np.pi * freq * t)

gyro_noise = np.random.normal(0, 0.1, len(t))
gyro_drift = 0
accel_noise = np.random.normal(0, 1, len(t))

noisy_gyro = true_gyro + gyro_noise + gyro_drift
noisy_accel = true_angle + accel_noise

alpha = 0.98
angle = 0.0
estimates = []
for i in range(len(t)):
    angle = alpha * (angle + noisy_gyro[i] * dt) + (1 - alpha) * noisy_accel[i]
    estimates.append(angle)

error = true_angle - np.array(estimates)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

ax1.plot(t, true_angle, label='True Angle', color='black', linewidth=2)
ax1.plot(t, noisy_accel, label='Accel', color='red', alpha=0.4, linewidth=0.8)
ax1.plot(t, noisy_gyro, label='Gyro Rate', color='green', alpha=0.4, linewidth=0.8)
ax1.plot(t, estimates, label='Estimate', color='blue', alpha=0.5, linewidth=2)

ax2.plot(t, error, label='Error', color='black', linewidth=2)

ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Angle (degrees)')
ax1.set_title('Complementary Filter Attitude Estimation')
ax1.legend()

ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Error (degrees)')
ax2.set_title('Estimation Error')
ax2.legend()
ax2.axhline(y=0, color='red', linestyle='--', linewidth=0.8)

plt.legend()
plt.show()
