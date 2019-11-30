"""
Logit link function implementation
"""

# author: Benjamin Cross
# email: btcross26@yahoo.com
# created: 2019-08-26


import numpy as np

from .base_class import BaseLink


class LogitLink(BaseLink):
    def _link(self, y: np.ndarray) -> np.ndarray:
        return np.log(y / (1.0 - y))

    def _inverse_link(self, nu: np.ndarray) -> np.ndarray:
        return 1.0 / (1.0 + np.exp(-nu))

    def dydnu(self, y: np.ndarray) -> np.ndarray:
        return y * (1.0 - y)

    def d2ydnu2(self, y: np.ndarray) -> np.ndarray:
        return self.dydnu(y) * (1.0 - 2.0 * y)