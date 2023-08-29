import PIL.Image
from dicebear import DAvatar, DStyle, DOptions, DColor, DFormat, bulk_create


# Creating options
options = DOptions(
    backgroundColor=DColor("00ddd0"),
    rotate=90
)


# Making a DAvatar object
av = DAvatar(
    style=DStyle.pixel_art,
    seed="John Apple",
    options=options
)
print(av.url_svg) # Prints the svg url


# Editing the DAvatar object
av.edit(
    extra_options=DOptions(backgroundColor=DColor("000000"))
)
# Using `extra_options` keep the `rotate` option but override the `backgroundColor` option

print(av.url_png) # Prints the png url


# Editing the style specific customisations
av.customise(
    blank_options={
        "face": "variant04"
    }
)
# Using `blank_options` will delete your previous customisations for this DAvatar and generate new ones

print(av.url_jpg) # Prints the jpg url


# Saving an avatar to your device
av.save(
    location=None, # Passing `None` will save it in the current working directory
    file_name="dicebear_avatar",
    file_format=DFormat.svg,
    overwrite=True,
    open_after_save=False
)


# Converting the DAvatar object into a PIL.Image.Image object
av_img: PIL.Image.Image = av.pillow()


# Opening and viewing the DAvatar image
av.open(use_pil=True) # or av.view()


# Creating multiple random avatars of the same style at once
avatars: list = bulk_create(style=DStyle.random(), amount=10)
