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
gyro_drift = 1
accel_noise = np.random.normal(0, 1, len(t))

noisy_gyro = true_gyro + gyro_noise + gyro_drift
noisy_accel = true_angle + accel_noise


def complementary_filter(noisy_accel, noisy_gyro, dt, alpha):
    angle = 0.0
    estimates = []
    for i in range(len(noisy_accel)):
        angle = alpha * (angle + noisy_gyro[i] * dt) + (1 - alpha) * noisy_accel[i]
        estimates.append(angle)
    return estimates


def get_error(true_angle, estimates):
    return true_angle - np.array(estimates)


a1 = complementary_filter(noisy_accel, noisy_gyro, dt, 0.98)
a2 = complementary_filter(noisy_accel, noisy_gyro, dt, 0.5)
a3 = complementary_filter(noisy_accel, noisy_gyro, dt, 0.99)

error  = get_error(true_angle, a1)
error2 = get_error(true_angle, a2)
error3 = get_error(true_angle, a3)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 8))

ax1.plot(t, true_angle, label='True Angle', color='black', linewidth=2)
ax1.plot(t, noisy_accel, label='Accel', color='red', alpha=0.4, linewidth=0.8)
ax1.plot(t, noisy_gyro, label='Gyro Rate', color='green', alpha=0.4, linewidth=0.8)
ax1.plot(t, a1, label='Estimate', color='blue', alpha=0.5, linewidth=2)
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Angle (degrees)')
ax1.set_title('Complementary Filter Attitude Estimation')
ax1.legend()

ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Error (degrees)')
ax2.set_title('Estimation Error')
ax2.legend()
ax2.axhline(y=0, color='red', linestyle='--', linewidth=0.8)
ax2.plot(t, error, label='Error', color='black', linewidth=2)

ax3.plot(t, a1, label='alpha = 0.98', color='red', linewidth=2)
ax3.plot(t, a2, label='alpha = 0.5', color='green', linewidth=1.5)
ax3.plot(t, a3, label='alpha = 0.99', color='blue', linewidth=1, linestyle='--')
ax3.plot(t, true_angle, label='True Angle', color='black', linewidth=2, zorder=5)
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Angle (degrees)')
ax3.legend()
ax3.set_title('Alpha Comparison')
ax3.axhline(y=0, color='black', linestyle='--', linewidth=0.5)

plt.legend()
plt.show()
