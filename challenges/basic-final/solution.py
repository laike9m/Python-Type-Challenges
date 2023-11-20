"""
TODO:

Make sure `my_list` cannot be re-assigned to.
"""

from typing import Final


my_list: Final = []

## End of your code ##
my_list.append(1)
my_list = []  # expect-type-error
my_list = "something else"  # expect-type-error
