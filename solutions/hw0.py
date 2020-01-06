def main():

    from quick_test import test
    test()

    import snap
    import numpy as np

    g = snap.LoadEdgeList(snap.PNGraph, '/Users/anna/Documents/repositories/cs224w/data/wiki-Vote.txt', 0, 1)

    n = g.GetNodes()
    print("Number of nodes is", n)

    loops = set()
    for e in g.Edges():
        if e.GetSrcNId() == e.GetDstNId():
            loops.add(e.GetSrcNId())
    n = snap.CntSelfEdges(g)
    print("Number of nodes with loops is", n)

    n = g.GetEdges()
    print("Number of directed edges is", n)

    reciprocal = [g.IsEdge(E.GetDstNId(), E.GetSrcNId()) for E in g.Edges()]
    print("Number of reciprocal edges is", np.sum(reciprocal))


if __name__ == "__main__":
    main()