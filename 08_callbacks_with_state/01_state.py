import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

# Instanciate the app
app = dash.Dash()

# Delfine the layout
app.layout = html.Div([
  dcc.Input(
    id = "number-in",
    value = 1,
    style = dict(
      fontsize = 24
    )
  ),
  html.Button(
    id = "submit-btn",
    n_clicks = 0,
    children = "Click me!!",
    style = dict(
      fontsize = 24
    )
  ),
  html.H1(
    id = "number-out"
  )
])

# Build the callbacks
@app.callback(
  Output(component_id = "number-out", component_property = "children"),
  Input(component_id = "submit-btn", component_property = "n_clicks"),
  State(component_id = "number-in", component_property = "value")
)
def multiply(n_clicks, number):
  return f"{number} was typed in and btn was clicked {n_clicks} times"

# Run the app
if __name__ == "__main__":
  app.run_server(debug = True)
