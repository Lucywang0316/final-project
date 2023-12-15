from graph import generate_graph
from prediction import prompt_user

# main
if __name__ == '__main__':
    print("Welcome to the MBus next bus estimator!")
    print("Fetching data from API...")
    root, route_map, routes = generate_graph()
    prompt_user(routes, route_map)
