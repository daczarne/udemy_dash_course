#######
# Objective: Create a histogram that plots the 'length' field
# from the Abalone dataset.
# Set the range from 0 to 1, with a bin size of 0.02
######

# Import libraries and modules
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Load data
df = pd.read_csv("abalone.csv")

# Build traces
data = [
  go.Histogram(
    x = df["length"],
    xbins = dict(
      start = 0,
      end = 1,
      size = 0.02
    )
  )
]

# add a layout
layout = go.Layout(
  title = "Abalone size"
)

# Build the figure
fig = go.Figure(
  data = data,
  layout = layout
)

# Save the plot
pyo.plot(fig, filename = "03_hist_exercise.html")
