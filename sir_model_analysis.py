import numpy as np
import matplotlib.pyplot as plt

# Parameters
μ_h = 0.1  # Human death/birth rate (assumed equal)
μ_t = 0.1  # Tick death/birth rate (assumed equal)
β_ht = 0.3  # Rate of human-to-tick transmission per bite
β_th = 0.2  # Rate of tick-to-human transmission per bite
a_h = 0.1  # Rate of humans becoming exposed after infection
b_t = 0.2  # Rate of ticks becoming exposed after infection
γ_h = 0.05  # Rate of recovery in humans (if applicable)
γ_t = 0.1  # Rate of recovery/molting in ticks (if applicable)

# Initial conditions
S_h_0 = 1000
E_h_0 = 0
I_h_0 = 10
R_h_0 = 0
S_t_0 = 10000
E_t_0 = 0
I_t_0 = 100
R_t_0 = 0

# Time parameters
t_0 = 0
t_end = 100
dt = 0.1  # time step

# Arrays for storing the results
t = np.arange(t_0, t_end, dt)
num_steps = len(t)

S_h = np.zeros(num_steps)
E_h = np.zeros(num_steps)
I_h = np.zeros(num_steps)
R_h = np.zeros(num_steps)
S_t = np.zeros(num_steps)
E_t = np.zeros(num_steps)
I_t = np.zeros(num_steps)
R_t = np.zeros(num_steps)

# Set initial conditions
S_h[0], E_h[0], I_h[0], R_h[0] = S_h_0, E_h_0, I_h_0, R_h_0
S_t[0], E_t[0], I_t[0], R_t[0] = S_t_0, E_t_0, I_t_0, R_t_0

for i in range(1, num_steps):
    N_h = S_h[i-1] + E_h[i-1] + I_h[i-1] + R_h[i-1]
    N_t = S_t[i-1] + E_t[i-1] + I_t[i-1] + R_t[i-1]

    dS_h = μ_h * N_h - β_ht * S_h[i-1] * I_t[i-1] / N_t - μ_h * S_h[i-1]
    dE_h = β_ht * S_h[i-1] * I_t[i-1] / N_t - a_h * E_h[i-1] - μ_h * E_h[i-1]
    dI_h = a_h * E_h[i-1] - γ_h * I_h[i-1] - μ_h * I_h[i-1]
    dR_h = γ_h * I_h[i-1] - μ_h * R_h[i-1]
    
    dS_t = μ_t * N_t - β_th * I_h[i-1] * S_t[i-1] / N_h - μ_t * S_t[i-1]
    dE_t = β_th * I_h[i-1] * S_t[i-1] / N_h - b_t * E_t[i-1] - μ_t * E_t[i-1]
    dI_t = b_t * E_t[i-1] - γ_t * I_t[i-1] - μ_t * I_t[i-1]
    dR_t = γ_t * I_t[i-1] - μ_t * R_t[i-1]
    
    # Update the state
    S_h[i] = S_h[i-1] + dS_h * dt
    E_h[i] = E_h[i-1] + dE_h * dt
    I_h[i] = I_h[i-1] + dI_h * dt
    R_h[i] = R_h[i-1] + dR_h * dt
    
    S_t[i] = S_t[i-1] + dS_t * dt
    E_t[i] = E_t[i-1] + dE_t * dt
    I_t[i] = I_t[i-1] + dI_t * dt
    R_t[i] = R_t[i-1] + dR_t * dt

# Plotting
plt.figure(figsize=(14, 8))

# Plotting the infectious humans and ticks
plt.plot(t, I_h, label='Infectious Humans', color='blue')
plt.plot(t, I_t, label='Infectious Ticks', color='red')

# Adding plot features
plt.title('Dynamics of Infectious Individuals in Human and Tick Populations')
plt.xlabel('Time')
plt.ylabel('Number of Infectious Individuals')
plt.legend()
plt.grid(True)

plt.show()
