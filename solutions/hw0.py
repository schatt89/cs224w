def main():

    from quick_test import test
    test()

    import snap

    g = snap.LoadEdgeList(snap.PNGraph, '/Users/anna/Documents/repositories/cs224w/data/wiki-Vote.txt', 0, 1)

    n = g.GetNodes()
    print("Number of nodes is", n)

    loops = set()
    for e in g.Edges():
        if e.GetSrcNId == e.GetDstNId:
            loops.add(e.GetSrcNId)
    print("Number of nodes with loops is", len(loops))


if __name__ == "__main__":
    main()