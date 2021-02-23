import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import requests

# Instanciate the app
app = dash.Dash()

# Build the layout
app.layout = html.Div(
  [
    html.Div(
      [
        html.Iframe(
          src = "https://www.flightradar24.com",
          height = 500,
          width = 1200
        )
      ]
    ),
    html.Div(
      [
        html.Pre(
          id = "counter-text",
          children = "Active flights worldwide"
        ),
        dcc.Interval(
          id = "interval-comp",
          interval = 6000,
          n_intervals = 0
        )
      ]
    )
  ]
)

# Build the callbacks
@app.callback(
  Output("counter-text", "children"),
  Input("interval-comp", "n_intervals")
)
def update_layout(n):
  url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&stats=1"
  res = requests.get(url, headers = {"User-Agent": "Mozilla/5.0"})
  data = res.json()
  counter = 0
  for element in data["stats"]["total"]:
    counter =+ data["stats"]["total"][element]
  return f"Active flights worldwide: {counter}"

# Run the app
if __name__ == "__main__":
  app.run_server(debug = True)
