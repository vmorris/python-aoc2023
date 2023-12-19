import networkx as nx
import matplotlib.pyplot as plt
import math
from itertools import cycle

from aoc2023.util import get_input


def build_digraph(mappings):
    digraph = nx.DiGraph()
    nodes_edges = {}
    for mapping in mappings:
        node, edges = mapping.split("=")
        node = node.strip()
        nodes_edges[node] = []
        for edge in edges.replace("(", "").replace(")", "").split(","):
            nodes_edges[node].append(edge.strip())
    digraph.add_nodes_from(nodes_edges.keys())
    for node in nodes_edges.keys():
        edges = nodes_edges[node]
        digraph.add_edge(node, edges[0], d="left")
        digraph.add_edge(node, edges[1], d="right")
    return digraph


def draw_digraph(digraph):
    #pos = nx.shell_layout(digraph)
    #nx.draw_shell(digraph, with_labels=True)
    #nx.draw_networkx_edge_labels(digraph, pos)
    #pos = nx.random_layout(digraph)
    #nx.draw_random(digraph, with_labels=True)
    #nx.draw_networkx_edge_labels(digraph, pos)
    pos = nx.circular_layout(digraph)
    nx.draw_networkx_edge_labels(digraph, pos)
    nx.draw_circular(digraph, with_labels=True)
    plt.show()


def traverse_edge(digraph, node, direction):
    if direction == "R":
        direction = "right"
    elif direction == "L":
        direction = "left"
    view = digraph.adj.get(node)
    # handle case where left and right go to same destination node
    if len(view.items()) == 1:
        direction = "right"
    destination = None
    for i in view.items():
        if i[1].get("d") == direction:
            destination = i[0]
    return destination


def solve_part1(entries):
    directions = cycle(entries.pop(0))
    entries.pop(0)
    digraph = build_digraph(entries)
    #print(list(digraph.nodes))
    #print(list(digraph.edges))
    #import pdb
    #pdb.set_trace()
    current_node = "AAA"
    steps = 0
    for d in directions:
        print(current_node)
        current_node = traverse_edge(digraph, current_node, d)
        steps += 1
        if current_node == "ZZZ":
            break
    return steps


def solve_part2(entries):
    directions = cycle(entries.pop(0))
    entries.pop(0)
    digraph = build_digraph(entries)
    #import pdb
    #pdb.set_trace()
    current_nodes = [n for n in digraph.nodes() if n.endswith("A")]
    node_steps = []
    steps = 0
    for d in directions:
        if len(current_nodes) == 0:
            break
        new_nodes = []
        for node in current_nodes:
            new_nodes.append(traverse_edge(digraph, node, d))
        steps += 1
        current_nodes = new_nodes
        for idx, node in enumerate(current_nodes):
            if node.endswith("Z"):
                print(f"node: {node}, index: {idx}, steps: {steps}")
                current_nodes.pop(idx)
                node_steps.append(steps)
    return math.lcm(*node_steps)


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2023/day08/input")
    #print(solve_part1(entries))
    print(solve_part2(entries))