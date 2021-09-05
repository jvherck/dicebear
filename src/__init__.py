import requests as r
from typing import Union

url = "https://avatars.dicebear.com/api/{}/{}.svg"
_options = ["seed", "dataUri", "flip", "rotate", "scale", "radius", "size", "backgroundColor", "translateX", "translateY"]


class Avatar:
    def __init__(self, type: str = "initials", seed: str = None, **kwargs):
        """

        :param type: the type of avatar you want to create; check the whole list at https://avatars.dicebear.com/styles
        :param seed: the seed for the avatar; the avatar will be edited according to the seed.
        :param options: `class: dict`
        """
        self.type: str = type
        self.seed: str = seed
        self.options: dict = kwargs.get("options", {})
        self.avatar = None

    def __repr__(self):
        self.__get_avater()
        return self.avatar

    def __str__(self):
        self.__get_avater()
        return self.avatar

    def __get_avater(self):
        if self.options:
            _url = url
            for option in self.options:
                if option in _options:
                    if self.options[option] is True:
                        self.options[option] = "true"
                    elif self.options[option] is False:
                        self.options[option] = "false"
                    _url += "?{}".format(f"{option}={self.options[option]}")
                else:
                    continue
            self.avatar = r.request('GET', _url.format(self.type, self.seed)).url
        else:
            self.avatar = r.request('GET', url.format(self.type, self.seed)).url


    def edit(self, *, type: str = None, seed: str = None, options: dict = None):
        if type is not None:
            self.type = type
        if seed is not None:
            self.seed = seed
        if options is not None:
            self.options = options











