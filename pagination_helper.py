"""https://www.codewars.com/kata/515bb423de843ea99400000a 5 kyu"""

from math import floor, ceil


class PaginationHelper:
    def __init__(self, collection, items_per_page: int):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        """returns the number of items within the entire collection"""
        return len(self.collection)

    def page_count(self):
        """returns the number of pages"""
        return ceil(len(self.collection) / self.items_per_page)

    def page_item_count(self, page_index: int):
        """returns the number of items on the current page. page_index is zero based"""
        page = len(self.collection) - page_index * self.items_per_page
        return -1 if page <= 0 else min(page, self.items_per_page)

    def page_index(self, item_index):
        """determines what page an item is on. Zero based indexes."""
        if item_index >= len(self.collection) or item_index < 0:
            return -1

        return floor(item_index / self.items_per_page)
