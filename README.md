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