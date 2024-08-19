#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict[str, Union[int, List]]:
        assert index >= 0 and index < len(self.__dataset)
        _dict: Dict = {
            'index': index,
            'data': [],
            'page_size': page_size,
            'next_index': 0
            }
        temp_index: int = index
        next_index: int = index + page_size
        while temp_index < next_index:
            if temp_index in self.__indexed_dataset.keys():
                _dict['data'].append(self.__indexed_dataset[temp_index])
            else:
                next_index += 1
            temp_index += 1
        _dict['next_index'] = next_index
        return _dict
