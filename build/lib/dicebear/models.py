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

from .errors import *
from typing import Union


options = ["dataUri", "flip", "rotate", "scale", "radius", "size", "backgroundColor", "translateX", "translateY"]
styles = ["adventurer", "adventurer-neutral", "avataaars", "big-ears", "big-ears-neutral",
          "big-smile", "bottts", "croodles", "croodles-neutral", "identicon", "initials",
          "micah", "miniavs", "open-peeps", "personas", "pixel-art", "pixel-art-neutral"]
styles_depricated = ["female", "gridy", "human", "jdenticon", "male"]


class DColor(str):
    def __init__(self, html_code: str = "#ffffff"):
        """
        Colors used in this package. This uses HTML color codes!

        :param html_code: the html color code to use as color
        """
        if not html_code.startswith("#"):
            html_code = "#" + html_code
        if len(html_code) not in [4, 7]:
            raise IncorrectColor(str(html_code))
        self.html_code: str = str(html_code)
        super().__init__()

    def __str__(self):
        return f"{self.html_code}"
    def __repr__(self):
        return f"{self.html_code}"


class DStyle(str):
    """
    All possible styles for the avatars. Visit https://avatars.dicebear.com/styles to see what they look like.\n
    - Note: Only works with attributes!
    """
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


default_options: dict = {options[0]: False, options[1]: False, options[2]: 0, options[3]: 100, options[4]: 0,
             options[5]: 0, options[6]: DColor(), options[7]: 0, options[8]: 0}

class DOptions(dict):
    empty: dict = {}
    def __init__(self, *, dataUri: bool = False, flip: bool = False, rotate: int = 0, scale: int = 100,
                 radius: int = 0, size: int = 0, backgroundColor: DColor = DColor(), translateX: int = 0, translateY: int = 0, **kwargs):
        """
        Go to https://github.com/jvherck/dicebear#base-options to see all info

        :param kwargs: `fromdict` to use a custom dict instead of args (if you use this kwarg all other args will be neglected)
        """
        # kwargs: list = [dataUri, flip, rotate, scale, radius, size, backgroundColor, translateX, translateY]
        dic = kwargs.get("fromdict", {})
        current: dict = {"dataUri": dataUri, "flip": flip, "rotate": rotate, "scale": scale, "radius": radius, "size": size,
                     "backgroundColor": backgroundColor, "translateX": translateX, "translateY": translateY}
        if not dic:
            for item in current:
                if item in default_options and current[item] != default_options[item]:
                    dic.update({item: current[item]})
        if "size" in dic and dic["size"] == 0:
            dic.pop("size")
        super().__init__(dic)



# class DUrl:
#     def __init__(self, url: str,):
#         self._url = url
#
#     def __str__(self) -> str:
#         return str(self._url)
#     def __repr__(self) -> str:
#         return str(self._url)
#     def __eq__(self, other) -> bool:
#         if isinstance(other, DUrl):
#             if str(other) == str(self._url):
#                 return True
#         return False
#     def __ne__(self, other) -> bool:
#         if isinstance(other, (str, DUrl)):
#             if str(other) != str(self._url):
#                 return True
#         return False


