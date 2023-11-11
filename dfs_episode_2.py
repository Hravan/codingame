from collections import defaultdict


def print_err(*args):
    import sys

    print(*args, file=sys.stderr)


class Network:
    def __init__(self):
        self.pregateways = defaultdict(list)
        self.gateways = defaultdict(list)
        self.rigid_connections = defaultdict(set)

    def add_rigid_connection(self, n1: int, n2: int):
        self.rigid_connections[n1].add(n2)
        self.rigid_connections[n2].add(n1)

    def break_connection(self, n1: int, n2: int):
        self.gateways[n1].remove(n2)
        self.pregateways[n2].remove(n1)
        if not self.gateways[n1]:
            del self.gateways[n1]
        if not self.pregateways[n2]:
            del self.pregateways[n2]

    def find_weakest_connection(self, agent_node: int) -> tuple[int, int]:
        # If agent is on a pregateway node, break connection
        if agent_node in self.pregateways:
            return self.pregateways[agent_node][-1], agent_node

        for pregateway, gateways in sorted(
            self.pregateways.items(), key=lambda x: len(x[1]), reverse=True
        ):
            if len(gateways) < 2:
                # There are no nodes with more than 2 gateway connections, return current node
                break

            is_unsafe = self.is_unsafe(agent_node, pregateway)
            if is_unsafe:
                break
        return gateways[-1], pregateway

        # elif there are 2-gateway nodes
        # if A is next to a domino path leading to a 2 gateway node, break one of these 2 connections
        # elif A is 2 steps to a 2 gateway node, break one off these 2 connections
        # else break one of the 2-gateway node connections
        # else break any connection

    def is_unsafe(self, agent_node, pregateway, visited=None):
        if visited is None:
            visited = set([pregateway])
        else:
            visited.add(pregateway)
        to_visit = set(self.rigid_connections[pregateway])
        for node in to_visit:
            if node in visited:
                continue
            if node == agent_node:
                break
            if node not in self.pregateways:
                continue
            return self.is_unsafe(agent_node, node, visited)
        else:
            return False
        return True


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
        else:
            network.add_rigid_connection(connection[0], connection[1])

    return network


def main():
    network = initialize()
    while True:
        si = int(input())
        n1, n2 = network.find_weakest_connection(si)
        print(n1, n2)
        network.break_connection(n1, n2)


main()
