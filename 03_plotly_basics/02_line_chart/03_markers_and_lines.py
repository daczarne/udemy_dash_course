# Import libraries and modules
import numpy as np
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

trace_2 = go.Scatter(
  x = x_values,
  y = y_values - 5,
  mode = "markers+lines",
  name = "Markers and Lines"
)

data = [trace_0, trace_1, trace_2]

layout = go.Layout(
  title = "Line Charts"
)

fig = go.Figure(
  data = data,
  layout = layout
)

# Save the plot
pyo.plot(fig, filename = "03_markers_and_lines.html")
