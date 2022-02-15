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
from typing import Union

class IncorrectColor(Exception):
    def __init__(self, wrong_color: str = None):
        super().__init__('Incorrect color given: "{}" is not an html hex code! (example: #ffffff)'.format(wrong_color))


class InvalidOption(Exception):
    def __init__(self, wrong_option: str = None):
        super().__init__('Invalid option given: "{}" is not an existing option! (use `Avatar.options` to get all possible options)'.format(
            wrong_option))


class Error(Exception):
    def __init__(self, error_type: str = "", message: str = ""):
        super().__init__('{}{}'.format(error_type + (': ' if error_type else ''), message))


class HTTPError(Error):
    def __init__(self, dic: dict):
        super().__init__(message=str(dic))



class ImageError(Exception):
    def __init__(self, message: str = None):
        super().__init__(message)


class ImageValueError(ImageError):
    def __init__(self, file_name: str = None):
        super().__init__('The output format could not be determined from the file name ("{}")'.format(file_name))


class ImageOSError(ImageError):
    def __init__(self, message: str = None):
        super().__init__('Fhe file could not be written. The file may have been created, and may contain partial data. ("{}")'.format(message))
