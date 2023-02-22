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
import typing
from random import choice, choices

from .errors import *


class _FindPil:
    """Not important for you, just makes things easier for me on the back-end ;)"""
    found: bool = True

_ascii_lowercase = "abcdef"
_incorrect_lowercase = "ghijklmnopqrstuvwxyz"
_digits = "0123456789"

options = all_options = ["flip", "rotate", "scale", "radius", "size", "backgroundColor", "backgroundType",
                         "backgroundRotation", "translateX", "translateY", "randomizeIds"]
styles = ["adventurer", "adventurer-neutral", "avataaars", "avataaars-neutral", "big-ears", "big-ears-neutral",
          "big-smile", "bottts", "bottts-neutral", "croodles", "croodles-neutral", "fun-emoji", "icons",
          "identicon", "initials", "lorelei", "lorelei-neutral", "micah", "miniavs", "open-peeps", "personas",
          "pixel-art", "pixel-art-neutral", "shapes", "thumbs"]
# styles_depricated = ["female", "gridy", "human", "jdenticon", "male"]


class DColor:
    """
    Base class for DAvatar's colors.
    """

    def __init__(self, html_code: Union[str, typing.List[str]] = "transparent"):
        """
        Colors used in this package. This uses HTML/hex color codes!

        :param html_code: class `str` :: the html color code to use as color. This can be a list of strings if `backgroundType` has been set to "gradientLinear". (default: transparent)
        :type html_code: str
        :raise dicebear.errors.IncorrectColor: if the given html_code is an invalid hex color
        """
        code_list: list = None
        hex_list: list = []
        if type(html_code) == str: code_list = html_code.replace(" ", "").split(",")
        elif type(html_code) == list and all(type(x) == str for x in html_code): code_list = html_code
        for code in code_list:
            if code.startswith("#"): code = code.replace("#", "")
            if (len(code) != 6 or any(x in code for x in _incorrect_lowercase)) and code != "transparent":
                raise IncorrectColor(str(code))
            hex_list.append(code)
        self.html_code: str = ",".join(hex_list)

    def __str__(self): return f"{self.html_code}"
    def __repr__(self): return f"{self.html_code}"
    def __eq__(self, other):
        if type(other) == str: return self.html_code == other
        return self.html_code == other.html_code
    def __ne__(self, other):
        if type(other) == str: return self.html_code != other
        return self.html_code != other.html_code

    @staticmethod
    def random():
        """
        Get a random html code.

        :return: class `dicebear.models.DColor`
        """
        return DColor(''.join(choices(_ascii_lowercase + _digits, k=6)))


class DStyle:
    """
    All possible styles for the avatars. Visit https://avatars.dicebear.com/styles to see what they look like.\n
    - Note: Only works with attributes!
    """
    list = all_styles = styles
    adventurer = styles[0]
    adventurer_neutral = styles[1]
    avataaars = styles[2]
    avataaars_neutral = styles[3]
    big_ears = styles[4]
    big_ears_neutral = styles[5]
    big_smile = styles[6]
    bottts = styles[7]
    bottts_neutral = styles[8]
    croodles = styles[9]
    croodles_neutral = styles[10]
    fun_emoji = styles[11]
    icons = styles[12]
    identicon = styles[13]
    initials = styles[14]
    lorelei = styles[15]
    lorelei_neutral = styles[16]
    micah = styles[17]
    miniavs = styles[18]
    open_peeps = styles[19]
    personas = styles[20]
    pixel_art = styles[21]
    pixel_art_neutral = styles[22]
    shapes = styles[23]
    thumbs = styles[24]
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
    list = all_formats = ["svg", "png", "jpg", "json"]
    svg = "svg"
    png = "png"
    jpg = "jpg"
    json = "json"
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
        return eval("DFormat.{}".format(format_str.replace("DFormat.", "")))


default_options: dict = {options[0]: False, options[1]: 0, options[2]: 100, options[3]: 0, options[4]: 0,
                         options[5]: DColor(), options[6]: "solid", options[7]: 0, options[8]: 0, options[9]: 0,
                         options[10]: False}

class DOptions(dict):
    """
    The options class for :py:class:`dicebear.avatar.DAvatar`
    """
    empty: dict = {}
    default_options = default = default_options
    def __init__(self, *, flip: bool = False, rotate: int = 0, scale: int = 100, radius: int = 0, size: int = 0,
                 backgroundColor: Union[DColor, str, typing.List[str], typing.List[DColor]] = DColor(), backgroundType: str = "solid", backgroundRotation: int = 0,
                 translateX: int = 0, translateY: int = 0, randomizeIds: bool = False, **kwargs):
        """
        Go to https://github.com/jvherck/dicebear#base-options to see all info (important for minimum and maximum values for each option!)

        :param kwargs: `fromdict` to use a custom dict instead of args (if you use this kwarg all other args will be neglected)
        """
        dic = kwargs.get("fromdict", {})
        current: dict = {"flip": flip, "rotate": rotate, "scale": scale, "radius": radius, "size": size,
                         "backgroundColor": DColor(backgroundColor), "backgroundType": backgroundType, "backgroundRotation": backgroundRotation,
                         "translateX": translateX, "translateY": translateY, "randomizeIds": randomizeIds}
        if dic:
            for item in dic:
                if item not in default_options.keys() or dic[item] == default_options[item]: dic.pop(item, None)
        else:  # if not dic
            for item in current:
                if item in default_options and current[item] != default_options[item]: dic.update({item: current[item]})
        if "size" in dic and dic["size"] == 0: dic.pop("size")
        super().__init__(dic)

    @property
    def _ver(self): return type(self)


def pilcheck(func):
    """Decorator to check if package Pillow is installed"""
    def wrapper(*args, **kwargs):
        if _FindPil.found is True: return func(*args, **kwargs)
        else: log_error(PILError())
    return wrapper
