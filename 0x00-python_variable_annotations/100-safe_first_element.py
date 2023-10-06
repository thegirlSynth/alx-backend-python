#!/usr/bin/env python3
"""
Duck typing - first element of a sequence
"""

from typing import Any, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    The types of the elements of the input are not known
    """
    if lst:
        return lst[0]
    else:
        return None
