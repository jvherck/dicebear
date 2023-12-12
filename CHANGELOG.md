# Changelog
To find the full documentation go to [https://dicebear.janvh.tk](https://dicebear.janvh.tk) \
You can click certain `blocks` to go to its documentation page. \
\
If you encounter any bugs or errors, please open an [issue](https://github.com/jvherck/dicebear/issues). 


---


## v2.7.1
2023-12-12

### Added
- New attribute [`schema`](https://dicebear.janvh.tk/reference/avatar#properties) for [`DAvatar`](https://dicebear.janvh.tk/reference/avatar#class-davatar) class

### Back-end
- Removed `test` parameter on all functions
- Improved type hinting and imports


---


## v2.7.0
2023-08-29

### Added
- New style [`rings`](https://dicebear.janvh.tk/start/customization#styles)
- New function [`DStyle.get_schema(style: str)`](https://dicebear.janvh.tk/reference/models#def-get_schema) to get the schema (all properties) of the given avatar style

### Back-end
- Upgrade to Dicebear new API version 7.0


---


## v2.6.1
2023-04-11

### Added
- New style [`notionists`](https://dicebear.janvh.tk/start/customization#styles)
- New style [`notionists-neutral`](https://dicebear.janvh.tk/start/customization#styles)

### Back-end
- Upgrade to Dicebear new API version 6.0


---


## v2.5.2
2023-03-21

### Back-end
- The package now pings an API to update the usage statistics (nothing personal is stored, it simply increments the 
amount of times certain functions have been used)


---


## v2.5.1
2023-03-16

### Removed
- Properties `DAvatar.text` and `DAvatar.bytes`

### Added
- Methods [`DAvatar.text(format)`](https://dicebear.janvh.tk/reference/avatar#def-text) and [`DAvatar.bytes(format)`](https://dicebear.janvh.tk/reference/avatar#def-bytes)

### Fixed
- [`DAvatar.pillow()`](https://dicebear.janvh.tk/reference/avatar#def-pillow) no longer raises error for no reason
