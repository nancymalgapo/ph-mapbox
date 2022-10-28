from flask import Flask, render_template

from ph_mapbox import plot_ph_cities

app = Flask(__name__)
app.config.from_object('config.Config')

@app.route("/", methods=['GET', 'POST'])
def ph_city_map():
    plot_ph_cities()
    return render_template("map_chart.html")


if __name__ == "__main__":
    app.run()
