import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import os
import pandas_datareader.data as web
import pandas as pd
from datetime import datetime

# Read data
nsdq = pd.read_csv("NASDAQcompanylist.csv")
nsdq.set_index("Symbol", inplace = True)

options = []
for ticker in nsdq.index:
  dict_values = {}
  dict_values["label"] = str(nsdq.loc[ticker]["Name"]) + " " + ticker
  dict_values["value"] = ticker
  options.append(dict_values)


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
        dcc.Dropdown(
          id = "stock-picker",
          options = options,
          value = ["TSLA"],
          multi = True
        )
      ],
      style = {
        "display": "inline-block",
        "verticalAlign": "top",
        "width": "30%"
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
    # Submit Btn
    html.Div(
      [
        html.Button(
          id = "submit-btn",
          n_clicks = 0,
          children = "Submit",
          style = {
            "fontSize": 24,
            "marginLeft": "30px"
          }
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
  Input(component_id = "submit-btn", component_property = "n_clicks"),
  State(component_id = "stock-picker", component_property = "value"),
  State(component_id = "date-picker", component_property = "start_date"),
  State(component_id = "date-picker", component_property = "end_date")
)
def update_graph(n_clicks, stock_ticker, start_date, end_date):
  # Parse the dates
  start = datetime.strptime(start_date[:10], "%Y-%m-%d")
  end = datetime.strptime(end_date[:10], "%Y-%m-%d")
  # Build the traces 
  traces = []
  for tic in stock_ticker:
    df = web.DataReader(tic, "iex", start, end)
    traces.append(
      {"x": df.index, "y": df["close"], "name": tic}
    )
  # Build the figure
  fig = {
    "data": traces,
    "layout": {
      "title": stock_ticker
    }
  }
  # Return fig
  return fig

# Run the app
if __name__ == "__main__":
  app.run_server(debug = True)
