class Network:
    def __init__(self, n_nodes):
        self.nodes = [Node() for _ in range(n_nodes)]
        self.connections = 
    
    def add_connection(self, n1: int, n2: int):
        self.nodes[n1].add_link(self.nodes[n2])
        self.nodes[n2].add_link(self.nodes[n1])
    
    def break_connection(self, n1: int, n2: int):
        self.nodes[n1].remove_link(n2)
        self.nodes[n2].remove_link(n1)

    def find_weakest_connection(self, agent: int) -> tuple[int, int]:
        # If A is on a gateway node, break connection
        if network[agent_node].is_gateway_adjacent:
            return agent_node, next(iter(network[agent_node].connected_gateways))

        for i, node in enumerate(self.nodes):
            if not node.is_gateway_adjacent or len(node.connected_gateways) < 2:
                continue

            return i, next(iter(network[agent_node].connected_gateways))
        return 

            
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
    network = Network(n_nodes)
    for i in range(n_links):
        n1, n2 = [int(j) for j in input().split()]
        network.add_connection(n1, n2)
        
    for i in range(n_exits):
        gateway = int(input())
        nodes[gateway].is_gateway = True
    return network

def main():
    network = initialize()
    while True:
        si = int(input()) 
        weakest_connection = network.find_weakest_connection(si)
        print(weakest_connection)
        network.break_connection(*weakest_connection)

