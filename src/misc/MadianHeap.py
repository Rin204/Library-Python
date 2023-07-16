from src.misc.DeletableHeapq import DeletableHeapq


class MedianHeap:
    def __init__(self, A=None):
        self.upp = DeletableHeapq()
        self.low = DeletableHeapq(reverse=True)

        if A is not None:
            for a in A:
                self.push(a)

    def __len__(self):
        return len(self.upp) + len(self.low)

    def push(self, x):
        if len(self.upp) == len(self.low) + 1:
            self.upp.push(x)
            self.low.push(self.upp.pop())
        else:
            self.low.push(x)
            self.upp.push(self.low.pop())

    def get_med(self):
        """
        A = [1, 2, 3] -> [2, 2] を返す
        A = [1, 2, 3, 4] -> [2, 3] を返す
        """
        if len(self.upp) == len(self.low):
            return [self.low[0], self.upp[0]]
        else:
            return [self.upp[0], self.upp[0]]

    def remove(self, x):
        if x <= self.low[0]:
            self.low.remove(x)
            if len(self.low) + 1 < len(self.upp):
                self.low.push(self.upp.pop())
        else:
            self.upp.remove(x)
            if len(self.upp) < len(self.low):
                self.upp.push(self.low.pop())

    def abs_sum(self):
        if len(self) == 0:
            return 0

        med = self.upp[0]
        ret = med * len(self.low) - self.low.tot
        ret += self.upp.tot - med * len(self.upp)
        return ret
