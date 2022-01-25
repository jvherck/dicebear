import requests as r
from urllib.parse import quote
from .errors import *
from .models import *


_url = "https://avatars.dicebear.com/api/{}/{}.svg?"


class DAvatar:
    default_options: dict = default_options
    all_options: list = options
    def __init__(self, style: DStyle, seed: str, *, options: DOptions = None):
        """
        :param type: the type of avatar you want to create; check the whole list at https://avatars.dicebear.com/styles
        :param seed: the seed for the avatar; the avatar will be edited according to the seed.
        :param options: `class: dict` the options for the avatar; check the whole list at https://avatars.dicebear.com/docs/options
        """
        if options is None:
            options = DOptions.empty
        self._style: DStyle = style
        self._seed: str = seed
        self._options: DOptions = options
        self._avatar_url = None
        self._avatar_svg = None
        self.__get_avatar_url()

    @property
    def style(self) -> DStyle:
        return self._style
    @property
    def seed(self) -> str:
        return self._seed
    @property
    def options(self) -> DOptions:
        _option_list = {}
        for key in self._options:
            if self._options[key] != DAvatar.default_options[key]:
                _option_list.update({key: self._options[key]})
        return DOptions(fromdict=_option_list)
    @property
    def avatar_url(self) -> DUrl:
        return self._avatar_url
    @property
    def avatar_svg(self) -> str:
        return self._avatar_svg

    def __repr__(self):
        self.__get_avatar_url()
        return self._avatar_url

    def __str__(self):
        self.__get_avatar_url()
        return self._avatar_url

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


    def edit(self, *, style: DStyle = None, seed: str = None, extra_options: DOptions = None, blank_options: DOptions = None) -> str:
        """

        :param style: edit the avatar's style (style of drawing)
        :param seed: edit the avatar's seed (string to determine its looks)
        :param extra_options: edit the avatar's options (old options stay, these get added) -- cannot be used at the same time with `blank_options` !
        :param blank_options: reset old options and set these options as new ones (new options) -- cannot be used at the same with `extra_options` !
        :return:
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
        return self._avatar_url
