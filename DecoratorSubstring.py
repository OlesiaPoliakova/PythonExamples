

class TextInjection:
    def __init__(self, substring, new_substring):
        self.substring = substring
        self.new_substring = new_substring

    def __call__(self, func):
        def wrapper(arg):
            new_string = arg.replace(self.substring, self.new_substring)
            return func(new_string)
        return wrapper

@TextInjection('Java', 'Python')
def text_constructor(text_substring):
    return f"Java is awesome and {text_substring}"

print(text_constructor('super'))
