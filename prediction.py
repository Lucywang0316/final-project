import requests
from dotenv import load_dotenv
import os
from node import BusStop
import datetime


# setup
BASE_URL = "https://mbus.ltp.umich.edu/bustime/api/v3"
load_dotenv()  # load API key from .env file
API_KEY = os.environ.get("API_KEY")


def get_next_bus(rt, stop):
    """Returns a list of predictions for the next bus at a given stop on a given route."""
    res = requests.get(
        f"{BASE_URL}/getpredictions?key={API_KEY}&rt={rt}&format=json&stpid={stop}&rtpidatafeed=bustime"
    )
    return res.json()["bustime-response"]["prd"]


def get_prediction(routes, route_map):
    """Prompts the user for a route and stop, then prints the next bus arrival time."""
    # prompt user for route
    print()
    print("Here are the bus routes:")
    for route in routes:
        print(f"{route['rt']}: {route['rtnm']}")
    rt = input("To get started, enter a bus route code: ")

    # prompt user for stop
    print()
    print("Here are the stops for that route:")
    # Traverse the tree to get all stops for the given route
    stops = [child for child in route_map[rt].children if isinstance(child, BusStop)]
    for stop in stops:
        print(f"{stop.data['stpid']}: {stop.data['stpnm']}")
    stop = input("Enter a stop ID: ")

    # get predictions
    print("Fetching predictions for next bus...")
    predictions = get_next_bus(rt, stop)
    if len(predictions) == 0:
        print("No predictions found.")
    else:
        formatted_est_time = datetime.datetime.strptime(predictions[0]["prdtm"], "%Y%m%d %H:%M")
        print("The next bus will arrive at", formatted_est_time.strftime("%I:%M %p"))

