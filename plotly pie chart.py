entorno_alumbrado_mvdeo = entorno_alumbrado["depto"] == 1

fig2 = px.pie(
    entorno_alumbrado[entorno_alumbrado_mvdeo],
    values="proporcion",
    names="group_by_var"
)

fig2.show()
