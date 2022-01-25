from dicebear import DAvatar, DStyle, DOptions, DColor

options = DOptions(
    backgroundColor=DColor("#00ddd0"), rotate=90
)

av = DAvatar(style=DStyle.pixel_art, seed="John Apple", options=options)

av.edit(extra_options=DOptions(backgroundColor=DColor("#000000")))
# This will keep the `rotate` option but override the `backgroundColor` option

print(av.url_png)
