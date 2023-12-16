import requests
from dotenv import load_dotenv
import os
from node import Node, BusStop, BusRoute, Direction

# setup
BASE_URL = "https://mbus.ltp.umich.edu/bustime/api/v3"
load_dotenv()  # load API key from .env file
API_KEY = os.environ.get("API_KEY")


def generate_graph():
    """Returns a graph of all bus routes, directions, and stops."""
    print("Fetching routes...")
    # get all Blue Bus routes
    res = requests.get(
        f"{BASE_URL}/getroutes?key={API_KEY}&format=json"
    )
    routes = res.json()["bustime-response"]["routes"]

    # create a root node
    root = Node(None)
    route_map = {}

    # add all routes to the root node
    for route in routes:
        route_node = BusRoute(route)
        route_map[route["rt"]] = route_node
        root.add_child(route_node)

    print("Fetching directions...")

    directions_map = {}
    # get all directions
    for rt in route_map:
        res = requests.get(
            f"{BASE_URL}/getdirections?key={API_KEY}&rt={rt}&format=json&rtpidatafeed=bustime"
        )
        directions = res.json()["bustime-response"]["directions"]

        for dir in directions:
            if dir["id"] not in directions_map:
                dir_node = Direction(dir)
                directions_map[dir["id"]] = dir_node
                root.add_child(dir_node)
            route_map[rt].add_child(directions_map[dir["id"]])


    print("Fetching stops...")
    # get all stops for each route
    stop_map = {}
    for rt in route_map:
        directions = [child for child in route_map[rt].children if isinstance(child, Direction)]
        for dir in directions:
            res = requests.get(
                f"{BASE_URL}/getstops?key={API_KEY}&rt={rt}&format=json&dir={dir.data['id']}&rtpidatafeed=bustime"
            )

            # skip if there is an error
            if "error" in res.json()["bustime-response"]:
                continue

            stops = res.json()["bustime-response"]["stops"]
        
            for stop in stops:
                if stop["stpid"] not in stop_map:
                    stop_node = BusStop(stop)
                    stop_map[stop["stpid"]] = stop_node
                    root.add_child(stop_node)
                else:
                    stop_node = stop_map[stop["stpid"]]

                # Add edge between route and stop
                route_map[rt].add_child(stop_node)
                stop_node.add_child(route_map[rt])

                # Add edge from root
                root.add_child(stop_node)
    return root, route_map, routes
