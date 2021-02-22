#######
# Objective: build a dashboard that imports OldFaithful.csv
# from the data directory, and displays a scatterplot.
# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).
######

# Import libraries and modules
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# Instanciate the app
app = dash.Dash()

# Load the data
df = pd.read_csv("OldFaithful.csv")

# Create a Dash layout that contains a Graph component:
app.layout = html.Div([
  dcc.Graph(
    id = "old_faithful",
    figure = {
      "data": [
        go.Scatter(
          x = df["X"],
          y = df["Y"],
          mode = "markers"
        )
      ],
      "layout": go.Layout(
        title = "Old Faithful Eruptions",
        xaxis = {
          "title": "Duration (in minutes)"
        },
        yaxis = {
          "title": "Interval (in minutes)"
        },
        hovermode = "closest"
      )
    }
  )
])

# Run app
if __name__ == '__main__':
    app.run_server(debug = True)
