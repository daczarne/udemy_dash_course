import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd

# Load the data
df = pd.read_csv("gapminderDataFiveYear.csv")

YEARS = []
for year in df["year"].unique():
  YEARS.append({"label": str(year), "value": year})

# Instanciate the app
app = dash.Dash()

# Delfine the layout
app.layout = html.Div([
  dcc.Graph(
    id = "graph"
  ),
  dcc.Dropdown(
    id = "year-picker",
    options = YEARS,
    value = df["year"].min()
  )
])

# Build the callbacks
@app.callback(
  Output(component_id = "graph", component_property = "figure"),
  Input(component_id = "year-picker", component_property = "value")
)
def update_figure(selected_year):
  # Filter data
  filtered_df = df[df["year"] == selected_year]
  # Build the plot
  data = []
  for continent in filtered_df["continent"].unique():
    df_by_continent = filtered_df[filtered_df["continent"] == continent]
    data.append(
      go.Scatter(
        x = df_by_continent["gdpPercap"],
        y = df_by_continent["lifeExp"],
        mode = "markers",
        opacity = 0.7,
        marker = {
          "size": 15
        },
        name = continent
      )
    )
  # Define the layout
  layout = go.Layout(
    title = "Gapminder",
    xaxis = {
      "title": "GPD per capita",
      "type": "log"
    },
    yaxis = {
      "title": "Life expectancy"
    }
  )
  # Build the figure
  fig = go.Figure(
    data = data,
    layout = layout
  )
  # Return the figure
  return fig

# Run the app
if __name__ == "__main__":
  app.run_server(debug = True)
