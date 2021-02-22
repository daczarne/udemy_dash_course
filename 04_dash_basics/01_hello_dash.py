import dash
import dash_html_components as html
import dash_core_components as dcc

# Instanciate the app
app = dash.Dash()

# Define de layout
app.layout = html.Div([
  html.H1("Hello Dash!")
])

# Run server
if __name__ == "__main__":
  app.run_server(debug = True)
