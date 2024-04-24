# Changelog
To find the full documentation go to [https://jvh.gitbook.io/dicebear/](https://jvh.gitbook.io/dicebear/) \
You can click certain `blocks` to go to its documentation page. \
\
If you encounter any bugs or errors, please open an [issue](https://github.com/jvherck/dicebear/issues). 


---


## v2.7.4
2024-04-24

### Back-end
- Back-end cleanup
- Dicebear version upgrade to 8.x (which contains API bug fixes)


---


## v2.7.3
2024-03-09

### Added
- [`styles_metadata`](https://jvh.gitbook.io/dicebear/reference/models#variables) (models.py) to directly get metadata of every style

### Back-end
- Made usage stats opt-in with environment variable [`ENABLE_PYTHON_DICEBEAR_USAGE_STATS`](https://jvh.gitbook.io/dicebear/start/statistics) set to true

### Fixed
- [`notionists`](https://jvh.gitbook.io/dicebear/start/customization#styles) and [`notionists-neutral`](https://jvh.gitbook.io/dicebear/start/customization#styles) were not implemented but have been added now


---


## v2.7.2
2023-12-12

### Added
- New attribute [`schema`](https://jvh.gitbook.io/dicebear/reference/avatar#properties) for [`DAvatar`](https://jvh.gitbook.io/dicebear/reference/avatar#class-davatar) class

### Back-end
- Removed `test` parameter on all functions
- Improved type hinting and imports


---


## v2.7.0
2023-08-29

### Added
- New style [`rings`](https://jvh.gitbook.io/dicebear/start/customization#styles)
- New function [`DStyle.get_schema(style: str)`](https://jvh.gitbook.io/dicebear/reference/models#def-get_schema) to get the schema (all properties) of the given avatar style

### Back-end
- Upgrade to Dicebear new API version 7.0


---


## v2.6.1
2023-04-11

### Added
- New style [`notionists`](https://jvh.gitbook.io/dicebear/start/customization#styles)
- New style [`notionists-neutral`](https://jvh.gitbook.io/dicebear/start/customization#styles)

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
- Methods [`DAvatar.text(format)`](https://jvh.gitbook.io/dicebear/reference/avatar#def-text) and [`DAvatar.bytes(format)`](https://jvh.gitbook.io/dicebear/reference/avatar#def-bytes)

### Fixed
- [`DAvatar.pillow()`](https://jvh.gitbook.io/dicebear/reference/avatar#def-pillow) no longer raises error for no reason
