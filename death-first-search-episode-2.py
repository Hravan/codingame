import sys
from collections import deque


class Network:
    def __init__(self, n_nodes):
        self.nodes = {n: set() for n in range(n_nodes)}
        self.gateways = set()
    
    def connect_nodes(self, a, b):
        self.nodes[a].add(b)
        self.nodes[b].add(a)
    
    def add_gateaway(self, n):
        self.gateways.add(n)
    
    def __repr__(self):
        return f'Nodes: {self.nodes!r}, Gateaways: {self.gateways!r}, '
    
    def severe_connection(self, a, b):
        self.nodes[a].remove(b)
        self.nodes[b].remove(a)
    
    def gateway_paths(self, start_node):
        paths = []
        for gateaway in self.gateways:
            shortest_path = self.shortest_path(start_node, gateaway)
            if shortest_path is not None:
                paths.append(shortest_path)
        return paths
    
    def shortest_path(self, start_node, end_node):
        to_visit = deque([start_node])
        node_to_parent = {}
        while to_visit:
            current_node = to_visit.popleft()
            for child in self.nodes[current_node]:
                if child in node_to_parent:
                    continue
                to_visit.append(child)
                node_to_parent[child] = current_node
                if child == end_node:
                    return path_from_parent_mapping(start_node, end_node, node_to_parent)
    
    def all_gateway_paths(self, start_node):
        paths = []
        for g in self.gateways:
            paths.extend(self.paths(start_node, g))
        return paths

    def paths(self, start_node, end_node):
        to_visit = deque([start_node])
        node_to_parent = {}
        paths = []
        while to_visit:
            current_node = to_visit.popleft()
            for child in self.nodes[current_node]:
                if child in node_to_parent:
                    continue
                to_visit.append(child)
                node_to_parent[child] = current_node
                if child == end_node:
                    path = path_from_parent_mapping(start_node, end_node, node_to_parent)
                    paths.append(path)
        return paths
    
    def node_to_gateways(self):
        return {node: [child for child in children if child in self.gateways] for node, children in self.nodes.items()}
    
    def most_frequent_gateway_connection(self):
        node_to_gateways = self.node_to_gateways()
        most_frequent_node = max(node_to_gateways, key=lambda x: len(node_to_gateways[x]))
        return most_frequent_node, node_to_gateways[most_frequent_node]
    
    def gateway_connections(self):
        from collections import defaultdict
        connections = defaultdict(list)
        for node, children in self.nodes.items():
            for g in self.gateways:
                if g in children:
                    connections[node].append(g)
        return connections


def path_from_parent_mapping(start_node, end_node, node_to_parent):
    path = []
    current_node = end_node
    while current_node != start_node:
        path.append(current_node)
        current_node = node_to_parent[current_node]
    path.append(start_node)
    return path[::-1]


def select_nodes(network, si):
    paths = network.gateway_paths(si)
    shortest_len = min(len(path) for path in paths)
    if shortest_len == 2:
        paths = [path for path in paths if len(path) == shortest_len]
        path = paths[0]
        return path[0], path[1]
    elif shortest_len == 3:
        # paths = [path for path in paths if len(path) == shortest_len]
        penultimate_nodes = [path[-2] for path in paths]
        penultimate_node_with_most_connections = max(penultimate_nodes, key=penultimate_nodes.count)
        with_most_connections_node = [path for path in paths if path[-2] == penultimate_node_with_most_connections]
        selected_path = min(with_most_connections_node, key=len)
        return selected_path[-2], selected_path[-1]
    else:
        node, gateways = network.most_frequent_gateway_connection()
        return node, gateways[0]


n_nodes, n_links, n_exits = [int(i) for i in input().split()]
network = Network(n_nodes)
for i in range(n_links):
    n1, n2 = [int(j) for j in input().split()]
    network.connect_nodes(n1, n2)
    
for i in range(n_exits):
    ei = int(input())  # the index of a gateway node
    network.add_gateaway(ei)


while True:
    si = int(input())
    paths = network.all_gateway_paths(si)
    print(paths, file=sys.stderr)
    for path in sorted(paths, key=len):
        print(path, file=sys.stderr)
        if len(path) == 2:
            print(path[-2], path[-1])
            network.severe_connection(path[-2], path[-1])
            break
        else:
            connections = network.gateway_connections()
            max_connections_node = max(connections, key=lambda x: len(connections[x]))
            print(max_connections_node, connections[max_connections_node][0])
            network.severe_connection(max_connections_node, connections[max_connections_node][0])
            break
    # nodes = select_nodes(network, si)
    # network.severe_connection(nodes[0], nodes[1])
    # print(f"{nodes[0]} {nodes[1]}")
