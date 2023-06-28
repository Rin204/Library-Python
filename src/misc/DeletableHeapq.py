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
