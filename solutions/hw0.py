def main():

    from quick_test import test
    test()

    import snap

    g = snap.LoadEdgeList(snap.PNGraph, '/Users/anna/Documents/repositories/cs224w/data/wiki-Vote.txt', 0, 1)

    CntV = snap.TIntPrV()
    snap.GetOutDegCnt(g, CntV)
    for p in CntV:
         print("degree %d: count %d" % (p.GetVal1(), p.GetVal2()))

if __name__ == "__main__":
    main()