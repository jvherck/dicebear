# MIT License
#
# Copyright (c) 2024 jvherck (on GitHub)
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

import io
import os
import pathlib
import re as regex
from ast import literal_eval
from random import choices
from string import ascii_lowercase, digits
from typing import Union
from urllib.parse import quote

import requests as r

from .errors import *
from .models import *
from .models import _FindPil, _pilcheck, _statsIncrease, _x

__all__ = ("DAvatar",)
__filename__ = "avatar.py"

try:
    from PIL import Image as Im
except Exception:

    class Im:
        class Image:
            def show(self):
                pass

    _FindPil.found = False

_y = _x + "/{}/svg?seed={}&"


class DAvatar:
    """
    Base class for the avatar generator.
    """

    default_options: dict = default_options
    all_options: list = options

    def __init__(
        self,
        style: Union[str, DStyle] = None,
        seed: str = None,
        *,
        options: DOptions = None,
        custom: dict = None,
    ) -> None:
        """
        Create a new avatar object.

        :param style: class `dicebear.models.DStyle` :: the style of avatar you want to create; check the whole list at https://github.com/jvherck/dicebear#styles
        :type style: dicebear.models.DStyle
        :param seed: class `str` :: the seed for the avatar; the avatar will be edited according to the seed
        :type seed: str
        :param options: class `DOptions` :: the options for the avatar; check the whole list at https://github.com/jvherck/dicebear#base-options
        :type options: dicebear.models.DOptions
        :param custom: `class: dict` :: customisations for the specified avatar style; see all specific options at https://github.com/jvherck/dicebear#specific-style-options
        :type custom: dict
        """
        if style is None:
            style = DStyle.random()
        if style not in styles:
            raise Error(
                "Invalid Style",
                '"{}" is not a valid style! Use `DStyle.list` to see all available styles'.format(style),
            )
        if seed is None:
            seed = "".join(choices(ascii_lowercase + digits, k=20))
        if options is None:
            options = DOptions.empty
        if custom is None:
            custom = {}
        self.__style: DStyle = style
        self.__seed: str = seed
        self.__options: DOptions = options
        self.__specific: dict = custom
        self.__url_svg: str
        self.__update()
        _statsIncrease(__filename__, self.__class__.__name__, ".__init__()")

    @property
    def style(self) -> DStyle:
        """
        :return: the style of the avatar
        """
        _statsIncrease(__filename__, self.__class__.__name__, ".style")
        return self.__style

    @property
    def seed(self) -> str:
        """
        :return: the seed of the avatar
        """
        _statsIncrease(__filename__, self.__class__.__name__, ".seed")
        return self.__seed

    @property
    def options(self) -> DOptions:
        """
        :return: the options of the avatar
        """
        _statsIncrease(__filename__, self.__class__.__name__, ".options")
        _option_list = {}
        for key in self.__options:
            if self.__options[key] != default_options[key]:
                _option_list.update({key: self.__options[key]})
        return DOptions.from_dict(_option_list)

    @property
    def customisations(self) -> dict:
        """
        :return: the customisations of the avatar
        """
        _statsIncrease(__filename__, self.__class__.__name__, ".customisations")
        return self.__specific

    customizations = customs = customisations

    @property
    def url_svg(self) -> str:
        """
        :return: url to svg avatar
        """
        _statsIncrease(__filename__, self.__class__.__name__, ".url_svg")
        return self.__url_svg

    @property
    def url_png(self) -> str:
        """
        :return: url to png avatar
        """
        _statsIncrease(__filename__, self.__class__.__name__, ".url_png")
        return self.__url_svg.replace("/svg?", "/png?")

    @property
    def url_jpg(self) -> str:
        """
        :return: url to jpg avatar
        """
        _statsIncrease(__filename__, self.__class__.__name__, ".url_jpg")
        return self.__url_svg.replace("/svg?", "/jpg?")

    @property
    def url_json(self) -> str:
        """
        :return: url to json data of avatar
        """
        _statsIncrease(__filename__, self.__class__.__name__, ".url_json")
        return self.__url_svg.replace("/svg?", "/json?")

    @property
    def schema(self) -> dict:
        """
        :return: dict object containing the schema of the avatar style
        """
        return r.get(_x + f"/{self.style}/schema.json").json()

    def text(self, format: DFormat = DFormat.svg) -> str:
        """
        :param format: class `dicebear.models.DFormat` :: which format to use
        :return: returns the avatar's request's full text/file in str format
        """
        _statsIncrease(__filename__, self.__class__.__name__, ".text()")
        req = r.get(regex.sub(r"/(svg|png|jpg|json)\?", f"/{format}?", self.__url_svg))
        self.__checkLinkError(req.text)
        return req.text

    def bytes(self, format: DFormat = DFormat.png) -> io.BytesIO:
        """
        :param format: class `dicebear.models.DFormat` :: which format to use
        :return: returns the bytes of the avatar in `io.BytesIO` format
        """
        _statsIncrease(__filename__, self.__class__.__name__, ".bytes()")
        req = r.get(regex.sub(r"/(svg|png|jpg|json)\?", f"/{format}?", self.__url_svg))
        self.__checkLinkError(req.text)
        return io.BytesIO(req.content)

    def __repr__(self):
        return f'DAvatar(style=DStyle.{self.style}, seed="{self.seed}", *, options={self.options}, custom={self.customizations})'

    def __str__(self):
        return self.__url_svg

    def __eq__(self, other):
        if type(other) is DAvatar:
            return self.__url_svg == other.__url_svg
        return self.__url_svg == other

    def __ne__(self, other):
        if type(other) is DAvatar:
            return self.__url_svg != other.__url_svg
        return self.__url_svg != other

    def __le__(self, other):
        if type(other) is DAvatar:
            return self.options["size"] <= other.options["size"]
        elif type(other) is dict:
            return self.options["size"] <= other["size"]
        return self.options["size"] <= other

    def __lt__(self, other):
        if type(other) is DAvatar:
            return self.options["size"] < other.options["size"]
        elif type(other) is dict:
            return self.options["size"] < other["size"]
        return self.options["size"] < other

    def __ge__(self, other):
        if type(other) is DAvatar:
            return self.options["size"] >= other.options["size"]
        elif type(other) is dict:
            return self.options["size"] >= other["size"]
        return self.options["size"] >= other

    def __gt__(self, other):
        if type(other) is DAvatar:
            return self.options["size"] > other.options["size"]
        elif type(other) is dict:
            return self.options["size"] > other["size"]
        return self.options["size"] > other

    def __dict__(self):
        return {
            "style": self.style,
            "seed": self.seed,
            "options": self.options,
            "custom": self.customisations,
        }

    def __contains__(self, key: str):
        """
        Returns `True` if the specified key is found in either DAvatar.options.keys() or DAvatar.customisations.keys(), else returns `False`
        """
        return key in self.options.keys() or key in self.customisations.keys()

    @staticmethod
    def __checkLinkError(text: str) -> None:
        """
        :param text: requests.Response.text
        """
        try:
            status = literal_eval(text)
        except (ValueError, SyntaxError):
            status = ""
        if type(status) is dict and "statusCode" in status:
            raise HTTPError(status)

    def __update(self) -> None:
        _link = _y
        _options, _specoptions, status = [], [], ""
        for item in self.__options:
            if item in all_options and self.__options[item] != default_options[item]:
                _options.append(
                    "{}={}".format(
                        quote(item),
                        str(self.__options[item]).replace("False", "false").replace("True", "true"),
                    )
                )
        for item in self.__specific:
            _specoptions.append(
                "{}={}".format(
                    quote(item),
                    str(self.__specific[item]).replace("False", "false").replace("True", "true"),
                )
            )
        _link += "&".join(_options + _specoptions)
        _link = _link.format(quote(str(self.__style)), quote(self.__seed))
        req = r.get(_link)
        self.__checkLinkError(req.text)
        self.__url_svg = req.url

    @staticmethod
    def __uniquify(path) -> str:
        filename, extension = os.path.splitext(path)
        counter = 0
        while os.path.exists(path):
            counter += 1
            path = filename + "(" + str(counter) + ")" + extension
        return path

    def edit(
        self,
        *,
        style: DStyle = None,
        seed: str = None,
        extra_options: DOptions = None,
        blank_options: DOptions = None,
    ) -> str:
        """
        Edit an already existing avatar.

        :param style: class `DStyle` :: edit the avatar's style (style of drawing)
        :type style: dicebear.models.DStyle
        :param seed: class `str` :: edit the avatar's seed (string to determine its looks)
        :type seed: str
        :param extra_options: class `DOptions` :: edit the avatar's options (old options stay, these get added) -- cannot be used at the same time with `blank_options` !
        :type extra_options: dicebear.models.DOptions
        :param blank_options: class `DOptions` :: reset old options and set these options as new ones (new options) -- cannot be used at the same with `extra_options` !
        :type blank_options: dicebear.models.DOptions
        :return: class `str` :: returns the link to the avatar url (svg)
        """
        _statsIncrease(__filename__, self.__class__.__name__, ".edit()")
        if style:
            self.__style = style
        if seed:
            self.__seed = seed
        if extra_options:
            self.__options.update(extra_options)
        elif blank_options:
            self.__options = blank_options
        self.__update()
        return self.__url_svg

    def customise(self, *, extra_options: dict = None, blank_options: dict = None) -> str:
        """
        Customise the specific options for an already existing avatar.

        :param extra_options: class `DOptions` :: edit the avatar's specific options (old options stay, these get added) -- cannot be used at the same time with `blank_options` !
        :type extra_options: dicebear.models.DOptions
        :param blank_options: class `DOptions` :: reset old specific options and set these options as new ones (new options) -- cannot be used at the same with `extra_options` !
        :type blank_options: dicebear.models.DOptions
        :return: class `str` :: returns the link to the avatar url (svg)
        """
        _statsIncrease(__filename__, self.__class__.__name__, ".customise()")
        if extra_options:
            self.__specific.update(extra_options)
        elif blank_options:
            self.__specific = blank_options
        self.__update()
        return self.__url_svg

    customize: callable = customise

    def save(
        self,
        *,
        location: Union[pathlib.Path, str] = None,
        file_name: str = "dicebear_avatar",
        file_format: DFormat = DFormat.svg,
        overwrite: bool = False,
        open_after_save: bool = False,
    ) -> str:
        """
        Save the avatar to your device.

        :param location: class `pathlib.Path` :: the folder to save the file in. (default is `None` which saves it in the current directory `os.getcwd()`)
        :type location: pathlib.Path
        :param file_name: class `str` :: the name of the file to save. (default is "dicebear_avatar")
        :type file_name: str
        :param file_format: class `DFormat` :: the format of the file. (default is "svg")
        :type file_format: dicebear.models.DFormat
        :param overwrite: class `bool` ::  whether to overwrite an already existing file if it has the same file name and extension
        :type overwrite: bool
        :param open_after_save: class `bool` ::  whether to open the file after saving it to your device
        :type open_after_save: bool
        :return: class `str` :: the path of the saved image if saved successfully
        """
        _statsIncrease(__filename__, self.__class__.__name__, ".save()")
        if file_format not in DFormat.all_formats:
            s = f'"{file_format}" is not a supported format!'
            raise ImageError(s)
        if location is None:
            location = pathlib.Path(os.getcwd())
        _location = os.path.join(location, "{}.{}".format(file_name, file_format))
        _location = self.__uniquify(_location) if overwrite is False else _location
        ret = -1
        try:
            if file_format in [DFormat.svg, DFormat.json]:
                with open(_location, "w", encoding="UTF-8") as f:
                    f.write(self.text(file_format))
                f.close()
            else:
                with open(_location, "wb") as f:
                    f.write(self.bytes(file_format).read())
                f.close()
            ret = _location
        except ValueError:
            raise ImageValueError(_location)
        except OSError as e:
            raise ImageOSError(str(e))
        if open_after_save:
            self.view(use_pil=False)
        return ret

    @_pilcheck
    def pillow(self) -> Im.Image:
        """
        Convert a :py:class:`DAvatar` to a :py:class:`PIL.Image.Image` object.

        :return: :py:class:`PIL.Image.Image`
        :raise `dicebear.errors.PILError`:
        """
        _statsIncrease(__filename__, self.__class__.__name__, ".pillow()")
        raw_img = Im.open(self.bytes(DFormat.png)).tobytes()
        img: Im.Image = Im.frombytes("RGBA", (256, 256), raw_img)
        return img

    def view(self, *, format: DFormat = DFormat.svg, use_pil: bool = True) -> None:
        """
        Open and view the avatar on your device.

        :param format: class `DFormat` :: what format to use when opening the DAvatar image
        :type format: dicebear.models.DFormat
        :param use_pil: class `bool` :: whether to use Pillow module to open the avatar image
        :type use_pil: bool
        :return: :py:class:`NoneType`
        :raise `dicebear.errors.PILError`:
        """
        _statsIncrease(__filename__, self.__class__.__name__, ".view()")
        if use_pil and _FindPil.found is True:
            self.__view_pil()
        elif use_pil and _FindPil.found is False:
            log_error(ModuleNotFoundError("Module `Pillow` is not found or installed"), True)
        else:
            os.startfile(getattr(self, "url_" + str(format)), "open")

    open: callable = view

    @_pilcheck
    def __view_pil(self) -> None:
        self.pillow().show("Dicebear Avatar")
