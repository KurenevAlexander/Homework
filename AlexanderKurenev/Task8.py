class Pagination:

    def __init__(self, text, length_page):
        self.__text__ = text
        self.length_page = length_page
        self.item_count = len(self.__text__)
        self.__pages__ = [self.__text__[i:i + length_page] for i in range(0, self.item_count, length_page)]
        self.page_count = len(self.__pages__)

    def count_items_on_page(self, page):
        if 0 <= page < self.page_count:
            return len(self.__pages__[page])
        else:
            raise Exception(f'Invalid index. Page is missing')

    def display_page(self, page):
        if 0 <= page < self.page_count:
            return self.__pages__[page]
        else:
            raise Exception(f'Invalid index. Page is missing')

    def find_page(self, find_text):
        length_find_text = len(find_text)
        ind = 0
        page_nums = []
        while ind != -1:
            ind = self.__text__.find(find_text, ind)
            if ind >= 0:
                begin_page = ind // self.length_page
                end_page = (ind + length_find_text - 1) // self.length_page
                page_nums.extend(list(range(begin_page, end_page + 1)))
                ind += length_find_text
        if len(page_nums):
            return page_nums
        else:
            raise Exception(f"'{find_text}' is missing on the pages")


if __name__ == '__main__':
    pages = Pagination('Your beautiful text', 5)
    print(pages.page_count)
    print(pages.item_count)

    print(pages.count_items_on_page(0))
    print(pages.count_items_on_page(3))
    #print(pages.count_items_on_page(4))

    print(pages.display_page(0))
    print(pages.display_page(2))

    print(pages.find_page('Your'))
    print(pages.find_page('e'))
    print(pages.find_page('beautiful'))
    #print(pages.find_page('great'))
