import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import requests

# Instanciate the app
app = dash.Dash()

# Counter list
counter_list = []

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
        # Counter
        html.Pre(
          id = "counter-text",
          children = "Active flights worldwide"
        ),
        # Counter graph
        dcc.Graph(
          id = "live-updates-graph",
          style = {
            "width": 1200
          }
        ),
        # Interval tracker
        dcc.Interval(
          id = "interval-comp",
          interval = 6000,
          n_intervals = 0
        )
      ]
    )
  ]
)

# Updates information
@app.callback(
  Output("counter-text", "children"),
  Input("interval-comp", "n_intervals")
)
def update_layout(n):
  # Get data
  url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&stats=1"
  res = requests.get(url, headers = {"User-Agent": "Mozilla/5.0"})
  data = res.json()
  counter = 0
  for element in data["stats"]["total"]:
    counter =+ data["stats"]["total"][element]
  # Update counter list
  counter_list.append(counter)
  # Return
  return f"Active flights worldwide: {counter}"

# Update the graph
@app.callback(
  Output("live-update-graph", "figure"),
  Input("interval-comp", "n_intervals")
)
def update_graph(n):
  # Build the figure
  fig = go.Figure(
    data = [
      go.Scatter(
        x = list(range(len(counter_list))),
        y = counter_list,
        mode = "lines+markers"
      )
    ]
  )
  # Return the figure
  return fig

# Run the app
if __name__ == "__main__":
  app.run_server(debug = True)
