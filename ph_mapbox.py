# This script is just a sample code to use plotly for mapping PH cities

import pandas as pd
import plotly.express as px
import plotly.offline


def plot_ph_cities():
    ph_cities = pd.read_csv("ph.csv")
    fig = px.scatter_mapbox(ph_cities, lat="lat", lon="lng", hover_name="city", hover_data=["population"],
                            color_discrete_sequence=["fuchsia"], zoom=5, height=800)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    plotly.offline.plot(fig, filename="map_chart.html", auto_open=False)
