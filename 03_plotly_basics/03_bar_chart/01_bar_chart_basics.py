# Import libraries and modules
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Read data
df = pd.read_csv("2018WinterOlympics.csv")

# Build the traces
data = [
  go.Bar(
    x = df["NOC"],
    y = df["Total"]
  )
]

layout = go.Layout(
  title = "Total medals"
)

# Build the plot
fig = go.Figure(
  data = data,
  layout = layout
)

# Save the plot
pyo.plot(fig, filename = "01_bar_chart_basics.html")