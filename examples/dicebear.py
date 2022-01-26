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

from dicebear import DAvatar, DStyle, DOptions, DColor

options = DOptions(
    backgroundColor=DColor("#00ddd0"),
    rotate=90
)

av = DAvatar(
    style=DStyle.pixel_art,
    seed="John Apple",
    options=options
)

print(av.url_svg)

av.edit(
    extra_options=DOptions(
        backgroundColor=DColor("#000000")
    )
)
# This will keep the `rotate` option but override the `backgroundColor` option

print(av.url_png)

av.edit_specific(
    blank_options={
        "face": "variant04"
    }
)
# This edits the style specific options

print(av.url_png)
