# Import libraries and modules
import plotly.offline as pyo
import plotly.graph_objs as go

# Define data array
y = [1, 14, 14, 15, 16, 18, 18, 19, 19, 20,
     20, 23, 24, 26, 27, 27, 28, 29, 33, 54]

# Create the traces
data = [
  go.Box(
    y = y,
    boxpoints = "all",
    jitter = 0.3, # Left-right spread
    pointpos = 0 # On top of the box
  )
]

# Build the figure
fig = go.Figure(
  data = data
)

# Save the plot
pyo.plot(fig, filename = "03_jitter.html")
