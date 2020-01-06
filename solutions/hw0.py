def main():

    from quick_test import test
    test()

    import snap
    import numpy as np

    g = snap.LoadEdgeList(snap.PNGraph, '/Users/anna/Documents/repositories/cs224w/data/wiki-Vote.txt', 0, 1)
    
    print("#### Part 1 ####")

    n = g.GetNodes()
    print("Number of nodes is", n)

    n = snap.CntSelfEdges(g)
    print("Number of nodes with loops is", n)

    n = g.GetEdges()
    print("Number of directed edges is", n)

    reciprocal = [g.IsEdge(E.GetDstNId(), E.GetSrcNId()) for E in g.Edges()]
    print("Number of unordered edges is", np.sum(reciprocal))

    reciprocal = [g.IsEdge(E.GetDstNId(), E.GetSrcNId()) for E in g.Edges()]
    print("Number of reciprocal edges is", np.sum(reciprocal))

    DegToCntV = snap.TIntPrV()
    snap.GetOutDegCnt(g, DegToCntV)
    print("%d nodes with out-degree %d" % (DegToCntV[0].GetVal2(), DegToCntV[0].GetVal1()))

    DegToCntV = snap.TIntPrV()
    snap.GetInDegCnt(g, DegToCntV)
    print("%d nodes with in-degree %d" % (DegToCntV[0].GetVal2(), DegToCntV[0].GetVal1()))

    DegToCntV = snap.TIntPrV()
    snap.GetOutDegCnt(g, DegToCntV)
    count = 0
    for item in DegToCntV:
        if item.GetVal2() > 10:
            count += item.GetVal1()
    print("%d nodes with out-degree more than %d" % (count, 10))

    DegToCntV = snap.TIntPrV()
    snap.GetInDegCnt(g, DegToCntV)
    count = 0
    for item in DegToCntV:
        if item.GetVal2() > 10:
            count += item.GetVal1()
    print("%d nodes with in-degree more than %d" % (count, 10))

    print("#### Part 2 ####")

    snap.PlotOutDegDistr(g, "smdfn", 'dlfjdl')

if __name__ == "__main__":
    main()