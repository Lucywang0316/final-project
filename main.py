from graph import generate_graph
from info import display_bus_routes, display_bus_stops, display_bus_directions
from prediction import get_prediction

# main
if __name__ == '__main__':
    print("Welcome to the MBus tool!")
    print("Fetching data from API...")
    root, route_map, routes = generate_graph()

    while True:
        option = input("Enter 1 to get predictions, 2 to get routes, or 3 to get bus stops, and 4 to get bus directions: ")
        if option == "1":
            get_prediction(routes, route_map)
        elif option == "2":
            display_bus_routes(root)
        elif option == "3":
            display_bus_stops(root)
        elif option == "4":
            display_bus_directions(root)
        else:
            print("Invalid option. Please try again.")
        exit = input("Enter q to quit or any other key to continue: ")
        if exit == "q":
            break
