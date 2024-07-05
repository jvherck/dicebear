# ℹ️ Changelog

To find the full documentation go to [https://dicebear.vhjan.me/](https://dicebear.vhjan.me/)\
You can click certain `blocks` to go to its documentation page.\
\
If you encounter any bugs or errors, please open an [issue](https://github.com/jvherck/dicebear/issues).

***

## v2.7.5

2024-07-06

### Back-end

* Dicebear version upgrade to 9.x

### Improvements

* Added tox for code quality automation

### Changed
* Moved style metadata to separate file `dicebear.metadata.Metadata`

***

## v2.7.4

2024-04-24

### Back-end

* Back-end cleanup
* Dicebear version upgrade to 8.x (API bug fixes)

***

## v2.7.3

2024-03-09

### Added

* [`styles_metadata`](https://dicebear.vhjan.me/reference/models#variables) (models.py) to directly get metadata of every style

### Back-end

* Made usage stats opt-in with environment variable [`ENABLE_PYTHON_DICEBEAR_USAGE_STATS`](https://dicebear.vhjan.me/start/statistics) set to true

### Fixed

* [`notionists`](https://dicebear.vhjan.me/start/customization#styles) and [`notionists-neutral`](https://dicebear.vhjan.me/start/customization#styles) were not implemented but have been added now

***

## v2.7.2

2023-12-12

### Added

* New attribute [`schema`](https://dicebear.vhjan.me/reference/avatar#properties) for [`DAvatar`](https://dicebear.vhjan.me/reference/avatar#class-davatar) class

### Back-end

* Removed `test` parameter on all functions
* Improved type hinting and imports

***

## v2.7.0

2023-08-29

### Added

* New style [`rings`](https://dicebear.vhjan.me/start/customization#styles)
* New function [`DStyle.get_schema(style: str)`](https://dicebear.vhjan.me/reference/models#def-get\_schema) to get the schema (all properties) of the given avatar style

### Back-end

* Upgrade to Dicebear new API version 7.0

***

## v2.6.1

2023-04-11

### Added

* New style [`notionists`](https://dicebear.vhjan.me/start/customization#styles)
* New style [`notionists-neutral`](https://dicebear.vhjan.me/start/customization#styles)

### Back-end

* Upgrade to Dicebear new API version 6.0

***

## v2.5.2

2023-03-21

### Back-end

* The package now pings an API to update the usage statistics (nothing personal is stored, it simply increments the amount of times certain functions have been used)

***

## v2.5.1

2023-03-16

### Removed

* Properties `DAvatar.text` and `DAvatar.bytes`

### Added

* Methods [`DAvatar.text(format)`](https://dicebear.vhjan.me/reference/avatar#def-text) and [`DAvatar.bytes(format)`](https://dicebear.vhjan.me/reference/avatar#def-bytes)

### Fixed

* [`DAvatar.pillow()`](https://dicebear.vhjan.me/reference/avatar#def-pillow) no longer raises error for no reason
