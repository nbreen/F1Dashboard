import fastf1 as f1
import cudf as cf
import plotly.express as px
import dash_table as dt

from dash.dependencies import Input, Output, State
from f1Analytics import app
from data import raceWeekends

@app.callback(Output('track-temp', 'figure'),
              Output('race-results', 'children'),
              Input('race-select', 'value'))
def update_session(weekendIndex):
    race = raceWeekends[weekendIndex].get_race()
    laps = race.load_laps()
    raceWeather = cf.from_pandas(race.weather_data)
    figTitle = 'Track temp during ' + raceWeekends[weekendIndex].name
    raceWeather['MeasurementTime'] = cf.to_datetime(race.date) + raceWeather['Time']
    raceResults = cf.DataFrame(race.results)
    raceResults = raceResults[['number', 'position', 'positionText', 'points']]
    figure = px.line(raceWeather.to_pandas(), 'MeasurementTime', 'TrackTemp', title=figTitle)
    table = dt.DataTable(id='results-table',
                         columns=[{"name": i, "id" : i} for i in raceResults.columns],
                         data=raceResults.to_pandas().to_dict('records'))

    return figure, table