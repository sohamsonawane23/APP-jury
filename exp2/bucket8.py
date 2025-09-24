print("soham sonawane")


def print_count_decorator(func):
    def wrapper(self, value):
        print(f"Count before increment: {self._get_count()}")
        result = func(self, value)
        print(f"Count after increment: {self._get_count()}")
        return result

    return wrapper


class Counter:
    def __init__(self):
        self._count = 0

    def _get_count(self):
        return self._count

    @print_count_decorator
    def increment(self, value):
        # Closure to update count
        def add(val):
            nonlocal value
            self._count += val

        add(value)


# Example Usage:
counter = Counter()
counter.increment(5)
counter.increment(3)
