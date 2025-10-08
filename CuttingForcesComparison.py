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

