import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import csv

# Set auth
with open("credentials.csv") as f:
  reader = csv.reader(f, delimiter = ",")
  credentials = []
  for line in reader:
    credentials.append(line)

USERNAME_PASSWORD_PAIRS = credentials

# Instanciate the app
app = dash.Dash()

# Check login pairs
auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD_PAIRS)

# Build the app layout
app.layout = html.Div(
  [
    dcc.RangeSlider(
        id = "range-slider",
        min = -5,
        max = 6,
        marks = {i: str(i) for i in range(-5, 7)},
        value = [-3, 4]
    ),
    html.H1(id = "product")  # this is the output
  ],
  style = {"width": "50%"}
)

# Define the callbacks
@app.callback(
    Output("product", "children"),
    Input("range-slider", "value")
)
def update_value(value_list):
    return value_list[0] * value_list[1]

# Run the app
if __name__ == '__main__':
    app.run_server()
