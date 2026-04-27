#!/usr/bin/env python3
"""Simple pagination"""
import csv
import math
from typing import Any, Dict, List, Tuple, Optional


def index_range(page, page_size) -> Tuple[int, int]:
    """Returns a tuple of size two containing a start index and an end index"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start,  end)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server with an empty dataset cache."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset loaded from CSV (header excluded)."""
        if self.__dataset is None:
            with open(self.DATA_FILE, newline="") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset, or an empty list if out of range."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        data = self.dataset()

        if start_index >= len(data):
            return []
        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Returns a dictionary containing the following key-value pairs:
                        page_size: the length of the returned dataset page
                        page: the current page number
                        data: the dataset page (equivalent to return from previous task)
                        next_page: the next page number, None if no next page
                        prev_page: the previous page number, None if no previous page
                        total_pages: the total number of pages in the dataset as an integer
                """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data_page = self.get_page(page, page_size)
        dataset_len = len(self.dataset())
        total_pages = math.ceil(dataset_len / page_size) if page_size else 0

        prev_page: Optional[int] = page - 1 if page > 1 else None
        next_page: Optional[int] = page + 1 if page < total_pages else None

        return {
            "page_size": len(data_page),
            "page": page,
            "data": data_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
