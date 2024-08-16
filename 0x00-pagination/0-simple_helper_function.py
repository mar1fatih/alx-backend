#!/usr/bin/env python3
"""pagination script"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ return a tuple of size two containing a start and end index """
    start_idx: int = 0
    end_idx: int = 0

    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size

    return (start_idx, end_idx)
