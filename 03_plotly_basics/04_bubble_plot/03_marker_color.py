# Import libraries and modules
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Read the data into a pandas df
df = pd.read_csv("mpg.csv", na_values = {'horsepower':'?'})

# Create the traces
data = [
  go.Scatter(
    x = df["horsepower"],
    y = df["mpg"],
    text = df["name"],
    mode = "markers",
    marker = dict(
      size = df["weight"] / 100,
      color = df["cylinders"],
      showscale = True
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
pyo.plot(fig, filename = "03_marker_color.html")
