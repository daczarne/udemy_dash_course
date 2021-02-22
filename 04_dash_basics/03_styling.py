import dash
import dash_html_components as html
import dash_core_components as dcc

# Instanciate the app
app = dash.Dash()

# Style
colors = {
  "background": "#111111",
  "text": "#7fdbff",
}

# Define de layout
app.layout = html.Div(
  children = [
    html.H1(
      children = "Hello Dash!",
      style = {
        "textAlign": "center",
        "color": colors["text"]
      }
    ),
    dcc.Graph(
      id = "example",
      figure = {
        "data": [
          {
            "x": [1, 2, 3],
            "y": [4, 1, 2],
            "type": "bar",
            "name": "SF"
          },
          {
            "x": [1, 2, 3],
            "y": [2, 4, 5],
            "type": "bar",
            "name": "NYC"
          }
        ],
        "layout": {
          "title": "Bar plots!",
          "plot_bgcolor": colors["background"],
          "paper_bgcolor": colors["background"],
          "font": {
            "color": colors["text"]
          }
        }
      }
    )
  ],
  style = {
    "backgroundColor": colors["background"]
  }
)

# Run server
if __name__ == "__main__":
  app.run_server(debug = True)
