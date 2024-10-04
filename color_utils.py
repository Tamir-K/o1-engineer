from termcolor import colored
from functools import partial, reduce
from enum import Enum


class Color(Enum):
    RED = "red"
    YELLOW = "yellow"
    BLUE = "blue"
    GREEN = "green"
    MAGENTA = "magenta"
    CYAN = "cyan"
    DARK_GREY = "dark_grey"
    ORANGE = "orange"


def compose(*funcs):
    """Compose multiple functions into a single function call"""
    def apply(x, fn):
        return fn(x)
    return lambda x: reduce(apply, funcs, x)


# coloring functions
colored_red = partial(colored, color=Color.RED.value)
colored_yellow = partial(colored, color=Color.YELLOW.value)
colored_blue = partial(colored, color=Color.BLUE.value)
colored_green = partial(colored, color=Color.GREEN.value)
colored_magenta = partial(colored, color=Color.MAGENTA.value)
colored_cyan = partial(colored, color=Color.CYAN.value)
colored_dark_grey = partial(colored, color=Color.DARK_GREY.value)

# print in color functions
print_in_red = compose(colored_red, print)
print_in_yellow = compose(colored_yellow, print)
print_in_blue = compose(colored_blue, print)
print_in_green = compose(colored_green, print)
print_in_magenta = compose(colored_magenta, print)
print_in_cyan = compose(colored_cyan, print)
