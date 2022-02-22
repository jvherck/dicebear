# DiceBear Py Wrapper
[![Downloads](https://static.pepy.tech/personalized-badge/dicebear?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/dicebear) [![Downloads](https://static.pepy.tech/personalized-badge/dicebear?period=month&units=international_system&left_color=grey&right_color=orange&left_text=Downloads/Month)](https://pepy.tech/project/dicebear) \
[`dicebear`](https://pypi.org/project/dicebear/) is an API wrapper for https://dicebear.com. Using this wrapper you can get custom avatars for your program.
\
For an example go to [`examples/dicebear.py`](https://github.com/jvherck/dicebear/tree/main/examples).

---

## Useful links
* PyPI: https://pypi.org/project/dicebear/
* GitHub: https://github.com/jvherck/dicebear
* Dicebear: https://dicebear.com

---

## How to install
Run `pip install dicebear`\
If that doesn't work try `py -m pip install dicebear`

---

## Usage
Important note: *Pillow* is not a required dependency, it's only required when you want to be able to edit the avatar images (using `DAvatar.pillow()`). 
When using a `PIL` function while it's not installed it will raise `dicebear.errors.PILError`.
```python
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
```

---

### Styles
All the possible avatar styles. \
https://avatars.dicebear.com/styles

* `adventurer`
* `adventurer-neutral`
* `avataaars`
* `big-ears`
* `big-ears-neutral`
* `big-smile`
* `bottts`
* `croodles`
* `croodles-neutral`
* `identicon`
* `initials`
* `micah`
* `miniavs`
* `open-peeps`
* `personas`
* `pixel-art`
* `pixel-art-neutral`

### Base Options
All the possible options for the avatar. These options work for all the styles.

* `seed` (type: `str`) - the seed for the avatar generator (determine its basic looks)
* `dataUri` (type: `bool`) - whether to give the dataUri 
* `flip` (type: `bool`) - flips the image vertically
* `rotate` (type: `int`) - rotates the avatar
* `scale` (type: `int`) - the scale of the avatar
* `radius` (type: `int`) - the radius of the avatar
* `size` (type: `int`) - the size of the avatar
* `backgroundColor` (type: `DColor( " #ffffff " )` ) - the background color of the avatar
* `translateX` (type: `int`) - move the avatar horizontally
* `translateY` (type: `int`) - move the avatar vertically

### Specific Style Options 
Specific options to get a more detailed avatar. This is different for every style.

* [adventurer](https://avatars.dicebear.com/styles/adventurer#style-options)
* [adventurer-neutral](https://avatars.dicebear.com/styles/adventurer-neutral#style-options)
* [avataaars](https://avatars.dicebear.com/styles/avataaars#style-options)
* [big-ears](https://avatars.dicebear.com/styles/big-ears#style-options)
* [big-ears-neutral](https://avatars.dicebear.com/styles/big-ears-neutral#style-options)
* [big-smile](https://avatars.dicebear.com/styles/big-smile#style-options)
* [bottts](https://avatars.dicebear.com/styles/bottts#style-options)
* [croodles](https://avatars.dicebear.com/styles/croodles#style-options)
* [croodles-neutral](https://avatars.dicebear.com/styles/croodles-neutral#style-options)
* [identicon](https://avatars.dicebear.com/styles/identicon#style-options)
* [initials](https://avatars.dicebear.com/styles/initials#style-options)
* [micah](https://avatars.dicebear.com/styles/micah#style-options)
* [miniavs](https://avatars.dicebear.com/styles/miniavs#style-options)
* [open-peeps](https://avatars.dicebear.com/styles/open-peeps#style-options)
* [personas](https://avatars.dicebear.com/styles/personas#style-options)
* [pixel-art](https://avatars.dicebear.com/styles/pixel-art#style-options)
* [pixel-art-neutral](https://avatars.dicebear.com/styles/pixel-art-neutral#style-options)

---

## Credits
Special thanks to [DiceBear](https://github.com/dicebear) 
([Florian Körner](https://github.com/FlorianKoerner)) 
for making this amazing API and to all artists that helped 
making avatars!

## Licenses and privacy policy
- Dicebear **Licenses**: https://avatars.dicebear.com/licenses
- Dicebear **Privacy Policy**: https://avatars.dicebear.com/legal/privacy-policy
- Dicebear Python API wrapper (this project): https://choosealicense.com/licenses/mit/