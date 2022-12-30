import numpy as np
import requests
from flask import Flask, jsonify, render_template, request
from geopy import distance

app = Flask(__name__)
__author__ = "nikspandya2@gmail.com"

earthquake_api_url = (
    "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def calculate_distance():
    # Get user entered lat/log data using post request
    input_latitude = request.form["latitude"]
    input_longitude = request.form["longitude"]

    # Pull the last 30 days earthquake data from earthquake api
    api_response = requests.get(earthquake_api_url)

    if api_response.status_code == 200:
        data_json = api_response.json()
        features = data_json.get("features")
        earthquakes = []
        input_location = (float(input_latitude), float(input_longitude))
        for entry in features:
            place = entry.get("properties").get("place")
            coordinates = entry.get("geometry").get("coordinates")
            earthquake_location = (coordinates[1], coordinates[0])
            # Calculate distance between given city and each of the earthquake locations
            distance_ = np.round(
                distance.great_circle(input_location, earthquake_location).km
            )
            earthquak = {"place": place, "distance": distance_}
            earthquakes.append(earthquak)

        # Remove duplicate entries of earthquakes
        list_without_duplicates = [
            dict(t) for t in {tuple(d.items()) for d in earthquakes}
        ]
        # Sort earthquake entries based on closest distance to input location
        sorted_list_of_earthquakes = sorted(
            list_without_duplicates, key=lambda d: d["distance"]
        )

        return (
            render_template("show-data.html", data=sorted_list_of_earthquakes[:10]),
            200,
        )

    else:
        return jsonify({"message": "Earthquake api not responding"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=8610, host="0.0.0.0")
