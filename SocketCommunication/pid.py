import matplotlib.pyplot as plt
import numpy as np
class PID:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.integral = 0
        self.previous_error = 0

    def update(self, measured_value, dt):
        error = self.setpoint - measured_value
        self.integral += error * dt
        derivative = (error - self.previous_error) / dt
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.previous_error = error
        return output


class HeaterSystem:
    def __init__(self, initial_temperature):
        self.temperature = initial_temperature

    def update(self, power, dt):
        # Simplified model: temperature change is proportional to the power applied
        self.temperature += power * dt

        # Simulate heat loss
        self.temperature -= 0.1 * dt  # Heat loss term
        return self.temperature


# PID parameters
Kp = 2.0
Ki = 1.0
Kd = 0.5
setpoint = 37.0  # Desired temperature

# Create PID controller and heater system
pid = PID(Kp, Ki, Kd, setpoint)
heater = HeaterSystem(initial_temperature=-10.0)

# Simulation parameters
dt = 0.1  # Time step
time = np.arange(0, 100, dt)  # 20 seconds of simulation

# Lists to store results
temperatures = []
control_signals = []

for t in time:
    current_temperature = heater.temperature
    control_signal = pid.update(current_temperature, dt)
    heater.update(control_signal, dt)

    # Store results
    temperatures.append(current_temperature)
    control_signals.append(control_signal)

# Plot results
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(time, temperatures, label='Temperature')
plt.axhline(y=setpoint, color='r', linestyle='--', label='Setpoint')
plt.xlabel('Time [s]')
plt.ylabel('Temperature [°C]')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, control_signals, label='Control Signal')
plt.xlabel('Time [s]')
plt.ylabel('Control Signal')
plt.legend()

plt.tight_layout()
plt.show()
