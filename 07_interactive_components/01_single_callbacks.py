import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

# Instanciate the app
app = dash.Dash()

# Delfine the layout
app.layout = html.Div([
  dcc.Input(
    id = "input-id",
    value = "Initial text",
    type = "text"
  ),
  html.Div(
    id = "output-div"
  )
])

# Build the callbacks
@app.callback(
  Output(component_id = "output-div", component_property = "children"),
  Input(component_id = "input-id", component_property = "value")
)
def update_text(input_text):
  return f"You entered: {input_text}"

# Run the app
if __name__ == "__main__":
  app.run_server(debug = True)
