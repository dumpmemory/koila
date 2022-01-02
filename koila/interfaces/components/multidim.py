from __future__ import annotations

import functools
import operator
from abc import abstractmethod
from typing import Protocol, Tuple, overload


class MultiDimensional(Protocol):
    def __len__(self) -> int:
        return self.size(0)

    def dim(self) -> int:
        return len(self.size())

    @property
    def ndim(self) -> int:
        return self.dim()

    ndimension = ndim

    @overload
    @abstractmethod
    def size(self) -> Tuple[int, ...]:
        ...

    @overload
    @abstractmethod
    def size(self, dim: int) -> int:
        ...

    @abstractmethod
    def size(self, dim: int | None = None) -> int | Tuple[int, ...]:
        ...

    @property
    def shape(self) -> Tuple[int, ...]:
        return self.size()

    def numel(self) -> int:
        return functools.reduce(operator.mul, self.shape, 1)
