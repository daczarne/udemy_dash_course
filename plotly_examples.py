
# import plotly.express as px
# fig = px.scatter(
#    x=[0, 1, 2, 3, 4],
#    y=[0, 1, 4, 9, 16]
# )
# fig.show()

import plotly.express as px
import pandas as pd

entorno_alumbrado = pd.read_csv(r"entorno_alumbrado.csv")

entorno_alumbrado_yes = entorno_alumbrado["group_by_var"] == "Sí"
fig = px.bar(
    entorno_alumbrado,
    x="depto",
    y="proporcion",
    color="group_by_var"
    # hover_name="depto"
)
fig.update_layout(
    title="Proporción de calles con alumbrado público por depto",
    xaxis_type="category",
    yaxis=dict(
        title="<b>Porcentaje</b>"
    ),
    yaxis_tickformat="%",
    barmode="stack",
    hovermode="x unified"
)
fig.show()
