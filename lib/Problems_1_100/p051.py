import time
from itertools import combinations

import numpy as np
from math import sqrt


def prime(m: int = 100) -> np.ndarray:
    p = np.arange(3, m + 1, 2)
    isp = np.ones((m - 1) // 2, dtype=bool)
    for f in p[:int(sqrt(m))]:
        if isp[(f - 2) // 2]: isp[(f * 3 - 2) // 2::f] = 0
    return np.insert(p[isp], 0, 2)


def ff(a: np.ndarray) -> np.ndarray:
    return np.fromiter(a[0], dtype='<U1')


def pe_p51() -> np.ndarray:
    lim = 1000000
    end = 8
    pn = prime(lim)

    for _c in range(4, str(lim).count('0')):
        _f, _t = pow(10, _c), pow(10, _c + 1)
        print(f'from {_f} to {_t}')
        p = pn[(pn >= _f) & (pn < _t)]
        p2d = np.apply_along_axis(ff, 1, p.astype(str)[:, np.newaxis]).astype(int)

        for i in range(2, _c - 1):
            cs = combinations([*range(_c + 1)], i)
            for c in cs:
                m = np.zeros(_c + 1, dtype=bool)
                m[..., c] = 1

                _ = p2d[:, m]
                _ia = np.where(np.argmin(_, axis=1) == np.argmax(_, axis=1))
                _av = p2d[_ia][:, ~m]
                vals, counts = np.unique(_av, return_counts=True, axis=0)

                if np.max(counts) >= end:
                    idx = np.all(p2d[_ia][..., ~m] == vals[np.where(counts == end)], axis=1)
                    return p2d[_ia][idx]


st = time.time()
print(pe_p51())
print(f"{time.time() - st} sec")