import numpy as np
import matplotlib.pyplot as plt

import numpy as np

gamma = 2.675e8  
B0 = np.array([0, 0, 0.03])  
M0 = np.array([1e-6, 2e-6, 1e-6])
dt = 1e-6
T_max = 0.05 
N = int(T_max / dt) 

def bloch_field_z(M, gamma, B0):
    dM_x = gamma * M[1] * B0[2]
    dM_y = -gamma * M[0] * B0[2]
    return np.array([dM_x, dM_y, 0])

def improved_euler_method(M, gamma, B0, dt, N):
    M_values = []
    for i in range(N):
        M_predict = M + dt * bloch_field_z(M, gamma, B0)
        M_new = M + dt * 0.5 * (bloch_field_z(M, gamma, B0) + bloch_field_z(M_predict, gamma, B0))
        M_values.append(M_new)
        M = M_new
    return np.array(M_values)

M_values = improved_euler_method(M0, gamma, B0, dt, N)

plt.figure(figsize=(10, 6))
plt.plot(np.linspace(0, T_max, N), M_values[:, 0], label='M_x', linestyle='--')
plt.plot(np.linspace(0, T_max, N), M_values[:, 1], label='M_y', linestyle='--')
plt.plot(np.linspace(0, T_max, N), M_values[:, 2], label='M_z', linestyle='--')

plt.xlabel('Vreme (s)')
plt.ylabel('Komponente magnetizacije')
plt.legend()
plt.title('Evolucija magnetizacije - Polje duž z-ose')
plt.show()