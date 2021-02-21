#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Import libraries and modules
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv("2010YumaAZ.csv")
days = list(df["DAY"].unique())

# Build the traces
data = []

for day in days:
    # Build the trace
    trace = go.Scatter(
        x = df[df["DAY"] == day]["LST_TIME"],
        y = df[df["DAY"] == day]["T_HR_AVG"],
        mode = "lines",
        name = day.capitalize()
    )
    # Append the trace
    data.append(trace)

# Build with a list comprehension
# data = [
#     {
#         "x": df["LST_TIME"],
#         "y": df[df["DAY"] == day]["T_HR_AVG"],
#         "name": day
#     }
#     for day in df["DAY"].unique()
# ]

# Define the layout
layout = go.Layout(
    title = "Avg temperature per day",
    xaxis = {
        "title": "Hour of the day"
    },
    yaxis = {
        "title": "Avg temperature"
    },
    hovermode = "closest"
)

# Set the figure
fig = go.Figure(
    data = data,
    layout = layout
)

# Create the plot
pyo.plot(fig, filename = "05_exercise.html")
