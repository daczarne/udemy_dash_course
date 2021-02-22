# Import libraries and modules
import plotly.offline as pyo
import plotly.graph_objs as go

# Define data array


# Create the traces



# Build the figure
fig = go.Figure(
  data = data
)

# Save the plot
pyo.plot(fig, filename = "01_hist_basics.html")
