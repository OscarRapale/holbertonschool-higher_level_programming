class CountedIterator:
    def __init__(self, iterable):

        self.counter = 0
        self.iterator = iter(iterable)

    def get_count(self):
        return self.counter

    def __next__(self):
        self.counter += 1
        return next(self.iterator)