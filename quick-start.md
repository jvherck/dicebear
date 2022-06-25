---
description: >-
  dicebear is an API wrapper for https://dicebear.com. Using this wrapper you
  can get custom avatars for your program.
---

# Quick Start

## Installing

```shell
pip install -U dicebear
```

or

```shell
py -m pip install -U dicebear
```

## Make your first avatar

Here's a quick example on how to quickly make your first own avatar.

```python
from dicebear import DAvatar, DStyle, DOptions, DColor
from PIL import Image

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

image: Image.Image = av.pillow()
# converts the DAvatar into a Pillow Image object
```
