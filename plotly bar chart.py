## Testing out plotly for python ##

import plotly.express as px
import pandas as pd

entorno_alumbrado = pd.read_csv(r"entorno_alumbrado.csv")

# Generate base trace
fig = px.bar(
    entorno_alumbrado,
    x="depto",
    y="proporcion",
    color="group_by_var",
    color_discrete_sequence=px.colors.qualitative.Bold
)

# Update trace
fig.update_traces(
    hovertemplate="%{x}<br>" +
    "<b>Calles con alumbrado público:</b> %{y:.02%}" + "<extra></extra>"
)

# Title
fig.update_layout(
    title={
        'text': '<b>Calles con alumbrado público por depto</b>',
        'x': 0.5,
        'xanchor': 'center'
    }
)

# X axis
fig.update_layout(
    xaxis_type="category",
    xaxis=dict(
        title=""
    )
)

# Y axis
fig.update_layout(
    yaxis=dict(
        title="<b>Porcentaje</b>"
    ),
    yaxis_tickformat="%"
)

# Legend
fig.update_layout(
    legend=dict(
        title=dict(
            text="<b>¿Tiene alumbrado<br>público?</b>"
        ),
        orientation="h"
    )
)

# Background color
fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

# Modes and behaviours
fig.update_layout(
    barmode="stack",
    hovermode="x"
)

# Print plot
fig.show(
    config=dict({
        "displayModeBar": False
    })
)
