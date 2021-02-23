import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd
import json

# Load the data
df = pd.read_csv("wheels.csv")

# Instanciate the app
app = dash.Dash()

# Build the layout
app.layout = html.Div([
  html.Div(
    dcc.Graph(
      id = "wheels-plot",
      figure = {
        "data": [
          go.Scatter(
            x = df["color"],
            y = df["wheels"],
            dy = 1,
            mode = "markers",
            marker = dict(
              size = 15
            )
          )
        ],
        "layout": go.Layout(
          title = "Hover Data",
          hovermode = "closest" 
        )
      }
    ),
    style = dict(
      width = "30%",
      float = "left"
    )
  ),
  html.Div(
    html.Pre(
      id = "hover-data",
      style = dict(
        paddingtop = 35
      )
    ),
    style = dict(
      width = "30%"
    )
  )
])

# Build the callbacks
@app.callback(
  Output(component_id = "hover-data", component_property = "children"),
  Input(component_id = "wheels-plot", component_property = "hoverData")
)
def callback_image(hoverData):
  hoverData["points"][0]["x"]
  return json.dumps(hoverData, indent = 2)

# Run the app
if __name__ == "__main__":
  app.run_server(debug = True)
