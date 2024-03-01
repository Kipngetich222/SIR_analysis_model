# Load necessary libraries
library(tidyverse)
library(deSolve)
library(tidyverse)


# Read data (replace with your actual data path)
data <- read.csv("C:/Users/Victor/Desktop/Class/extra files/nathoo/assignment/epidemic.csv")

# Check column names and rename if necessary
colnames(data)
# Uncomment and modify as needed:
# colnames(data) <- c("time", "cases", "total_deaths")

# Inspect the data
head(data)

# Define the SIR model function
sir_model <- function(time, state, parameters) {
  with(as.list(c(state, parameters)), {
    dS <- -beta * S * I
    dI <- beta * S * I - gamma * I
    dR <- gamma * I
    
    return(list(c(dS, dI, dR)))
  })
}

# Set initial parameters and state
initial_params <- c(beta = 0.1, gamma = 0.05)
initial_state <- c(S = max(data$cases), I = min(data$cases), R = 0)

# Define time points
times <- data$time

# Fit the model
fit <- lsoda(y = initial_state, times = times, func = sir_model, parms = initial_params)

# Plot the fitted model
plot(fit, 
     y ~ time, type = "l", 
     col = c("blue", "red", "green"), 
     pch = c(16, 17, 18), 
     lwd = 2, 
     main = "SIR Model Fit", 
     xlab = "Time", 
     ylab = "Population")

legend("topright", 
       legend = c("Susceptible", "Infected", "Recovered"), 
       col = c("blue", "red", "green"), 
       pch = c(16, 17, 18), 
       lty = 1)
