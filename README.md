# DiceBear Py Wrapper
`dicebear` is an API wrapper for https://dicebear.com. Using the API you can get custom avatars for your program.

## How to install
Run `pip install dicebear`\
If that doesn't work try `py -m pip install dicebear`

## Usage
```python
from dicebear import Avatar

options = {
    "flip": True,
    "rotate": 90
}

av = Avatar(type="avataaars", seed="John Apple", options=options) # this returns a URL to the avatar
print(av)

av.edit(options={"flip": True}) # this will edit the avatar instance 
print(av)
```


### Styles
All the possible avatar styles.

* `avataaars`
* `big-ears`
* `big-ears-neutral`
* `big-smile`
* `bottts`
* `croodles`
* `croodles-neutral`
* `gridy`
* `identicon`
* `initials`
* `jdenticon`
* `micah`
* `miniavs`
* `open-peeps`
* `personas`
* `pixel-art`
* `pixel-art-neutral`

### Base Options
All the possible options for the avatar.

* `seed` (type: string) - the seed for the avatar generator
* `dataUri` (type: boolean) - wether or not to give the dataUri 
* `flip` (type: boolean) - flips the image vertically
* `rotate` (type: int) - rotates the avatar
* `scale` (type: int) - edits the scale of the avatar
* `radius` (type: int) - edits the radius of the avatar
* `size` (type: int) - the size of the avatar
* `backgroundColor` (type: hex 0x) - the background color of the avatar
* `translateX` (type: int) - move the avatar horizontally
* `translateY` (type: int) - move the avatar vertically

### Style Options 
Specific options to get a more detailed avatar.