class Node:
    """Node class for graph."""
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)


class BusStop(Node):
    """Node class for bus stops."""
    def __init__(self, data):
        super().__init__(data)


class Direction(Node):  
    """Node class for bus directions."""
    def __init__(self, data):
        super().__init__(data)


class BusRoute(Node):
    """Node class for bus routes."""
    def __init__(self, data):
        super().__init__(data)
