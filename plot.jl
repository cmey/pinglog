using SQLite

db = SQLite.DB("pinglog-sqlite3.db")
df = SQLite.query(db,"SELECT date, dest, ping FROM pinglog;")

using PlotlyJS
using Plots
plotlyjs()

Plots.plot(map(x->parse(Float32, x), df[:ping]))
