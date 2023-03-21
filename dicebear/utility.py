# MIT License
#
# Copyright (c) 2023 jvherck (on GitHub)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from string import ascii_lowercase, digits
from random import choices
from typing import Union, List, Annotated

from .avatar import DAvatar
from .models import DStyle, DOptions, _statsIncrease

__all__ = (
    'create_avatar',
    'bulk_create',
)
__filename__ = "utility.py"


def create_avatar(
    style: DStyle,
    seed: str,
    options: Union[DOptions, None] = None,
    customisations: Union[dict, None] = None,
    *,
    test: bool = False
) -> DAvatar:
    """
    Creates a DAvatar object and returns it.

    :param style: class `DStyle` :: the style of your avatar
    :param seed: class `str` :: the seed for the avatar; the avatar will be edited according to the seed
    :param options: class `DOptions` :: the options for the avatar
    :param customisations: class `dict` :: customisations for the specified avatar style
    :param test: class `bool` :: to indicate if you are currently testing or not
    :type test: bool
    :return: DAvatar object
    """
    _statsIncrease(__filename__, "/", ".create_avatar()", test)
    return DAvatar(style, seed, options=options, custom=customisations)


def bulk_create(
    style: DStyle = DStyle.random(),
    amount: Annotated[int, "Min: 1, Max: 50"] = 2,
    *,
    options: DOptions = None,
    custom: dict = None,
    test: bool = False
) -> List[DAvatar]:
    """
    Creates a list of :py:class:`DAvatar` objects. Easy way to make multiple of the same style (but different randomly generated seeds) at once.

    :param style: class `DStyle` :: the style to apply to all avatars
    :type style: dicebear.models.DStyle
    :param amount: class `int` :: the amount of DAvatars to create. Default: 2, Min: 1, Max: 50
    :type amount: int
    :param options: class `DOptions` :: options for the avatar
    :type options: dicebear.models.DOptions
    :param custom: class `dict` :: customisations for the specified style
    :type custom: dict
    :param test: class `bool` :: to indicate if you are currently testing or not
    :type test: bool
    :return: list[DAvatar] :: a list with DAvatar objects
    """
    if amount >= 50 or amount < 1: raise ValueError("argument `amount` must be between 1 and 50")
    _statsIncrease(__filename__, "/", ".bulk_create()", test)
    if style is None: style = DStyle.random()
    if custom is None: custom = {}
    if options is None: options = DOptions.empty
    result = []
    for _ in range(amount):
        av = DAvatar(style, "".join(choices(ascii_lowercase + digits, k=20)), options=options, custom=custom)
        result.append(av)
    return result
