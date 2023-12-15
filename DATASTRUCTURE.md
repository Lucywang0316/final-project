# README file data structure
This project uses a graph to represent the bus stops, bus routes and bus directions retrieved from the MBus API.
## Nodes
We have 3 different nodes: bus stop, bus route, and bus direction
## Edges
We have edges between related nodes. For instance, each bus route will have an edge to the bus stop that the route serves.
## Graph traversal
We traverse the graph using the edge to return the appropriate bus stops for each route. This then allows us to use the correct ID to request for predictions of the next bus from the MBus API.