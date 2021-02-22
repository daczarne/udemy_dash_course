#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Import libraries and modules
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
import pandas as pd

# Load data
df = pd.read_csv("abalone.csv")

# Take two random samples
a = np.random.choice(df['rings'], 30, replace = False)
b = np.random.choice(df['rings'], 20, replace = False)

# Build traces
data = [
  go.Box(
    y = a,
    name = "A"
  ),
  go.Box(
    y = b,
    name = "B"
  )
]

# Build Layout
layout = go.Layout(
  title = "Two random samples"
)

# Build the figure
fig = go.Figure(
  data = data,
  layout = layout
)

# Save the plot
pyo.plot(fig, filename = "06_exercise.html")
