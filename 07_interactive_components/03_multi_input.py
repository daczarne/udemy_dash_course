import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd

# Load the data
df = pd.read_csv("mpg.csv", na_values = {'horsepower':'?'})

features = df.columns

# Instanciate the app
app = dash.Dash()

# Delfine the layout
app.layout = html.Div(
  children = [
    html.Div(
      children = [
        dcc.Dropdown(
          id = "xaxis",
          options = [{"label": i, "value": i} for i in features],
          value = "displacement"
        )
      ],
      style = dict(
        width = "48%",
        display = "inline-block"
      )
    ),
    html.Div(
      children = [
        dcc.Dropdown(
          id = "yaxis",
          options = [{"label": i, "value": i} for i in features],
          value = "mpg"
        )
      ],
      style = dict(
        width = "48%",
        display = "inline-block"
      )
    ),
    dcc.Graph(
      id = "graph"
    )
  ],
  style = dict(
    padding = 10
  )
)

# Build the callbacks
@app.callback(
  Output(component_id = "graph", component_property = "figure"),
  Input(component_id = "xaxis", component_property = "value"),
  Input(component_id = "yaxis", component_property = "value")
)
def update_graph(xaxis, yaxis):
  # Build the plot
  data = [
    go.Scatter(
      x = df[xaxis],
      y = df[yaxis],
      text = df["name"],
      mode = "markers",
      marker = dict(
        size = 15,
        opacity = 0.5,
        line = dict(
          width = 0.5,
          color = "white"
        )
      )
    )
  ]
  # Define the layout
  layout = go.Layout(
    title = "MPG",
    xaxis = {
      "title": xaxis
    },
    yaxis = {
      "title": yaxis
    },
    hovermode = "closest"
  )
  # Build the figure
  fig = go.Figure(
    data = data,
    layout = layout
  )
  # Return the figure
  return fig

# Run the app
if __name__ == "__main__":
  app.run_server(debug = True)
