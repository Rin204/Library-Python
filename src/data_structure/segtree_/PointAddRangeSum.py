from src.data_structure.SegmentTreeBase_ import SegmentTreeBase_


class PointAddRangeSum(SegmentTreeBase_):
    def e(self):
        return 0

    def ope(self, l, r):
        return l + r
