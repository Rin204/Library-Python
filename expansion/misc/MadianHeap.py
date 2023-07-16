import heapq


class DeletableHeapq:
    def __init__(self, lst=None, reverse=False):
        if reverse:
            self.pm = -1
        else:
            self.pm = 1
        if lst is None:
            self.hq = []
        else:
            self.hq = [self.pm * x for x in lst]

        heapq.heapify(self.hq)
        self.tot = sum(self.hq) * self.pm
        self.cnt = {}
        for x in self.hq:
            self.cnt[x] = self.cnt.get(x, 0) + 1
        self.length = len(self.hq)

    def __bool__(self):
        return bool(self.hq)

    def __len__(self):
        return self.length

    @property
    def sum(self):
        return self.tot

    def top(self):
        if self.hq:
            return self.hq[0] * self.pm
        else:
            return None

    def __getitem__(self, i):
        # 先頭要素にアクセスしたいときのみ
        assert i == 0
        return self.top()

    def push(self, x):
        self.length += 1
        self.cnt[x * self.pm] = self.cnt.get(x * self.pm, 0) + 1
        self.tot += x
        heapq.heappush(self.hq, x * self.pm)

    def pop(self):
        if not self.hq:
            return None
        self.length -= 1
        x = heapq.heappop(self.hq)
        self.cnt[x] -= 1
        self.tot -= x * self.pm
        self._delete()
        return x * self.pm

    def remove(self, x):
        if self.cnt.get(x * self.pm, 0) == 0:
            return False
        self.length -= 1
        self.cnt[x * self.pm] -= 1
        self.tot -= x
        self._delete()
        return True

    def _delete(self):
        while self.hq and self.cnt.get(self.hq[0], 0) == 0:
            heapq.heappop(self.hq)


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
