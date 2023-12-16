from node import BusRoute, BusStop, Direction


def get_bus_routes(root_node):
    """Returns a list of all bus routes."""
    routes = [r for r in root_node.children if isinstance(r, BusRoute)]
    return routes


def display_bus_routes(root_node):
    """Prints all bus routes."""
    routes = get_bus_routes(root_node)
    print("Here are the bus routes:")
    for route in routes:
        print(f"{route.data['rt']}: {route.data['rtnm']}")


def get_bus_stops(root_node):
    """Returns a list of all bus stops."""
    stops = [child for child in root_node.children if isinstance(child, BusStop)]
    return stops


def display_bus_stops(root_node):
    """Prints all bus stops."""
    stops = get_bus_stops(root_node)
    print("Here are the bus stops:")
    for stop in stops:
        print(f"{stop.data['stpid']}: {stop.data['stpnm']}")


def display_bus_directions(root_node):
    """Prints all directions for a given route."""
    directions = [child for child in root_node.children if isinstance(child, Direction)]
    print("Here are the directions")
    for dir in directions:
        print(f"{dir.data['name']}")
