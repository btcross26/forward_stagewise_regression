"""
Student's t function implementation
"""

# author: Benjamin Cross
# email: btcross26@yahoo.com
# created: 2019-08-26

from typing import Optional

import numpy as np

from .base_class import BaseLoss


class StudentTLoss(BaseLoss):
    """
    Student's t loss function class

    The math is likely wrong here...need to check before finalizing
    """

    def __init__(self, scale: Optional[float] = None, dof: int = 2):
        super().__init__()
        self.nu_ = dof
        self.scale_ = (dof + 1.0) / 2.0 if scale is None else scale

    def __call__(self, yt: np.ndarray, yp: np.ndarray) -> np.ndarray:
        return self._loss(yt, yp)

    def _loss(self, yt: np.ndarray, yp: np.ndarray) -> np.ndarray:
        return self.scale_ * np.log(1.0 + (yt - yp) ** 2 / self.nu_)

    def dldyp(self, yt: np.ndarray, yp: np.ndarray) -> np.ndarray:
        return -2.0 * self.scale_ * (yt - yp) / (self.nu_ + (yt - yp) ** 2)

    def d2ldyp2(self, yt: np.ndarray, yp: np.ndarray) -> np.ndarray:
        left_term_du = -2.0 * self.scale_ / (self.nu_ + (yt - yp) ** 2)
        right_term_du = (
            4.0 * self.scale_ * ((yt - yp) ** 2) / ((self.nu_ + (yt - yp) ** 2) ** 2)
        )
        return -(left_term_du + right_term_du)
