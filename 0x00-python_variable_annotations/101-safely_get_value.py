#!/usr/bin/env python3
"""
More involved type annotations
"""

from typing import Any, Mapping, Optional, TypeVar, Union

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Optional[T] = None
) -> Union[Any, T]:
    """
    Using TypeVar to add type annotations to a function
    """
    if key in dct:
        return dct[key]
    else:
        return default
