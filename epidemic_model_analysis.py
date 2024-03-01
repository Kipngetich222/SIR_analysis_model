import pandas as pd
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Load data
data_path = "C:/Users/Victor/Desktop/Class/extra files/nathoo/assignment/epidemic.csv"
data = pd.read_csv(data_path)

# Inspect data (optional)
print(data.head())

# Rename columns if necessary (adjust based on your data structure)
# data.columns = ["time", "cases", "total_deaths"]

# SIR model function
def sir_model(t, y, beta, gamma):
    S, I, R = y
    dS_dt = -beta * S * I
    dI_dt = beta * S * I - gamma * I
    dR_dt = gamma * I
    return [dS_dt, dI_dt, dR_dt]

# Initial parameters and state
beta, gamma = 0.1, 0.05
initial_state = [max(data['cases']), min(data['cases']), 0]  # Adjust based on column names

# Time points
times = data['time'].to_numpy()  # Adjust based on column names

# Fit the model
solution = solve_ivp(sir_model, [min(times), max(times)], initial_state, args=(beta, gamma), t_eval=times)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(solution.t, solution.y[0], 'b-', label='Susceptible')
plt.plot(solution.t, solution.y[1], 'r-', label='Infected')
plt.plot(solution.t, solution.y[2], 'g-', label='Recovered')
plt.title("SIR Model Fit")
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend()
plt.show()

# Note: Estimating rates (beta and gamma) through fitting the model to actual data
# would require more advanced techniques, including optimization algorithms
# not directly implemented in this script. Libraries like `scipy.optimize` could be used for such tasks.
