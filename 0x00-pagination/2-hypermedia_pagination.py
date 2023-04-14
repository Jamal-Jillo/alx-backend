#!/usr/bin/env python3
"""Simple pagination."""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cache dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> tuple:
        """Return a tuple of size two with a start index and an end index."""
        start = ((page - 1) * page_size)
        end = page * page_size
        return (start, end)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset.

        (i.e. the correct list of rows)
        based on the page and page_size parameters.
        """
        assert isinstance(page, int) and page > 0, "page must be a positive \
            integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must \
            be a positive"

        dataset = self.dataset()
        start_index, end_index = self.index_range(page, page_size)

        if start_index >= len(dataset):
            return []
        else:
            return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Return a dictionary containing the following key-value pairs:.

        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        dataset = self.get_page(page, page_size)  # Get dataset
        dataset_len = len(self.dataset())  # Get dataset length
        total_pages = math.ceil(dataset_len / page_size)  # Total num of pages

        # Check if page is less than total_pages
        if page + 1 <= total_pages:
            next_page = page + 1
        else:
            next_page = None

        # Check if page is greater than 1
        if page - 1 >= 1:
            prev_page = page - 1
        else:
            prev_page = None

        return {
            'page_size': len(dataset),
            'page': page,
            'data': dataset,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
