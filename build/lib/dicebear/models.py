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
import sys
import traceback

from .errors import *
from random import choice, choices
class FindPil:
    """Not important for you, just makes things easier for me on the back-end ;)"""
    found: bool = True

_ascii_lowercase = "abcdef"
_incorrect_lowercase = "ghijklmnopqrstuvwxyz"
_digits = "0123456789"

options = all_options = ["dataUri", "flip", "rotate", "scale", "radius", "size", "backgroundColor", "translateX", "translateY"]
styles = ["adventurer", "adventurer-neutral", "avataaars", "big-ears", "big-ears-neutral",
          "big-smile", "bottts", "croodles", "croodles-neutral", "identicon", "initials",
          "micah", "miniavs", "open-peeps", "personas", "pixel-art", "pixel-art-neutral"]
styles_depricated = ["female", "gridy", "human", "jdenticon", "male"]


class DColor:
    """
    Base class for DAvatar's colors.
    """
    def __init__(self, html_code: str = "#ffffff"):
        """
        Colors used in this package. This uses HTML color codes!

        :param html_code: class `str` :: the html color code to use as color (default: #ffffff)
        :type html_code: str
        :raise dicebear.errors.IncorrectColor:
        """
        if html_code in ["random", "rnd"]:
            html_code = '#' + ''.join(choices(_ascii_lowercase+_digits, k=6))
        if not html_code.startswith("#"):
            html_code = "#" + html_code
        if len(html_code) not in [4, 7] or any(x in html_code for x in _incorrect_lowercase):
            raise IncorrectColor(str(html_code))
        self.html_code: str = str(html_code)

    def __str__(self):
        return f"{self.html_code}"
    def __repr__(self):
        return f"{self.html_code}"
    def __eq__(self, other):
        return self.html_code == other.html_code
    def __ne__(self, other):
        return self.html_code != other.html_code

    @staticmethod
    def random():
        """
        Get a random html code.

        :return: class `dicebear.models.DColor`
        """
        return DColor('#' + ''.join(choices(_ascii_lowercase + _digits, k=6)))


class DStyle:
    """
    All possible styles for the avatars. Visit https://avatars.dicebear.com/styles to see what they look like.\n
    - Note: Only works with attributes!
    """
    list = all_styles = styles
    adventurer = styles[0]
    adventurer_neutral = styles[1]
    avataaars = styles[2]
    big_ears = styles[3]
    big_ears_neutral = styles[4]
    big_smile = styles[5]
    bottts = styles[6]
    croodles = styles[7]
    croodles_neutral = styles[8]
    identicon = styles[9]
    initials = styles[10]
    micah = styles[11]
    miniavs = styles[12]
    open_peeps = styles[13]
    personas = styles[14]
    pixel_art = styles[15]
    pixel_art_neutral = styles[16]

    def __init__(self):
        """Only use `.attribute` to use a style."""
        pass

    @staticmethod
    def random():
        """
        Get a random style.
        """
        return choice(styles)

    @staticmethod
    def from_str(style_str: str):
        """
        Get an avatar style from a string.

        :param style_str: class `str` :: the string to convert to a DStyle
        :type style_str: str
        """
        return eval("DStyle.{}".format(style_str.replace("-", "_")))


class DFormat:
    """
    All possible image formats for saving or converting avatars.
    - Note: Only works with attributes!
    """
    list = all_formats = ["png", "svg"]
    png = "png"
    svg = "svg"
    def __init__(self):
        """Only use `.attribute` to use a format."""
        pass

    @staticmethod
    def from_str(format_str: str):
        """
        Get an avatar format from a string

        :param format_str: class `str` :: the string to convert to a DFormat
        :type format_str: str
        """
        return eval("DFormat.{}".format(format_str))


default_options: dict = {options[0]: False, options[1]: False, options[2]: 0, options[3]: 100, options[4]: 0,
             options[5]: 0, options[6]: DColor(), options[7]: 0, options[8]: 0}

class DOptions(dict):
    """
    The options class for :py:class:`dicebear.avatar.DAvatar`
    """
    empty: dict = {}
    default_options = default = default_options
    def __init__(self, *, dataUri: bool = False, flip: bool = False, rotate: int = 0, scale: int = 100,
                 radius: int = 0, size: int = 0, backgroundColor: DColor = DColor(), translateX: int = 0, translateY: int = 0, **kwargs):
        """
        Go to https://github.com/jvherck/dicebear#base-options to see all info (important for minimum and maximum values for each option!)

        :param kwargs: `fromdict` to use a custom dict instead of args (if you use this kwarg all other args will be neglected)
        """
        # kwargs: list = [dataUri, flip, rotate, scale, radius, size, backgroundColor, translateX, translateY]
        dic = kwargs.get("fromdict", {})
        current: dict = {"dataUri": dataUri, "flip": flip, "rotate": rotate, "scale": scale, "radius": radius, "size": size,
                     "backgroundColor": backgroundColor, "translateX": translateX, "translateY": translateY}
        if dic:
            for item in dic:
                if item not in default_options.keys() or dic[item] == default_options[item]:
                    dic.pop(item, None)
        else: # if not dic
            for item in current:
                if item in default_options and current[item] != default_options[item]:
                    dic.update({item: current[item]})
        if "size" in dic and dic["size"] == 0:
            dic.pop("size")
        super().__init__(dic)

    @property
    def _ver(self):
        return type(self)



def pilcheck(func):
    """Decorator to check if package Pillow is installed"""
    def wrapper(*args, **kwargs):
        if FindPil.found is True:
            return func(*args, **kwargs)
        else:
            log_error(PILError())
    return wrapper
