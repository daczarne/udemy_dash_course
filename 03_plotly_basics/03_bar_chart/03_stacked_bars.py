# Import libraries and modules
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Read data
df = pd.read_csv("2018WinterOlympics.csv")

# Build the traces
trace_0 = go.Bar(
  x = df["NOC"],
  y = df["Gold"],
  name = "Gold",
  marker = dict(
    color = "#ffd700"
  )
)

trace_1 = go.Bar(
  x = df["NOC"],
  y = df["Silver"],
  name = "Silver",
  marker = dict(
    color = "#9ea0a1"
  )
)

trace_2 = go.Bar(
  x = df["NOC"],
  y = df["Bronze"],
  name = "Bronze",
  marker = dict(
    color = "#cd7f32"
  )
)

data = [trace_0, trace_1, trace_2]

layout = go.Layout(
  title = "Total medals",
  barmode = "stack"
)

# Build the plot
fig = go.Figure(
  data = data,
  layout = layout
)

# Save the plot
pyo.plot(fig, filename = "03_stacked_bars.html")
