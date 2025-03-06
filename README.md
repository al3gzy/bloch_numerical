# Numerical Solvers for Magnetization Dynamics

This repository contains implementations of various numerical solvers for simulating magnetization dynamics under different conditions. The main models include constant fields, linear gradients, point source fields and evolution in rotating reference frames. The simulations use sparse matrices for efficient computation and provide 3D visualizations of the results.

## Projects

### 1. **Magnetization Evolution under Linear Gradients**
   This simulation solves for the evolution of magnetization `M` in a 2D grid with linear gradients in both x and y directions. The model includes diffusion terms and a gradient field applied to a material. The evolution is solved using the Crank-Nicolson method with sparse matrix operations.

   - **Libraries**: `numpy`, `scipy.sparse`, `scipy.sparse.linalg`, `matplotlib`
   - **Key equations**: Diffusion equation, Magnetization dynamics with gradient terms

   **Results**: 3D visualization of magnetization evolution over time, and oscillations of magnetization in selected regions.

---

### 2. **Magnetization Evolution with Point Source**
   This solver models the magnetization dynamics in the presence of a point source applied at a specific location in a 2D grid. The solution uses a similar approach as the previous solver but includes an additional term to represent the point source field.

   - **Libraries**: `numpy`, `scipy.sparse`, `scipy.sparse.linalg`, `matplotlib`
   - **Key equations**: Diffusion equation with a point source

   **Results**: 3D visualization of magnetization evolution with a point source, and oscillations of magnetization at selected regions.

### 3. **Bloch Equation Solver (Euler and Improved Euler Methods)**
   This solver computes the time evolution of magnetization in the presence of a magnetic field along the z-axis using the Bloch equation. The code implements both the standard Euler method and the Improved Euler method for better accuracy.

   - **Libraries**: `numpy`, `matplotlib`
   - **Key equations**: Bloch equations for magnetization evolution
   
   **Results**: Evolution of the magnetization components \( M_x \), \( M_y \), and \( M_z \) over time.

---

### 4. **Rotating Frame Magnetization Dynamics**
   This simulation solves the Bloch equations for a rotating reference frame. The solver includes terms for longitudinal and transverse relaxation times (T1 and T2), and the magnetic field components in the rotating frame.

   - **Libraries**: `numpy`, `matplotlib`
   - **Key equations**: Bloch equations in rotating frame, relaxation processes

   **Results**: Time evolution of magnetization components under the influence of rotating magnetic fields.

---
