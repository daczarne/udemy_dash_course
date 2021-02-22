# Import libraries and modules
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Read data
df = pd.read_csv("2010SantaBarbaraCA.csv")

# Build traces
data = [
  go.Heatmap(
    x = df["DAY"],
    y = df["LST_TIME"],
    z = df["T_HR_AVG"].values.tolist(),
    colorscale = "Jet"
  )
]

# Define the layout
layout = go.Layout(
  title = "SB CA Temperature"
)

# Build the figure
fig = go.Figure(
  data = data,
  layout = layout
)

# Save the plot
pyo.plot(fig, filename = "02_colorscale.html")
