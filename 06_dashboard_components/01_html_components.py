from os import stat_result
import dash
import dash_html_components as html
import dash_core_components as dcc

# Instanciate the app
app = dash.Dash()

# Define style

# Define the layout
app.layout = html.Div(
  children = [
    "This is a div",
    html.Div(
      children = [
        "This is an inner div"
      ],
      style = dict(
        color = "red",
        border = "2px solid red"
      )
    ),
    html.Div(
      children = [
        "Another inner div!"
      ],
      style = dict(
        color = "blue",
        border = "2px solid blue"
      )
    )
  ],
  style = dict(
    color = "green",
    border = "2px solid green"
  )
)

# Run app
if __name__ == "__main__":
  app.run_server(debug = True)