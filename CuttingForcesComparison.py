import numpy as np
import matplotlib.pyplot as plt

tau_s = 400.0
t0 = 0.10
b = 5.0

alphas_deg = np.arange(-15, 36. 1) # -15 to +35 degrees
mus = [0.3, 0.6, 0.9]

def phi_merchant(alpha_deg, mu):
    beta = np.degrees(np.arctan(mu))
    return 45.0 + alpha_deg/2.0 - beta/2.0