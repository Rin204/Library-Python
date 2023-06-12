from src.data_structure.SegmentTreeBase_ import SegmentTreeBase_


class PointAddRangeSum(SegmentTreeBase_):
    def ope(self, l, r):
        return l + r

    def e(self):
        return 0
