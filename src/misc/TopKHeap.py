from src.misc.DeletableHeapq import DeletableHeapq


class TopKHeap:
    def __init__(self, K, reverse=False, A=None):
        self.K = K
        if not reverse:
            self.upp = DeletableHeapq()
            self.low = DeletableHeapq(reverse=True)
        else:
            self.upp = DeletableHeapq(reverse=True)
            self.low = DeletableHeapq()

        if A is not None:
            for a in A:
                self.push(a)

    def __len__(self):
        return len(self.upp) + len(self.low)

    @property
    def tot(self):
        return self.upp.tot

    @property
    def sum(self):
        return self.upp.sum

    def push(self, x):
        self.upp.push(x)
        if len(self.upp) > self.K:
            self.low.push(self.upp.pop())

    def remove(self, x):
        if len(self.low) > 0 and x <= self.low[0]:
            self.low.remove(x)
        else:
            self.upp.remove(x)
            if len(self.low) > 0:
                self.upp.push(self.low.pop())
