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

from typing import Union, List
from random import choice, choices
from requests import post, get
from os import environ

from .errors import *

__all__ = (
    'DColor',
    'DStyle',
    'DFormat',
    'DOptions',
    'options',
    'all_options',
    'style_metadata',
    'styles',
    'default_options',
)
__filename__ = "models.py"


class _FindPil:
    """Not important for you, just makes things easier for me on the back-end ;)"""
    found: bool = True

_ascii_lowercase = "abcdef"
_incorrect_lowercase = "ghijklmnopqrstuvwxyz"
_digits = "0123456789"
_y = "https://api.dicebear.com/7.x/{}/schema.json"

options = all_options = ["flip", "rotate", "scale", "radius", "size", "backgroundColor", "backgroundType",
                         "backgroundRotation", "translateX", "translateY", "randomizeIds"]
style_metadata = {
    "adventurer": {
        "title": "Adventurer",
        "creator": "Lisa Wischofsky",
        "source": "https://www.figma.com/community/file/1184595184137881796",
        "homepage": "https://www.instagram.com/lischi_art/",
        "license": {
            "name": "CC BY 4.0",
            "url": "https://creativecommons.org/licenses/by/4.0/",
        },
    },
    "adventurer-neutral": {
        "title": "Adventurer Neutral",
        "creator": "Lisa Wischofsky",
        "source": "https://www.figma.com/community/file/1184595184137881796",
        "homepage": "https://www.instagram.com/lischi_art/",
        "license": {
            "name": "CC BY 4.0",
            "url": "https://creativecommons.org/licenses/by/4.0/",
        },
    },
    "avataaars": {
        "title": "Avataaars",
        "creator": "Pablo Stanley",
        "source": "https://avataaars.com/",
        "homepage": "https://twitter.com/pablostanley",
        "license": {
            "name": "Free for personal and commercial use",
            "url": "https://avataaars.com/",
        },
    },
    "avataaars-neutral": {
        "title": "Avataaars",
        "creator": "Pablo Stanley",
        "source": "https://avataaars.com/",
        "homepage": "https://twitter.com/pablostanley",
        "license": {
            "name": "Free for personal and commercial use.",
            "url": "https://avataaars.com/",
        },
    },
    "big-ears": {
        "title": "Face Generator",
        "creator": "The Visual Team",
        "source": "https://www.figma.com/community/file/986078800058673824",
        "homepage": "https://thevisual.team/",
        "license": {
            "name": "CC BY 4.0",
            "url": "https://creativecommons.org/licenses/by/4.0/",
        },
    },
    "big-ears-neutral": {
        "title": "Face Generator",
        "creator": "The Visual Team",
        "source": "https://www.figma.com/community/file/986078800058673824",
        "homepage": "https://thevisual.team/",
        "license": {
            "name": "CC BY 4.0",
            "url": "https://creativecommons.org/licenses/by/4.0/",
        },
    },
    "big-smile": {
        "title": "Custom Avatar",
        "creator": "Ashley Seo",
        "source": "https://www.figma.com/community/file/881358461963645496",
        "homepage": "http://www.ashleyseo.com/",
        "license": {
            "name": "CC BY 4.0",
            "url": "https://creativecommons.org/licenses/by/4.0/",
        },
    },
    "bottts": {
        "title": "Bottts",
        "creator": "Pablo Stanley",
        "source": "https://bottts.com/",
        "homepage": "https://twitter.com/pablostanley",
        "license": {
            "name": "Free for personal and commercial use",
            "url": "https://bottts.com/",
        },
    },
    "bottts-neutral": {
        "title": "Bottts",
        "creator": "Pablo Stanley",
        "source": "https://bottts.com/",
        "homepage": "https://twitter.com/pablostanley",
        "license": {
            "name": "Free for personal and commercial use",
            "url": "https://bottts.com/",
        },
    },
    "croodles": {
        "title": "Croodles - Doodle your face",
        "creator": "vijay verma",
        "source": "https://www.figma.com/community/file/966199982810283152",
        "homepage": "https://vjy.me/",
        "license": {
            "name": "CC BY 4.0",
            "url": "https://creativecommons.org/licenses/by/4.0/",
        },
    },
    "croodles-neutral": {
        "title": "Croodles - Doodle your face",
        "creator": "vijay verma",
        "source": "https://www.figma.com/community/file/966199982810283152",
        "homepage": "https://vjy.me/",
        "license": {
            "name": "CC BY 4.0",
            "url": "https://creativecommons.org/licenses/by/4.0/",
        },
    },
    "fun-emoji": {
        "title": "Fun Emoji Set",
        "creator": "Davis Uche",
        "source": "https://www.figma.com/community/file/968125295144990435",
        "homepage": "https://www.instagram.com/davedirect3/",
        "license": {
            "name": "CC BY 4.0",
            "url": "https://creativecommons.org/licenses/by/4.0/",
        },
    },
    "icons": {
        "title": "Bootstrap Icons",
        "creator": "The Bootstrap Authors",
        "source": "https://github.com/twbs/icons",
        "homepage": "https://getbootstrap.com/",
        "license": {
            "name": "MIT",
            "url": "https://github.com/twbs/icons/blob/main/LICENSE",
        },
    },
    "identicon": {
        "title": "Identicon",
        "creator": "DiceBear",
        "source": "https://www.dicebear.com",
        "homepage": "https://www.dicebear.com",
        "license": {
            "name": "CC0 1.0",
            "url": "https://creativecommons.org/publicdomain/zero/1.0/",
        },
    },
    "initials": {
        "title": "Initials",
        "creator": "DiceBear",
        "source": "https://github.com/dicebear/dicebear",
        "license": {
            "name": "CC0 1.0",
            "url": "https://creativecommons.org/publicdomain/zero/1.0/",
        },
    },
    "lorelei": {
        "title": "Lorelei",
        "creator": "Lisa Wischofsky",
        "source": "https://www.figma.com/community/file/1198749693280469639",
        "homepage": "https://www.instagram.com/lischi_art/",
        "license": {
            "name": "CC0 1.0",
            "url": "https://creativecommons.org/publicdomain/zero/1.0/",
        },
    },
    "lorelei-neutral": {
        "title": "Lorelei Neutral",
        "creator": "Lisa Wischofsky",
        "source": "https://www.figma.com/community/file/1198749693280469639",
        "homepage": "https://www.instagram.com/lischi_art/",
        "license": {
            "name": "CC0 1.0",
            "url": "https://creativecommons.org/publicdomain/zero/1.0/",
        },
    },
    "micah": {
        "title": "Avatar Illustration System",
        "creator": "Micah Lanier",
        "source": "https://www.figma.com/community/file/829741575478342595",
        "homepage": "https://dribbble.com/micahlanier",
        "license": {
            "name": "CC BY 4.0",
            "url": "https://creativecommons.org/licenses/by/4.0/",
        },
    },
    "miniavs": {
        "title": "Miniavs - Free Avatar Creator",
        "creator": "Webpixels",
        "source": "https://www.figma.com/community/file/923211396597067458",
        "homepage": "https://webpixels.io/",
        "license": {
            "name": "CC BY 4.0",
            "url": "https://creativecommons.org/licenses/by/4.0/",
        },
    },
    "notionists": {
        "title": "Notionists",
        "creator": "Zoish",
        "source": "https://heyzoish.gumroad.com/l/notionists",
        "homepage": "https://bio.link/heyzoish",
        "license": {
            "name": "CC0 1.0",
            "url": "https://creativecommons.org/publicdomain/zero/1.0/",
        },
    },
    "notionists-neutral": {
        "title": "Notionists",
        "creator": "Zoish",
        "source": "https://heyzoish.gumroad.com/l/notionists",
        "homepage": "https://bio.link/heyzoish",
        "license": {
            "name": "CC0 1.0",
            "url": "https://creativecommons.org/publicdomain/zero/1.0/",
        },
    },
    "open-peeps": {
        "title": "Open Peeps",
        "creator": "Pablo Stanley",
        "source": "https://www.openpeeps.com/",
        "homepage": "https://twitter.com/pablostanley",
        "license": {
            "name": "CC0 1.0",
            "url": "https://creativecommons.org/publicdomain/zero/1.0/",
        },
    },
    "personas": {
        "title": "Personas by Draftbit",
        "creator": "Draftbit - draftbit.com",
        "source": "https://personas.draftbit.com/",
        "homepage": "https://draftbit.com/",
        "license": {
            "name": "CC BY 4.0",
            "url": "https://creativecommons.org/licenses/by/4.0/",
        },
    },
    "pixel-art": {
        "title": "Pixel Art",
        "creator": "DiceBear",
        "source": "https://www.figma.com/community/file/1198754108850888330",
        "homepage": "https://www.dicebear.com",
        "license": {
            "name": "CC0 1.0",
            "url": "https://creativecommons.org/publicdomain/zero/1.0/",
        },
    },
    "pixel-art-neutral": {
        "title": "Pixel Art Neutral",
        "creator": "DiceBear",
        "source": "https://www.figma.com/community/file/1198754108850888330",
        "homepage": "https://www.dicebear.com",
        "license": {
            "name": "CC0 1.0",
            "url": "https://creativecommons.org/publicdomain/zero/1.0/",
        },
    },
    "rings": {
        "title": "Rings",
        "creator": "DiceBear",
        "source": "https://www.dicebear.com",
        "homepage": "https://www.dicebear.com",
        "license": {
            "name": "CC0 1.0",
            "url": "https://creativecommons.org/publicdomain/zero/1.0/",
        },
    },
    "shapes": {
        "title": "Shapes",
        "creator": "DiceBear",
        "source": "https://www.dicebear.com",
        "homepage": "https://www.dicebear.com",
        "license": {
            "name": "CC0 1.0",
            "url": "https://creativecommons.org/publicdomain/zero/1.0/",
        },
    },
    "thumbs": {
        "title": "Thumbs",
        "creator": "DiceBear",
        "source": "https://www.dicebear.com",
        "homepage": "https://www.dicebear.com",
        "license": {
            "name": "CC0 1.0",
            "url": "https://creativecommons.org/publicdomain/zero/1.0/",
        },
    },
}

styles = list(style_metadata.keys())
# styles_depricated = ["female", "gridy", "human", "jdenticon", "male"]


class DColor:
    """
    Base class for DAvatar's colors.
    """

    def __init__(self, html_code: Union[str, List[str]] = "transparent"):
        """
        Colors used in this package. This uses HTML/hex color codes!

        :param html_code: :py:class:`str` :: the html color code to use as color. This can be a list of strings if `backgroundType` has been set to "gradientLinear". (default: transparent)
        :type html_code: str
        :raise dicebear.errors.IncorrectColor: if the given html_code is an invalid hex color
        """
        code_list: list = []
        hex_list: list = []
        if type(html_code) == str: code_list = html_code.replace(" ", "").split(",")
        elif type(html_code) == list and all(type(x) == str for x in html_code): code_list = html_code
        for code in code_list:
            if code.startswith("#"): code = code.replace("#", "")
            if (len(code) != 6 or any(x in code for x in _incorrect_lowercase)) and code != "transparent":
                raise IncorrectColor(str(code))
            hex_list.append(code)
        self.html_code: str = ",".join(hex_list)

    def __str__(self): return str(self.html_code)
    def __repr__(self): return str(self.html_code)
    def __eq__(self, other):
        if type(other) == DColor: return self.html_code == other.html_code
        return self.html_code == other
    def __ne__(self, other):
        if type(other) == DColor: return self.html_code != other.html_code
        return self.html_code != other

    @staticmethod
    def random() -> "DColor":
        """
        Get a random html code.

        :return: :py:class:`dicebear.models.DColor`
        """
        return DColor(''.join(choices(_ascii_lowercase + _digits, k=6)))


class DStyle:
    """
    All possible styles for the avatars. Visit https://dicebear.com/styles to see what they look like.\n
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
    notionists = styles[19]
    notionists_neutral = styles[20]
    open_peeps = styles[21]
    personas = styles[22]
    pixel_art = styles[23]
    pixel_art_neutral = styles[24]
    rings = styles[25]
    shapes = styles[26]
    thumbs = styles[27]

    def __init__(self):
        """Only use `.attribute` to use a style."""
        raise NotImplementedError("DStyle should not be initialized.")

    @staticmethod
    def get_schema(style: str) -> dict:
        """
        Returns a dict with the JSON schema (all properties) of the given avatar style.

        :param style: :py:class:`str` :: the avatar style to get the JSON schema of
        :type style: str
        :return: :py:class:`dict`
        """
        if style not in styles:
            raise ValueError(f'"{style}" is not a valid avatar style.')
        try:
            dictionary = get(_y.format(style)).json()
        except Exception as e:
            raise HTTPError({"exception": str(type(e)), "error": str(e)})
        else:
            return dictionary

    @staticmethod
    def random() -> str:
        """
        Get a random style.

        :return: a random style
        """
        return choice(styles)

    @classmethod
    def from_str(cls, style_str: str) -> str:
        """
        Get an avatar style from a string.

        :param style_str: :py:class:`str` :: the string to convert to a DStyle
        :type style_str: str
        """
        return getattr(cls, style_str.replace("-", "_"))


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
        raise NotImplementedError("DFormat should not be initialized.")

    @classmethod
    def from_str(cls, format_str: str) -> str:
        """
        Get an avatar format from a string

        :param format_str: :py:class:`str` :: the string to convert to a DFormat
        :type format_str: str
        """
        return getattr(cls, format_str.replace("DFormat.", ""))


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
                 backgroundColor: Union[DColor, List[DColor]] = DColor(), backgroundType: str = "solid", backgroundRotation: int = 0,
                 translateX: int = 0, translateY: int = 0, randomizeIds: bool = False, **kwargs):
        """
        Go to https://github.com/jvherck/dicebear#base-options to see all info (important for minimum and maximum values for each option!)

        :param kwargs: `fromdict` to use a custom dict instead of args (if you use this kwarg all other args will be neglected)
        """
        dic = kwargs.get("fromdict", {})
        current: dict = {"flip": flip, "rotate": rotate, "scale": scale, "radius": radius, "size": size,
                         "backgroundColor": backgroundColor, "backgroundType": backgroundType, "backgroundRotation": backgroundRotation,
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





def _statsIncrease(_file: str, _class: str, _function: str, *, _test: bool = False) -> None:
    """
    Pings an API to update this package's usage stats. This will be used to analyse Dicebear's usage and improve your overall experience.
    """
    if environ.get('ENABLE_PYTHON_DICEBEAR_USAGE_STATS', '').lower() != 'true':
        return
    __body = {"file": _file, "class": _class, "function": _function, "test": str(_test).lower()}
    __headers = {"User-Agent": "pipedream/1", "Content-Type": "application/json", "-Key": "acbd2023"}
    post("https://eo1p6rm1ydzj8yl.m.pipedream.net/runs", json=__body, headers=__headers, timeout=10)

def _pilcheck(func):
    """Decorator to check if package Pillow is installed"""
    def wrapper(*args, **kwargs):
        if _FindPil.found is True: return func(*args, **kwargs)
        else: log_error(PILError())
    return wrapper
