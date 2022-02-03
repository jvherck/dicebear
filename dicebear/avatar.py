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
import os
import pathlib
import requests as r
from urllib.parse import quote
from PIL import Image
import io
from ast import literal_eval
from .errors import *
from .models import *


_url = "https://avatars.dicebear.com/api/{}/{}.png?"


class DAvatar:
    default_options: dict = default_options
    all_options: list = options
    def __init__(self, style: DStyle, seed: str, *, options: DOptions = None, specific_options: dict = None):
        """
        Create an avatar using this class, use `.url_svg` to get the svg url or `.url_png` to get the png url.
        Clickable links: https://github.com/jvherck/dicebear#styles , https://github.com/jvherck/dicebear#base-options , https://github.com/jvherck/dicebear#specific-style-options

        :param style: the style of avatar you want to create; check the whole list at https://github.com/jvherck/dicebear#styles
        :param seed: the seed for the avatar; the avatar will be edited according to the seed.
        :param options: `class: DOptions` the options for the avatar; check the whole list at https://github.com/jvherck/dicebear#base-options
        :param specific_options: `class: dict` specific options for the specified avatar style; see all specific options at https://github.com/jvherck/dicebear#specific-style-options
        """
        if specific_options is None:
            specific_options = {}
        if options is None:
            options = DOptions.empty
        if style not in styles:
            raise Error("Invalid Style", '"{}" is not a valid style! Use `DStyle.`'.format(style))
        self.__style: DStyle = style
        self.__seed: str = seed
        self.__options: DOptions = options
        self.__specific: dict = specific_options
        self.__url_svg: str = None
        self.__text: str = None
        self.__url_png: str = None
        self.__content = None
        self.__get_avatar_url()

    @property
    def style(self) -> DStyle:
        """
        :return: the style of the avatar
        """
        return self.__style
    @property
    def seed(self) -> str:
        """
        :return: the seed of the avatar
        """
        return self.__seed
    @property
    def options(self) -> DOptions:
        """
        :return: the options of the avatar
        """
        _option_list = {}
        for key in self.__options:
            if self.__options[key] != DAvatar.default_options[key]:
                _option_list.update({key: self.__options[key]})
        return DOptions(fromdict=_option_list)
    @property
    def url_svg(self) -> str:
        """
        :return: url to avatar (svg, use `.to_png()` to convert to png)
        """
        return self.__url_svg
    @property
    def url_png(self) -> str:
        """
        :return:  url to avatar (png, use `.url_svg` to convert to svg)
        """
        return self.__url_png
    @property
    def text(self) -> str:
        """
        :return: returns the bytes of this request in str format
        """
        return self.__text

    def __repr__(self):
        self.__get_avatar_url()
        return self.__full_svg

    def __str__(self):
        self.__get_avatar_url()
        return self.__url_png

    def __get_avatar_url(self):
        _link = _url
        _options = []
        for item in options:
            if item == "size" and "size" in self.__options and self.__options["size"] == 0:
                continue
            elif item == "size" and "size" not in self.__options:
                continue
            elif item in self.__options and self.__options[item] == default_options[item]:
                continue
            elif item not in self.__options:
                continue
            else:
                _options.append(
                    "{}={}".format(
                        quote(item),
                        str(self.__options[item]).lower() if type(self.__options[item]) == bool else quote(str(self.__options[item]))
                    )
                )
        _specoptions = []
        for item in self.__specific:
            _specoptions.append(
                "{}={}".format(
                    quote(item),
                    str(self.__specific[item]).lower() if type(self.__specific[item]) == bool else quote(
                        str(self.__specific[item]))
                )
            )
        _link += "&".join(_options)
        if len(_options) == 0 and len(_specoptions) > 0:
            _link += "&".join(_specoptions)
        else:
            _link += "&" + "&".join(_specoptions)
        _link.replace("False", "false").replace("True", "true")
        _link = _link.format(quote(self.__style), quote(self.__seed))
        req = r.request('GET', _link)
        status = ""
        try:
            status = literal_eval(req.text)
        except ValueError:
            pass
        if type(status) == dict and "statusCode" in status:
            raise HTTPError(status)

        self.__url_png = req.url
        self.__url_svg = self.to_svg()
        self.__text = req.text
        self.__content = req.content
        self.__response: r.Response = req


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
            self.__style = style
        if seed:
            self.__seed = seed
        if extra_options:
            self.__options.update(extra_options)
        elif blank_options:
            self.__options = blank_options

        self.__get_avatar_url()
        return self.__url_png

    def edit_specific(self, *, extra_options: dict = None, blank_options: dict = None):
        """
        Edit the specific options for an already existing avatar.

        :param extra_options: edit the avatar's specific options (old options stay, these get added) -- cannot be used at the same time with `blank_options` !
        :param blank_options: reset old specific options and set these options as new ones (new options) -- cannot be used at the same with `extra_options` !
        :return: returns the link to the avatar url (png)
        """
        if extra_options:
            self.__specific.update(extra_options)
        elif blank_options:
            self.__specific = blank_options

        self.__get_avatar_url()
        return self.__url_png

    def to_png(self):
        """
        Turns the avatar from svg into png and returns the url.

        :return: class `str` :: link to png avatar
        """
        self.__url_png = self.__url_svg.replace(".svg", ".png")
        return self.__url_png

    def to_svg(self):
        """
        Turns the avatar from svg into png and returns the url.

        :return: class `str` :: link to png avatar
        """
        self.__url_svg = self.__url_png.replace(".png", ".svg")
        return self.__url_svg

    def save(self, *, location: pathlib.Path = None, file_name: str = "dicebear_avatar", format: DFormat = DFormat.png):
        """
        Save a file to your device. (Currently overrides if a file with this name and format already exists!)

        :param location: class `pathlib.Path` :: the folder to save the file in. (default is None which saves it in the current directory `os.getcwd()`
        :param file_name: class `str` :: the name of the file to save. (default is "dicebear_avatar")
        :param format: class `DFormat` :: the format of the file. (default is "png")
        :return: returns the path when successful
        """
        if location is None:
            location = pathlib.Path(os.getcwd())
        _location = os.path.join(location, "{}.{}".format(file_name, format)) # TODO: when file exists add num
        if format == DFormat.svg:
            svg_text = r.request('GET', self.to_svg()).text
        else:
            img = Image.open(io.BytesIO(self.__response.content))
        ret = -1
        try:
            if format == DFormat.svg:
                with open(_location, "w", encoding="UTF-8") as f:
                    f.write(svg_text)
                f.close()
            else:
                img.save(_location, format)
        except ValueError:
            raise ImageValueError()
        except OSError:
            raise ImageOSError()
        except Exception as e:
            raise e
        else:
            ret = _location

        return ret

