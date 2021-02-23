import dash
import dash_html_components as html

# Define variables
crash_free = 0
crash_free += 1

# Instanciate the app
app = dash.Dash()

# Build the layout
app.layout = html.H1(
  f"Crash free for {crash_free} refreshes"
)

# Run the app
if __name__ == "__main__":
  app.run_server(debug = True)
