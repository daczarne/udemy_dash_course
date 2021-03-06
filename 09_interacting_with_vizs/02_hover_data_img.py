import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd
import base64
import json

# Load the data
df = pd.read_csv("wheels.csv")

def encode_image(image_file):
  encoded = base64.b64encode(open(image_file, "rb").read())
  return "data:image/png;base64,{}".format(encoded.decode())

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
    html.Img(
      id = "hover-data",
      src = "children",
      height = 300,
      style = {
        "paddingTop": 35
      }
    ),
    style = dict(
      width = "30%"
    )
  )
])

# Build the callbacks
@app.callback(
  Output(component_id = "hover-data", component_property = "src"),
  Input(component_id = "wheels-plot", component_property = "hoverData")
)
def callback_image(hoverData):
  # Grab data from hover
  wheels = hoverData["points"][0]["y"]
  color = hoverData["points"][0]["x"]
  # Path
  path = "images/"
  encoded = encode_image(
    path + df[(df["wheels"] == wheels) & (df["color"] == color)]["image"].values[0]
  )
  return encoded

# Run the app
if __name__ == "__main__":
  app.run_server(debug = True)
