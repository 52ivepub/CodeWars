url = 'https://www.codewars.com/kata/515bb423de843ea99400000a/train/python'


class PaginationHelper:

    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page

    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        if len(self.collection) % self.items_per_page == 0:
            return len(self.collection) // self.items_per_page
        else:
            return (len(self.collection) // self.items_per_page) + 1

    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        res, count = [], len(self.collection)
        while count >= self.items_per_page:
            res.append(self.items_per_page)
            count -= self.items_per_page
        res.append(count)
        if page_index in range(self.page_count()): return res[page_index]
        else: return -1

    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index not in range(len(self.collection)) or len(self.collection) == 0:
            return -1
        count = 0
        while item_index >= self.items_per_page:
            count += 1
            item_index -= self.items_per_page
        return count

Pag = PaginationHelper(['a','b','c','d','e','f'], 4)
print(Pag.page_item_count(1))