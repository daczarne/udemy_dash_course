import dash
from dash_core_components.Graph import Graph
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv("mpg.csv", na_values = {'horsepower':'?'})
df["year"] = np.random.randint(-4, 5, len(df)) * 0.1 + df["model_year"] + 1900

# Instanciate the app
app = dash.Dash()

# Build the layout
app.layout = html.Div(
  children = [
    html.Div(
      children = [
        dcc.Graph(
          id = "mpg-scatter",
          figure = {
            "data": [
              go.Scatter(
                x = df["year"],
                y = df["mpg"],
                text = df["name"],
                hoverinfo = "text",
                mode = "markers"
              )
            ],
            "layout": go.Layout(
              title = "MPG",
              xaxis = {
                "title": "Model Year"
              },
              yaxis = {
                "title": "MPG"
              },
              hovermode = "closest"
            )
          }
        )
      ],
      style = {
        "width": "50%",
        "display": "inline-block"
      }
    ),
    html.Div(
      children = [
        dcc.Graph(
          id = "mpg-line",
          figure = {
            "data": [
              go.Scatter(
                x = [0, 1],
                y = [0, 1],
                mode = "lines"
              )
            ],
            "layout": go.Layout(
              title = "Acceleration",
              margin = {
                "l": 0
              }
            )
          }
        )
      ],
      style = {
        "width": "30%",
        "height": "50%",
        "display": "inline-block"
      }
    ),
    html.Div(
      children = [
        dcc.Markdown(
          id = "mpg-stats"
        )
      ],
      style = {
        "width": "20%",
        "height": "50%",
        "display": "inline-block"
      }
    )
  ]
)

# Define callbacks
@app.callback(
  Output("mpg-line", "figure"),
  Input("mpg-scatter", "hoverData")
)
def callback_graph(hoverData):
  # Find point index
  v_index = hoverData["points"][0]["pointIndex"]
  # Build the figure
  figure = {
    "data": [
      go.Scatter(
        x = [0, 1],
        y = [0, 60 / df.iloc[v_index]["acceleration"]],
        mode = "lines",
        line = {
          "width": 2 * df.iloc[v_index]["cylinders"]
        }
      )
    ],
    "layout": go.Layout(
      title = df.iloc[v_index]["name"],
      xaxis = {
        "visible": False
      },
      yaxis = {
        "visible": False,
        "range": [0, 60 / df["acceleration"].min()]
      },
      margin = {
        "l": 0
      },
      height = 300
    )
  }
  # Return figure
  return figure

@app.callback(
  Output("mpg-stats", "children"),
  Input("mpg-scatter", "hoverData")
)
def callback_stats(hoverData):
  # Find point index
  v_index = hoverData["points"][0]["pointIndex"]
  # Build Md text
  cylinders = df.iloc[v_index]["cylinders"]
  displacement = df.iloc[v_index]["displacement"]
  zero_to_sixty = df.iloc[v_index]["acceleration"]
  stats = f"""
  {cylinders} cylinders \n
  {displacement} cc displacement \n
  0 to 60mph in {zero_to_sixty} seconds
  """
  # Return the stats
  return stats

# Run the app
if __name__ == "__main__":
  app.run_server(debug = True)
