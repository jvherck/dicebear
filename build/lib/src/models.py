from .errors import *
from typing import Union


options = ["dataUri", "flip", "rotate", "scale", "radius", "size", "backgroundColor", "translateX", "translateY"]
styles = ["adventurer", "adventurer-neutral", "avataaars", "big-ears", "big-ears-neutral",
          "big-smile", "bottts", "croodles", "croodles-neutral", "identicon", "initials",
          "micah", "miniavs", "open-peeps", "personas", "pixel-art", "pixel-art-neutral"]
styles_depricated = ["female", "gridy", "human", "jdenticon", "male"]


class DColor(str):
    def __init__(self, hex_code: str = "#ffffff"):
        if not hex_code.startswith("#"):
            hex_code = "#" + hex_code
        if len(hex_code) not in [4, 7]:
            raise IncorrectColor(str(hex_code))
        self.hex_code: str = str(hex_code)
        super().__init__()

    def __str__(self):
        return f"{self.hex_code}"
    def __repr__(self):
        return f"{self.hex_code}"


class DStyle(str):
    adventurer = styles[0]
    adventurer_neutral = styles[1]
    avataaars = styles[2]
    big_ears = styles[3]
    big_ears_neutral = styles[4]
    big_smile = styles[5]
    bottts = styles[6]
    croodles = styles[7]
    croodles_neutral = styles[8]
    identicon = styles[9]
    initials = styles[10]
    micah = styles[11]
    miniavs = styles[12]
    open_peeps = styles[13]
    personas = styles[14]
    pixel_art = styles[15]
    pixel_art_neutral = styles[16]


default_options: dict = {options[0]: False, options[1]: False, options[2]: 0, options[3]: 100, options[4]: 0,
             options[5]: 0, options[6]: DColor(), options[7]: 0, options[8]: 0}

class DOptions(dict):
    empty: dict = {}
    def __init__(self, *, dataUri: bool = False, flip: bool = False, rotate: int = 0, scale: int = 100,
                 radius: int = 0, size: int = 0, backgroundColor: DColor = DColor(), translateX: int = 0, translateY: int = 0, **kwargs):
        # kwargs: list = [dataUri, flip, rotate, scale, radius, size, backgroundColor, translateX, translateY]
        dic = kwargs.get("fromdict", {})
        current: dict = {"dataUri": dataUri, "flip": flip, "rotate": rotate, "scale": scale, "radius": radius, "size": size,
                     "backgroundColor": backgroundColor, "translateX": translateX, "translateY": translateY}
        if not dic:
            for item in current:
                if item in default_options and current[item] != default_options[item]:
                    dic.update({item: current[item]})
        if "size" in dic and dic["size"] == 0:
            dic.pop("size")
        super().__init__(dic)



class DUrl:
    def __init__(self, url: str,):
        self._url = url

    def __str__(self) -> str:
        return str(self._url)
    def __repr__(self) -> str:
        return str(self._url)
    def __eq__(self, other) -> bool:
        if isinstance(other, DUrl):
            if str(other) == str(self._url):
                return True
        return False
    def __ne__(self, other) -> bool:
        if isinstance(other, (str, DUrl)):
            if str(other) != str(self._url):
                return True
        return False


