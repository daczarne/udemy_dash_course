# Import libraries and modules
import plotly.offline as pyo
import plotly.graph_objs as go

# Define data arrays
snodgrass = [0.209, 0.205, 0.196, 0.210, 0.202, 0.207, 0.224, 0.223, 0.220, 0.201]
twain = [0.225, 0.262, 0.217, 0.240, 0.230, 0.229, 0.235, 0.217]

# Create the traces
data = [
  go.Box(
    y = snodgrass,
    boxpoints = "outliers",
    name = "Snodgrass"
  ),
  go.Box(
    y = twain,
    boxpoints = "outliers",
    name = "Twain"
  )
]

# Build the figure
fig = go.Figure(
  data = data
)

# Save the plot
pyo.plot(fig, filename = "05_mark_twain.html")
