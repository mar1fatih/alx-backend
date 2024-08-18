#!/usr/bin/env python3
""" pagination script """
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple:
    """ return a tuple of size two containing a start index and an end index """
    start_idx: int = 0
    end_idx: int = 0

    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size

    return (start_idx, end_idx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page method"""
        assert type(page) == type(page_size) == int and page > 0 and page_size > 0
        tuple_idx: Tuple = index_range(page, page_size)
        new_list: List = []
        data_set: Server = self.dataset()
        try:
            for i in range(tuple_idx[0], tuple_idx[1]):
                new_list.append(data_set[i])
            return new_list
        except IndexError:
            return []
