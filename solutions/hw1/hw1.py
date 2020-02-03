def main():

    import snap
    import numpy as np
    import matplotlib.pyplot as plt
    import random

    # Setup
    erdosRenyi = None
    smallWorld = None
    collabNet = None


    # Problem 1.1
    def genErdosRenyi(N=5242, E=14484):
        """
        :param - N: number of nodes
        :param - E: number of edges

        return type: snap.PUNGraph
        return: Erdos-Renyi graph with N nodes and E edges
        """
        ############################################################################
        # TODO: Your code here!
        Graph = None

        nodes = np.arange(N)
        edges = []
        for i in range(len(nodes)):
            possible = nodes[np.arange(len(nodes))!=i]
            #node_edges = []
            #for j in range(len(possible)):
            node_edges = np.column_stack((np.full(len(possible), nodes[i]), possible))
            #node_edges.append(edge)
            edges += node_edges
        edges = set(frozenset(k) for k in edges)
        edges = list(edges)
        edges = random.choices(edges, k = E)


        ############################################################################
        return edges 
    erdosRenyi = genErdosRenyi()
    print(len(erdosRenyi))

if __name__ == "__main__":
    main()