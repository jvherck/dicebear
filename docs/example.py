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
