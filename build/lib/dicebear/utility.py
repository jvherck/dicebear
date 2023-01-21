# MIT License
#
# Copyright (c) 2022 jvherck (https://jvherck.github.io/dicebear/)
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

from . import DFormat, DStyle, DOptions, DAvatar
from string import ascii_lowercase, digits
from random import choices
import typing


def create_avatar(style: DStyle, seed: str, options: typing.Union[DOptions, None], customisations: typing.Union[dict, None]) -> DAvatar:
    return DAvatar(style, seed, options=options, custom=customisations)


def bulk_create(style: DStyle = DStyle.random(), amount: typing.Annotated[int, "Min: 1, Max: 1000"] = 2, *, format: DFormat = DFormat.png, options: DOptions = None, custom: dict = None) -> typing.List[DAvatar]:
    """
    Creates a list of :py:class:`DAvatar` objects. Easy way to make multiple of the same style (but different randomly generated seeds) at once.

    :param style: class `DStyle` :: the style to apply to all avatars
    :type style: dicebear.DStyle
    :param amount: class `int` :: the amount of DAvatars to create. Default: 2, Min: 1, Max: 1000
    :type amount: int
    :param format: class `DFormat` :: the format for the generated avatars
    :type format: dicebear.DFormat
    :param options: class `DOptions` :: options for the avatar
    :type options: dicebear.DOptions
    :param custom: class `dict` :: customisations for the specified style
    :type custom: dict
    :return: list[DAvatar] :: a list with DAvatar objects
    """
    if amount > 1000 or amount < 1: raise ValueError("argument `amount` must be between 1 and 1000")
    if style is None: style = DStyle.random()
    if custom is None: custom = {}
    if options is None: options = DOptions.empty
    result = []
    for _ in range(amount):
        av = DAvatar(style, "".join(choices(ascii_lowercase + digits, k=20)), options=options, custom=custom)
        result.append(av.url_svg if format == DFormat.svg else DFormat.png)
    return result
