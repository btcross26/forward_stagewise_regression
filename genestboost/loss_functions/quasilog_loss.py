"""
QuasiLogLoss function implementation
"""

# author: Benjamin Cross
# email: btcross26@yahoo.com
# created: 2019-10-16

from typing import Callable

import numpy as np

from .base_class import BaseLoss


class QuasiLogLoss(BaseLoss):
    """
    QuasiLogLoss loss function class
    """

    def __init__(
        self,
        vt_callback: Callable[[np.ndarray], np.ndarray],
        d0_n: int = 100,
        d2_eps: float = 1e-12,
    ):
        super().__init__()
        self._vt_callback = vt_callback
        self._d0_n = d0_n + (d0_n % 2)
        self._d2_eps = d2_eps

    def _loss(self, yt: np.ndarray, yp: np.ndarray) -> np.ndarray:
        # use Simpson's rule to numerically integrate
        dims = tuple([1] * yp.ndim + [-1])
        x = np.linspace(0.0, 1.0, self._d0_n + 1).reshape(dims)
        iwts = np.hstack(
            [[1.0], np.tile([4.0, 2.0], (self._d0_n - 2) // 2), [4.0, 1.0]]
        ).reshape(dims)
        ipts = np.expand_dims(yp, axis=-1) + np.expand_dims(yt - yp, axis=-1) * x
        values = np.sum(self.dldyp(np.expand_dims(yt, axis=-1), ipts) * iwts, axis=-1)
        values = values * (yp - yt) / (3.0 * self._d0_n)
        return values

    def dldyp(self, yt: np.ndarray, yp: np.ndarray) -> np.ndarray:
        return -(yt - yp) / self._vt_callback(yp)

    def d2ldyp2(self, yt: np.ndarray, yp: np.ndarray) -> np.ndarray:
        v1 = self.dldyp(yt, yp - self._d2_eps)
        v2 = self.dldyp(yt, yp + self._d2_eps)
        return (v2 - v1) / (2.0 * self._d2_eps)
