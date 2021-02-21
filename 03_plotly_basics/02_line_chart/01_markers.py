# Import libraries and modules
import numpy as np
from numpy.core.fromnumeric import size
import plotly.offline as pyo
import plotly.graph_objs as go

# Generate random data
np.random.seed(56)
x_values = np.linspace(0, 1, 100)
y_values = np.random.randn(100)

# Create the line chart
trace = go.Scatter(
  x = x_values,
  y = y_values + 5,
  mode = "markers",
  name = "Markers"
)

data = [trace]

layout = go.Layout(
  title = "Markers Chart"
)

fig = go.Figure(
  data = data,
  layout = layout
)

# Save the plot
pyo.plot(fig, filename = "01_markers.html")
