import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import os
import pandas_datareader.data as web
from datetime import datetime

# Get API key
with open("api_key.txt") as f:
  os.environ["IEX_API_KEY"] = f.readline()

# Instanciate the app
app = dash.Dash()

# Build the layout
app.layout = html.Div(
  [
    html.H1("Stock Ticker Dashboard"),
    html.H3("Enter a stock symbol"),
    dcc.Input(
      id = "stock-picker",
      value = "TSLA"
    ),
    dcc.Graph(
      id = "graph",
      figure = {
        "data": [
          {"x": [1, 2], "y": [3, 1]}
        ],
        "layout": {
          "title": "Stock Name"
        }
      }
    )
  ]
)

# Build the callbacks
@app.callback(
  Output(component_id = "graph", component_property = "figure"),
  Input(component_id = "stock-picker", component_property = "value")
)
def update_graph(stock_ticker):
  # Get the data
  start = datetime(2017, 1, 1)
  end = datetime(2017, 12, 31)
  df = web.DataReader(stock_ticker, "iex", start, end)
  # Update plot title
  fig = {
    "data": [
      {"x": df.index, "y": df["close"]}
    ],
    "layout": {
      "title": stock_ticker
    }
  }
  # Return fig
  return fig

# Run the app
if __name__ == "__main__":
  app.run_server(debug = True)
