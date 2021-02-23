import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

# Instanciate the app
app = dash.Dash()

# Build the layout
app.layout = html.Div(
  [
    html.H1(
      id = "live-update-text"
    ),
    dcc.Interval(
      id = "interval",
      interval = 2000,
      n_intervals = 0
    )
  ]
)

# Build callbacks
@app.callback(
  Output("live-update-text", "children"),
  Input("interval", "n_intervals")
)
def update_layout(n):
  return f"Crash free for {n} refreshes"

# Run the app
if __name__ == "__main__":
  app.run_server(debug = True)
