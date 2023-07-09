# verification-helper: PROBLEM https://yukicoder.me/problems/1013
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from collections import deque


class AhoCorasick:
    def __init__(self, words=None):
        if words is None:
            self.words = []
        else:
            self.words = words

    def register(self, word):
        self.words.append(word)

    def build(self):
        self.children = [{}]
        self.match = [[]]

        for i, word in enumerate(self.words):
            self._register(i, word)

        self.failure = [0] * len(self.children)
        self._create_failure()

    def _register(self, i, word):
        k = 0
        for s in word:
            if s in self.children[k]:
                k = self.children[k][s]
            else:
                le = len(self.children)
                self.children[k][s] = le
                self.children.append({})
                self.match.append([])
                k = le

        self.match[k].append(i)

    def _create_failure(self):
        queue = deque(self.children[0].values())
        while queue:
            k = queue.popleft()
            b = self.failure[k]
            for s, j in self.children[k].items():
                self.failure[j] = self._next(b, s)
                self.match[j] += self.match[self.failure[j]]
                queue.append(j)

    def _next(self, k, s):
        while 1:
            if s in self.children[k]:
                return self.children[k][s]
            elif k == 0:
                return 0

            k = self.failure[k]

    def search(self, text):
        k = 0
        le = len(text)
        matched = [[] for _ in range(le)]
        for i, s in enumerate(text):
            k = self._next(k, s)
            for m in self.match[k]:
                matched[i - len(self.words[m]) + 1].append(m)

        return matched


S = input()
n = int(input())
ac = AhoCorasick()
for i in range(n):
    T = input()
    ac.register(T)

ac.build()
match = ac.search(S)
ls = len(S)
ans = 0
for row in match:
    ans += len(row)

print(ans)
