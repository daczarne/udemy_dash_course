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
trace_0 = go.Scatter(
  x = x_values,
  y = y_values + 5,
  mode = "markers",
  name = "Markers"
)

trace_1 = go.Scatter(
  x = x_values,
  y = y_values,
  mode = "lines",
  name = "Lines"
)

data = [trace_0, trace_1]

layout = go.Layout(
  title = "Line Charts"
)

fig = go.Figure(
  data = data,
  layout = layout
)

# Save the plot
pyo.plot(fig, filename = "02_lines.html")
