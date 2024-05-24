class CountedIterator:
    def __init__(self, iterable):

        self.counter = 0
        self.iterator = iter(iterable)

    def get_count(self):
        return self.counter

    def __next__(self):
        next_item = next(self.iterator)
        self.counter += 1
        return next_item
