using SQLite

db = SQLite.DB("pinglog-sqlite3.db")
df = SQLite.query(db,"SELECT date, dest, ping FROM pinglog;")

df[:date] = map(x->Dates.unix2datetime(parse(Float32, x)), df[:date])
df[:ping] = map(x->parse(Float32, x), df[:ping])
df = df[df[:date] .> DateTime("2017-12-08"), :]
pings_to_google = df[df[:dest] .== "google.com", [:date, :ping]]
pings_to_router = df[df[:dest] .== "192.168.0.1", [:date, :ping]]

using PlotlyJS
using Plots
plotlyjs()

p1 = Plots.plot(
    pings_to_google[:date],
    pings_to_google[:ping],
    title="Ping logs from rpi3",
    label="google.com",
    color="red")
p2 = Plots.plot(
    pings_to_router[:date],
    pings_to_router[:ping],
    xlabel="Time [DateTime]",
    label="router",
    color="blue")
Plots.plot(p1, p2, layout=(2,1),
    link=:x,
    ylabel="Ping [ms]")
