# Nearby-Earthquakes Controller API:

This is a connector to the earthquakes API to show 10 most nearby earthquakes (earthquakes that happened in the closest proximity of given city).

- Controller api will pull the earthquakes data (place, coordinates) from [Earthquakes API](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson)
- The Earthquakes API info can be found [here](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php)
- Controller api smartly pulls the data calculate the distance and display 10 most nearby earthquakes

## Installations:

## Using docker

Install [docker](https://docs.docker.com) and [docker compose](https://docs.docker.com/compose)

Then run the following cmd from the root folder to start the controller api

     docker-compose up

or to start the app in the background

     docker-compose -d

## Manually

Please use the following steps to run the api manually

1. Install [python 3.8](https://www.python.org/downloads) or higher
2. Install and create new isolated [conda env](https://docs.conda.io/en/latest/miniconda.html) or [python virtual env](https://docs.python.org/3/tutorial/venv.html) and activate it
3. Then from /api run `pip install -r requirements.txt`. it will install all required dependency
4. From /api run `python controller.py` to start the controller api

## Usage

1. Open any web browser and go to http://localhost:8610
2. Enter 'latitude' (between -90 to 90) and 'longitude' (between -180 to 180) values (only numeric values up to six decimal places are allowed)
3. After entering values click on 'Calculate' button (and then wait) to get list of 10 most nearby earthquakes
4. For next calculation please click back in browser and repeat steps 2 and 3

## Important:

The steps here for the controller api is to start and run development server. For the Production Deployment of the dockerized api using k8s please [refer](https://docs.docker.com/get-started/kube-deploy).
