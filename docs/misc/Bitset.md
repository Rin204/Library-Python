---
title: Bitset
documentation_of: ././expansion/misc/Bitset.py
---

# 概要
C++ の bitset を真似したものです．

## 使い方
<details><summary> std::bitset 対応表 </summary>

[参考](https://cpprefjp.github.io/reference/bitset/bitset.html)

| std::bitset | 自作Bitset |
| --- | --- |   
| `operator&` | `__and__` |
| `operator&=` | `__iand__` |
| `operator\|` | `__or__` |
| `operator\|=` | `__ior__` |
| `operator^` | `__xor__` |
| `operator^=` | `__ixor__` |
| `operator<<` | `__lshift__` |
| `operator<<=` | `__ilshift__` |
| `operator>>` | `__rshift__` |
| `operator>>=` | `__irshift__` |
| `set` | `__setitem__(k=1)` |
| `reset()` | なし |
| `reset(size_t pos)` | `__setitem__(k=0)` |
| `operator~`, `flip()` | なし |
| `flip(size_t pos)` | `rev` |
| `operator[]` | `__getitem__` |
| `count` | `count`, `__sum__` |
| `size` | `__len__`, `.size` |
| `test` | `__getitem__` |
| `all` | `count == size` |
| `any` | `count != 0` |
| `none` | `count == 0` |
| `to_ulong`, `to_ullong` | なし |
| `to_string` | `__str__` |
| `operator==`, `operator!=` | なし |
| なし | `resize` |
| なし | `and_count` |
| なし | `or_count` |
| なし | `xor_count` |

</details>
