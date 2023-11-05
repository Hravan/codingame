from collections import defaultdict


def print_err(*args):
    import sys

    print(*args, file=sys.stderr)


class Network:
    def __init__(self):
        self.pregateways = defaultdict(list)
        self.gateways = defaultdict(list)

    def add_connection(self, n1: int, n2: int):
        self.nodes[n1].add_link(self.nodes[n2])
        self.nodes[n2].add_link(self.nodes[n1])

    def break_connection(self, n1: int, n2: int):
        self.gateways[n1].remove(n2)
        self.pregateways[n2].remove(n1)
        if not self.gateways[n1]:
            del self.gateways[n1]
        if not self.pregateways[n2]:
            del self.pregateways[n2]

    def add_gateway(self, gateway: int):
        for i, node in enumerate(self.nodes):
            if gateway in node.linked_to:
                self.gateways[gateway].add(i)

    def find_weakest_connection(self, agent_node: int) -> tuple[int, int]:
        # If agent is on a pregateway node, break connection
        if agent_node in self.pregateways:
            return self.pregateways[agent_node][-1], agent_node

        for pregateway, gateways in sorted(
            self.pregateways.items(), key=lambda x: len(x[1]), reverse=True
        ):
            if len(gateways) < 2:
                # There are no nodes with more than 2 gateway connections, return current node
                return gateways[-1], pregateway
            return gateways[-1], pregateway

        # elif there are 2-gateway nodes
        # if A is next to a domino path leading to a 2 gateway node, break one of these 2 connections
        # elif A is 2 steps to a 2 gateway node, break one off these 2 connections
        # else break one of the 2-gateway node connections
        # else break any connection


class Node:
    def __init__(self):
        self.linked_to = set()
        self.connected_gateways = set()

    @property
    def is_gateway_adjacent(self):
        return bool(self.connected_gateways)

    def add_link(self, node: int):
        self.linked_to.add(node)

    def remove_link(self, node: int):
        self.linked_to.remove(node)
        self.connected_gateways.remove(node)

    def link_gateway(self, gateway: int):
        self.connected_gateways.add(gateway)


def initialize():
    n_nodes, n_links, n_exits = [int(i) for i in input().split()]
    connections = set()
    for i in range(n_links):
        n1, n2 = [int(j) for j in input().split()]
        # network.add_connection(n1, n2)
        connections.add((n1, n2))

    gateways = set()
    for i in range(n_exits):
        gateway = int(input())
        gateways.add(gateway)

    network = Network()
    for connection in connections:
        if connection[0] in gateways:
            network.gateways[connection[0]].append(connection[1])
            network.pregateways[connection[1]].append(connection[0])
        elif connection[1] in gateways:
            network.gateways[connection[1]].append(connection[0])
            network.pregateways[connection[0]].append(connection[1])

    return network


def main():
    network = initialize()
    while True:
        si = int(input())
        n1, n2 = network.find_weakest_connection(si)
        print(n1, n2)
        network.break_connection(n1, n2)


main()
