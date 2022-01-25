class IncorrectColor(Exception):
    def __init__(self, wrong_color: str = None):
        super().__init__('Incorrect color given: "{}" is not an html hex code! (example: #ffffff)'.format(wrong_color))


class InvalidOption(Exception):
    def __init__(self, wrong_option: str = None):
        super().__init__('Invalid option given: "{}" is not an existing option! (use `Avatar.options` to get all possible options)'.format(
            wrong_option))
