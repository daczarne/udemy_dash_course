import dash
import dash_html_components as html

# Instanciate the app
app = dash.Dash()

# Define global variable
crash_free = 0

def refresh_layout():
  global crash_free
  crash_free += 1
  return html.H1(f"Crash free for {crash_free} refreshes")

# Build the layout
app.layout = refresh_layout

# Run the app
if __name__ == "__main__":
  app.run_server(debug = True)
