import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Nx, Ny = 50, 50
dx, dy = 0.1, 0.1
D = 0.001
gamma = 2.675e8
alfa_x, alfa_y = 0.01, 0.01
dt = 0.01
Nt = 100

x = np.linspace(0, (Nx - 1) * dx, Nx)
y = np.linspace(0, (Ny - 1) * dy, Ny)
X, Y = np.meshgrid(x, y, indexing='ij')

M = np.exp(-((X - 2.5)**2 + (Y - 2.5)**2))
M = M.flatten()

Ix = sp.eye(Nx)
Iy = sp.eye(Ny)
Dx2 = sp.diags([1, -2, 1], [-1, 0, 1], shape=(Nx, Nx)) / dx**2
Dy2 = sp.diags([1, -2, 1], [-1, 0, 1], shape=(Ny, Ny)) / dy**2
Lx = sp.kron(Iy, Dx2)
Ly = sp.kron(Dy2, Ix)
L = D * (Lx + Ly)

gradB_x = gamma * alfa_x * sp.eye(Nx * Ny)
gradB_y = gamma * alfa_y * sp.eye(Nx * Ny)

def kreiraj_matrice():
    A = sp.eye(Nx * Ny) - 0.5 * dt * (L - gradB_x - gradB_y)
    B = sp.eye(Nx * Ny) + 0.5 * dt * (L - gradB_x - gradB_y)
    return A, B

A, B = kreiraj_matrice()
solver = spla.factorized(A)

for _ in range(Nt):
    M = solver(B @ M)

M_final = M.reshape((Nx, Ny))

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, M_final, cmap='inferno')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Magnetizacija')
ax.set_title('Evolucija magnetizacije - Linearni gradijenti')
plt.show()

x_centar, y_centar = 2, 2
poluprecnik = 4
x_indeksi = (X >= x_centar - poluprecnik) & (X <= x_centar + poluprecnik)
y_indeksi = (Y >= y_centar - poluprecnik) & (Y <= y_centar + poluprecnik)

indeksi = np.ravel(np.where(x_indeksi & y_indeksi))
odabrani_indeksi = np.random.choice(indeksi, size=10, replace=False)
evolucija_M = []

for _ in range(Nt):
    M = solver(B @ M)
    evolucija_M.append(M[odabrani_indeksi])

evolucija_M = np.array(evolucija_M)

plt.figure(figsize=(8, 6))
for i in range(evolucija_M.shape[1]):
    plt.plot(evolucija_M[:, i])
plt.xlabel('Vremenski koraci')
plt.ylabel('Magnetizacija')
plt.title('Oscilacije magnetizacije u odabranom području')
plt.legend()
plt.grid(True)
plt.show()