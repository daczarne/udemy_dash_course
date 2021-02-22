import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

# Instanciate the app
app = dash.Dash()

# Delfine the layout
app.layout = html.Div(
  children = [
    dcc.RangeSlider(
      id = "selected-values",
      min = -10,
      max = 10,
      marks = {i: str(i) for i in range(-10, 11)},
      value = [-1, 1]
    ),
    html.H1(
      id = "result"
    )
  ]
)

# Build the callbacks
@app.callback(
  Output(component_id = "result", component_property = "children"),
  Input(component_id = "selected-values", component_property = "value")
)
def multiply(selected_values):
  return selected_values[0] * selected_values[1]

# Run the app
if __name__ == "__main__":
  app.run_server(debug = True)
