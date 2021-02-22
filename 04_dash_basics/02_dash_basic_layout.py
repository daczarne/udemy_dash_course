import dash
import dash_html_components as html
import dash_core_components as dcc

# Instanciate the app
app = dash.Dash()

# Define de layout
app.layout = html.Div([
  html.H1("Hello Dash!"),
  html.Div("Dash: Web Dashboards with Python"),
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
        "title": "Bar plots!"
      }
    }
  )
])

# Run server
if __name__ == "__main__":
  app.run_server(debug = True)
