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
    # Stock ticker selector
    html.Div(
      [
        html.H3(
          "Enter a stock symbol",
          style = {
            "paddingRight": "30px"
          }
        ),
        dcc.Input(
          id = "stock-picker",
          value = "TSLA",
          style = {
            "fontSize": 24,
            "width": 75
          }
        )
      ],
      style = {
        "display": "inline-block",
        "verticalAlign": "top"
      }
    ),
    # Date range selector
    html.Div(
      [
        html.H3(
          "Select a start and end date",
          style = {
            "paddingRight": "30px"
          }
        ),
        dcc.DatePickerRange(
          id = "date-picker",
          min_date_allowed = datetime(2015, 1, 1),
          max_date_allowed = datetime.today(),
          start_date = datetime(2018, 1, 1),
          end_date = datetime.today()
        )
      ],
      style = {
        "display": "inline-block"
      }
    ),
    # Plot
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
  Input(component_id = "stock-picker", component_property = "value"),
  Input(component_id = "date-picker", component_property = "start_date"),
  Input(component_id = "date-picker", component_property = "end_date")
)
def update_graph(stock_ticker, start_date, end_date):
  # Get the data
  start = datetime.strptime(start_date[:10], "%Y-%m-%d")
  end = datetime.strptime(end_date[:10], "%Y-%m-%d")
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
