#Step 01: Imports and Parameters
import numpy as np
import matplotlib.pyplot as plt

# Parameters (assumptions)
tau_s = 400.0   # MPa = N/mm^2
t0 = 0.10       # mm
b = 5.0         # mm

alphas_deg = np.arange(-15, 36, 1) # -15 to +35 degrees
mus = [0.3, 0.6, 0.9]

#Step 02: Define the Shear Angle Models
def phi_merchant(alpha_deg, mu):
    beta = np.degrees(np.arctan(mu))
    return 45.0 + alpha_deg / 2.0 - beta / 2.0

def phi_leeshaffer(alpha_deg, mu):
    beta = np.degrees(np.arctan(mu))
    return 45.0 + alpha_deg - beta  # From φ + β - α = 45° 

phis = phi_merchant(alphas_deg, 0.3)
print(phis)

# Step 03: Define the function to solve cutting and thrust forces

def solve_forces(alpha_deg, phi_deg, mu, tau_s, t0, b):
    alpha = np.radians(alpha_deg)
    phi = np.radians(phi_deg)

    As = b * t0 / np.sin(phi)

    Fs = tau_s * As

    A = np.array([
        [np.cos(phi), -np.sin(phi)],
        [np.sin(alpha) - mu * np.cos(alpha),np.cos(alpha) + mu * np.sin(alpha)]
    ])

    rhs = np.array([Fs, 0.0])

    Fc, Ft = np.linalg.solve(A, rhs)
    return Fc, Ft, Fs, As

phi = phi_merchant(10, 0.3)
Fc, Ft, Fs, As = solve_forces(10, phi, 0.3, tau_s, t0, b)
print(Fc, Ft, Fs, As)

