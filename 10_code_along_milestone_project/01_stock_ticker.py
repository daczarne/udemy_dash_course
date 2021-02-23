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
    dcc.Input(
      id = "stock_picker",
      value = "TSLA"
    ),
    dcc.Graph(
      id = "graph",
      figure = {
        "data": [
          {"x": [1, 2], "y": [3, 1]}
        ]
      }
    )
  ]
)

# Run the app
if __name__ == "__main__":
  app.run_server(debug = True)
