# MIT License
#
# Copyright (c) 2021 jvherck (on GitHub)
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
import requests as r
from urllib.parse import quote
from .errors import *
from .models import *


_url = "https://avatars.dicebear.com/api/{}/{}.svg?"


class DAvatar:
    default_options: dict = default_options
    all_options: list = options
    def __init__(self, style: DStyle, seed: str, *, base_options: DOptions = None, options: dict = None): # TODO: add specific options
        """
        Create an avatar using this class, use `.url_svg` to get the svg url or `.url_png` to get the png url.
        Clickable links: https://github.com/jvherck/dicebear#styles , https://github.com/jvherck/dicebear#base-options , https://github.com/jvherck/dicebear#specific-style-options

        :param style: the style of avatar you want to create; check the whole list at https://github.com/jvherck/dicebear#styles
        :param seed: the seed for the avatar; the avatar will be edited according to the seed.
        :param base_options: `class: DOptions` the options for the avatar; check the whole list at https://github.com/jvherck/dicebear#base-options
        :param options: `class: dict` specific options for the specified avatar style; see all specific options at https://github.com/jvherck/dicebear#specific-style-options
        """
        if base_options is None:
            base_options = DOptions.empty
        self._style: DStyle = style
        self._seed: str = seed
        self._options: DOptions = base_options
        self._avatar_url = None
        self._avatar_svg = None
        self._url = None
        self.__get_avatar_url()

    @property
    def style(self) -> DStyle:
        """
        :return: the style of the avatar
        """
        return self._style
    @property
    def seed(self) -> str:
        """
        :return: the seed of the avatar
        """
        return self._seed
    @property
    def options(self) -> DOptions:
        """
        :return: the options of the avatar
        """
        _option_list = {}
        for key in self._options:
            if self._options[key] != DAvatar.default_options[key]:
                _option_list.update({key: self._options[key]})
        return DOptions(fromdict=_option_list)
    @property
    def url_svg(self) -> str:
        """
        :return: url to avatar (svg, use `.to_png()` to convert to png)
        """
        return self._avatar_url
    @property
    def url_png(self) -> str:
        """
        :return:  url to avatar (png, use `.url_svg` to convert to svg)
        """
        return self._url
    @property
    def full_svg(self) -> str:
        """
        :return: the raw svg code of the avatar
        """
        return self._avatar_svg

    def __repr__(self):
        self.__get_avatar_url()
        return self._avatar_url

    def __str__(self):
        self.__get_avatar_url()
        return self._url

    def __get_avatar_url(self):
        _link = _url
        _options = []
        for item in options:
            if item == "size" and "size" in self._options and self._options["size"] == 0:
                continue
            elif item == "size" and "size" not in self._options:
                continue
            elif item in self._options and self._options[item] == default_options[item]:
                continue
            elif item not in self._options:
                continue
            else:
                _options.append(
                    "{}={}".format(
                        quote(item),
                        str(self._options[item]).lower() if type(self._options[item]) == bool else quote(str(self._options[item]))
                    )
                )
        _link += "&".join(_options)
        _link.replace("False", "false").replace("True", "true")
        _link = _link.format(quote(self._style), quote(self._seed))
        req = r.request('GET', _link)
        self._avatar_url = req.url
        self._avatar_svg = req.text
        self._content = req.content
        self.to_png()


    def edit(self, *, style: DStyle = None, seed: str = None, extra_options: DOptions = None, blank_options: DOptions = None) -> str:
        """
        Edit an already existing avatar.

        :param style: edit the avatar's style (style of drawing)
        :param seed: edit the avatar's seed (string to determine its looks)
        :param extra_options: edit the avatar's options (old options stay, these get added) -- cannot be used at the same time with `blank_options` !
        :param blank_options: reset old options and set these options as new ones (new options) -- cannot be used at the same with `extra_options` !
        :return: returns the link to the avatar url (png)
        """
        if style:
            self._style = style
        if seed:
            self._seed = seed
        if extra_options:
            self._options.update(extra_options)
        elif blank_options:
            self._options = blank_options

        self.__get_avatar_url()
        return self._url

    def to_png(self):
        """
        Turns the avatar from svg into png and returns the url.

        :return: class `str` :: link to png avatar
        """
        self._url = self._avatar_url.replace(".svg", ".png")
        return self._url
