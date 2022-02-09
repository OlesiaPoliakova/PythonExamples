
class IsMultipleOf:
    def __init__(self, multi):
        self.multi = multi

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) % self.multi == 0
        return wrapper

@IsMultipleOf(3)
def multisum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

print(multisum(3, 1, k=3))




















