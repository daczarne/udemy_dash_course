#######
# Objective: Using the "flights" dataset available
# from the data folder as flights.csv
# create a heatmap with the following parameters:
# x-axis="year"
# y-axis="month"
# z-axis(color)="passengers"
######

# Import libraries and modules
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Load data
df = pd.read_csv("flights.csv")

# Build traces
data = [
  go.Heatmap(
    x = df["year"],
    y = df["month"],
    z = df["passengers"]
  )
]

# Define the layout
layout = go.Layout(
  title = "Flights"
)

# Build the figure
fig = go.Figure(
  data = data,
  layout = layout
)

# Save the plot
pyo.plot(fig, filename = "04_heatmap_exercise.html")

