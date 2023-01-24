# DiceBear Py Wrapper  
![Downloads](https://static.pepy.tech/personalized-badge/dicebear?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)
![Downloads](https://static.pepy.tech/personalized-badge/dicebear?period=month&units=international_system&left_color=grey&right_color=orange&left_text=Downloads/Month)
![PyPI](https://img.shields.io/pypi/v/dicebear)
![GitHub issues](https://img.shields.io/github/issues/jvherck/dicebear)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dicebear)
![GitHub](https://img.shields.io/github/license/jvherck/dicebear)
![Maintenance](https://img.shields.io/maintenance/yes/2024)
![PyPI - Status](https://img.shields.io/pypi/status/dicebear)

Always keep an eye on https://dicebear.janvh.tk for updates and warnings about this packages!

[`dicebear`](https://pypi.org/project/dicebear/) is an API wrapper for https://dicebear.com. Using this wrapper you can get custom avatars for your program. \
For an example go to [`examples/dicebear.py`](https://github.com/jvherck/dicebear/tree/main/examples).


---


## Useful links  
* Docs: https://jvherck.github.io/dicebear  
* PyPI: https://pypi.org/project/dicebear/  
* GitHub: https://github.com/jvherck/dicebear  
* Dicebear: https://dicebear.com/  
- Dicebear CLI: https://github.com/jvherck/dicebear-cli  


---


## How to install  
Run `pip install dicebear` \
If that doesn't work try `py -m pip install dicebear`  


---


## Usage  
Important note: *Pillow* is not a required dependency, it's only required when you want to be able to edit the avatar images (using `DAvatar.pillow()`).
When using a `PIL` function while it's not installed it will raise `dicebear.errors.PILError`.  
```py  
import PIL.Image  
from dicebear import DAvatar, DStyle, DOptions, DColor, bulk_create  
  
  
# Creating options  
options = DOptions(  
 backgroundColor=DColor("00ddd0"), rotate=90)  
  
  
# Making a DAvatar object  
av = DAvatar(  
 style=DStyle.pixel_art, seed="John Apple", options=options)  
print(av.url_svg) # Prints the svg url  
  
  
# Editing the DAvatar object  
av.edit(  
 extra_options=DOptions(backgroundColor=DColor("000000")))  
# Using `extra_options` keep the `rotate` option but override the `backgroundColor` option  
  
print(av.url_jpg) # Prints the jpg url  
  
  
# Editing the style specific customisations  
av.customise(  
 blank_options={ "face": "variant04" })  
# Using `blank_options` will delete your previous customisations for this DAvatar and generate new ones  
  
print(av.url_svg) # Prints the svg url  
  
  
# Converting the DAvatar object into a PIL.Image.Image object  
av_img: PIL.Image.Image = av.pillow()  
  
  
# Opening and viewing the DAvatar image  
av.open(use_pil=True) # or av.view()  
  
  
# Creating multiple random avatars of the same style at once  
avatars: list = bulk_create(style=DStyle.random(), amount=10)  
```  


## CLI Usage  
Since version 0.4.0 there's a CLI for DiceBear. It can quickly create one or more avatars at a time
but it can't take options.  

__To use the CLI go to__ https://github.com/jvherck/dicebear-cli __and use `pip install dicebear-cli` to install the CLI__  


---


## Customisation  
Customise your avatars with these possibilities.  


### Styles  
All the possible avatar styles. \
https://dicebear.com/styles  
  
* `adventurer`  
* `adventurer-neutral`  
* `avataaars`  
* `avataaars-neutral`  
* `big-ears`  
* `big-ears-neutral`  
* `big-smile`  
* `bottts`  
* `bottts-neutral`  
* `croodles`  
* `croodles-neutral`  
* `fun-emoji`  
* `icons`  
* `identicon`  
* `initials`  
* `lorelei`  
* `lorelei-neutral`  
* `micah`  
* `miniavs`  
* `open-peeps`  
* `personas`  
* `pixel-art`  
* `pixel-art-neutral`  


### Base Options  
All the possible options for the avatar. These options work for all the styles.  

* `seed` (type: `str`) - the seed for the avatar generator, determine its basic looks  
* `flip` (type: `bool`) - flips the image vertically (default False)  
* `rotate` (type: `int`) - rotates the avatar (default 0, min 0, max 360)  
* `scale` (type: `int`) - the scale of the avatar drawing itself (default 100, min 0, max 200)  
* `radius` (type: `int`) - the radius of the avatar (default 0, min 0, max 50)  
* `size` (type: `int`) - the size of the avatar (px) (default 256, min 1, max 256)  
* `backgroundColor` (type: `DColor("transparent")` ) - the background color of the avatar (default transparent)  
* `backgroundType` (type: `str` ) - set the background to either `gradientLinear` or `solid` (default solid)  
* `backgroundRotation` (type: `int` ) - rotate the background if backgroundType is set to `gradientLinear` (default 0)  
* `translateX` (type: `int`) - move the avatar horizontally (default 0, min -100, max 100)  
* `translateY` (type: `int`) - move the avatar vertically (default 0, min -100, max 100)  


### Specific Style Options   
Specific options to get a more detailed avatar. This is different for every style. \
Click the style to see its options.  

* [adventurer](https://dicebear.com/styles/adventurer#options)  
* [adventurer-neutral](https://dicebear.com/styles/adventurer-neutral#options)  
* [avataaars](https://dicebear.com/styles/avataaars#options)  
* [avataaars-neutral](https://dicebear.com/styles/avataaars-neutral#options)  
* [big-ears](https://dicebear.com/styles/big-ears#options)  
* [big-ears-neutral](https://dicebear.com/styles/big-ears-neutral#options)  
* [big-smile](https://dicebear.com/styles/big-smile#options)  
* [bottts](https://dicebear.com/styles/bottts#options)  
* [bottts-neutral](https://dicebear.com/styles/bottts-neutral#options)  
* [croodles](https://dicebear.com/styles/croodles#options)  
* [croodles-neutral](https://dicebear.com/styles/croodles-neutral#options)  
* [fun-emoji](https://dicebear.com/styles/fun-emoji#options)  
* [icons](https://dicebear.com/styles/icons#options)  
* [identicon](https://dicebear.com/styles/identicon#options)  
* [initials](https://dicebear.com/styles/initials#options)  
* [lorelei](https://dicebear.com/styles/lorelei#options)  
* [lorelei-neutral](https://dicebear.com/styles/lorelei-neutral#options)  
* [micah](https://dicebear.com/styles/micah#options)  
* [miniavs](https://dicebear.com/styles/miniavs#options)  
* [open-peeps](https://dicebear.com/styles/open-peeps#options)  
* [personas](https://dicebear.com/styles/personas#options)  
* [pixel-art](https://dicebear.com/styles/pixel-art#options)  
* [pixel-art-neutral](https://dicebear.com/styles/pixel-art-neutral#options)  


### Formats   
These are the only supported formats. \
If you have Pillow (PIL) installed you can convert `DAvatar` to a `PIL.Image.Image` object to get a
wider range of formats (Pillow doesn't support svg).  
  
* `DFormat.svg` (default)  
* `DFormat.png`  
* `DFormat.jpg`  
* `DFormat.json`  


---


## Credits  
Special thanks to [DiceBear](https://github.com/dicebear) ([Florian Körner](https://github.com/FlorianKoerner)) for making this amazing API and to [all artists](https://dicebear.com/licenses) that helped   
making avatars!  


## Licenses and privacy policy  
- Dicebear **Licenses**: https://dicebear.com/licenses  
- Dicebear **Privacy Policy**: https://dicebear.com/legal/privacy-policy  
- Dicebear Python API wrapper (this project): https://github.com/jvherck/dicebear/blob/main/LICENSE
