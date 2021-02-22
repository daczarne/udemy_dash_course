from os import stat_result
import dash
import dash_html_components as html
import dash_core_components as dcc

# Instanciate the app
app = dash.Dash()

# Define style

# Define the layout
app.layout = html.Div([
  html.Label("Dropdown"),
  dcc.Dropdown(
    options = [
      dict(label = "New York City", value = "NYC"),
      dict(label = "San Francisco", value = "SF")
    ],
    value = "SF"
  ),
  html.Label("Slider"),
  dcc.Slider(
    min = -10,
    max = 10,
    step = 0.5,
    marks = {i: str(i) for i in range(-10, 11)},
    value = 0
  ),
  html.Label("Radio items"),
  dcc.RadioItems(
    options = [
      dict(label = "New York City", value = "NYC"),
      dict(label = "San Francisco", value = "SF")
    ],
    value = "SF"
  )
])

# Run app
if __name__ == "__main__":
  app.run_server(debug = True)
