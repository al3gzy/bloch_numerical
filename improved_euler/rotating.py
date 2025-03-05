import numpy as np
import matplotlib.pyplot as plt

gamma = 2.675e8
B1 = .000001
B0 = .0003
omega = gamma * B0
T1 = 1.5
T2 = 0.1
M0 = np.array([0.001, 0.002, 0.0015])

Bz_prime = B0 - omega / gamma
A = np.array([[-1/T2, -gamma * Bz_prime, 0],
              [gamma * Bz_prime, -1/T2, -gamma * B1],
              [0, gamma * B1, -1/T1]])

a = np.array([0, 0, 1/T1])

dt = 1e-4
t_max = 1
t_values = np.arange(0, t_max, dt)
M_values = np.zeros((len(t_values), 3))

M = M0.copy()

for i, t in enumerate(t_values):
    M_pred = M + dt * (A @ M + a)
    M = M + (dt / 2) * ((A @ M + a) + (A @ M_pred + a))
    M_values[i, :] = M

plt.figure(figsize=(8, 5))
plt.plot(t_values, M_values[:, 0], label='$M_x$', color='r')
plt.plot(t_values, M_values[:, 1], label='$M_y$', color='g')
plt.plot(t_values, M_values[:, 2], label='$M_z$', color='b')
plt.xlabel('Vreme (s)')
plt.ylabel('Magnetizacija')
plt.legend()
plt.title('Evolucija magnetizacije - Rotirajući okvir')
plt.grid()
plt.show()