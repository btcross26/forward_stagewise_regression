"""
Custom type hints for use in various places of module
"""

# Author: Benjamin Cross
# email: btcross26@yahoo.com
# created: 2019-11-15


from __future__ import annotations

import numpy as np

# import Protocol and self return type type hints depending on Python version
try:  # pre-Python 3.8
    from typing_extensions import Protocol
except ImportError:  # prior to Python 3.8
    from typing import Protocol as Protocol  # type: ignore


class Model(Protocol):
    def fit(self, X: np.ndarray, y: np.ndarray) -> Model:
        pass

    def predict(self, X: np.ndarray) -> np.ndarray:
        pass


class ActivationCallback(Protocol):
    def __call__(self, yp: np.ndarray) -> np.ndarray:
        pass


class WeightsCallback(Protocol):
    def __call__(self, yt: np.ndarray, yp: np.ndarray) -> np.ndarray:
        pass
