import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

# Instanciate the app
app = dash.Dash()

# Build the layout
app.layout = html.Div(
  [
    html.H1("Stock Ticker Dashboard"),
    html.H3("Enter a stock symbol"),
    html.Input(
      id = "stock-picker",
      values = "TSLA"
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
  # Update plot title
  fig = {
    "data": [
      {"x": [1, 2], "y": [3, 1]}
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
