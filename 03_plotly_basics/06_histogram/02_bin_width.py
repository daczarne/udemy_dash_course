# Import libraries and modules
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Define data array
df = pd.read_csv("mpg.csv", na_values = {'horsepower':'?'})

# Create the traces
data = [
  go.Histogram(
    x = df["mpg"],
    xbins = dict(
      start = 0,
      end = 50,
      size = 10
    )
  )
]

# Define the layout
layout = go.Layout(
  title = "MPG"
)

# Build the figure
fig = go.Figure(
  data = data,
  layout = layout
)

# Save the plot
pyo.plot(fig, filename = "02_bin_width.html")
