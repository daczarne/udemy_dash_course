#######
# Objective: Create a stacked bar chart from
# the file mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

# Import libraries and modules
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Read the data into a pandas df
df = pd.read_csv("mocksurvey.csv", index_col = 0)

# Create the traces
data = [
  go.Bar(
    x = df[response],
    y = df.index,
    orientation = "h",
    name = response
  )
  for response in df.columns
]

# Create the layout
layout = go.Layout(
  title = "Survey Results",
  barmode = "stack"
)

# Build the figure
fig = go.Figure(
  data = data,
  layout = layout
)

# Save the plot
pyo.plot(fig, filename = "05_exercise_extra.html")
