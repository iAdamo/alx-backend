#!/usr/bin/env python3
"""Simple helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple of size two containing the start index and the end index
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


# res = index_range(1, 7)
# print(type(res))
# print(res)
#
# res = index_range(page=3, page_size=15)
# print(type(res))
# print(res)
