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
    
    DegToCntV = snap.TIntPrV()
    snap.GetOutDegCnt(g, DegToCntV)
    count = []
    degree = []
    for item in DegToCntV:
        count.append(item.GetVal2())
        degree.append(item.GetVal1())

    count = np.log10(np.array(count))
    degree = np.log10(np.array(degree))

    degree = degree[1:]
    count = count[1:]
    
    import matplotlib.pyplot as plt

    plt.plot(degree, count, '-ro')
    plt.title("Out-degree distribution")
    plt.ylabel("log of count")
    plt.xlabel("log of out-degree")
    #plt.show()
    
    ## polyfit 

    z = np.polyfit(count, degree, deg = 1)

    y = count * z[0] + z[1]

    plt.plot(degree, count, '-ro')
    plt.plot(y, count, '-b')
    plt.title("Out-degree distribution")
    plt.ylabel("log of count")
    plt.xlabel("log of out-degree")
    #plt.show()

    print(z)

    print("#### Part 3 ####")

    g = snap.LoadEdgeList(snap.PNGraph, '/Users/anna/Documents/repositories/cs224w/data/stackoverflow-Java.txt', 0, 1)
    Components = snap.TCnComV()
    snap.GetWccs(g, Components)
    print("Number of weakly-connected components is", len(Components))

    MxWcc = snap.GetMxWcc(g)
    print("Number of edges in the maximal weakly connected component is", MxWcc.GetEdges())
    print("Number of nodes in the maximal weakly connected component is", MxWcc.GetNodes())

    PRankH = snap.TIntFltH()
    snap.GetPageRank(g, PRankH)
    nodes = []
    pgr = []
    for item in PRankH:
        nodes.append(item)
        pgr.append(PRankH[item])
    nodes = np.array(nodes)
    pgr = np.array(pgr)
    
    print("The nodes with indices", nodes[np.argpartition(pgr, -3)[-3:]], "are the most center with the following PageRank values respectively:")
    print(pgr[np.argpartition(pgr, -3)[-3:]])
    

if __name__ == "__main__":
    main()