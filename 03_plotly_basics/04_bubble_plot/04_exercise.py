#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Import libraries and modules
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Read the data into a pandas df
df = pd.read_csv("mpg.csv", na_values = {'horsepower':'?'})

# Create the traces
data = [
  go.Scatter(
    x = df["displacement"],
    y = df["acceleration"],
    text = df["name"],
    mode = "markers",
    marker = dict(
      size = df["weight"] / 200,
      color = df["model_year"]
    )
  )
]

# Create the layout
layout = go.Layout(
  title = "Bubble chart"
)

# Build the figure
fig = go.Figure(
  data = data,
  layout = layout
)

# Save the plot
pyo.plot(fig, filename = "04_exercise.html")
