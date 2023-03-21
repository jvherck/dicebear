# Changelog
To find the full documentation go to [https://dicebear.janvh.tk](https://dicebear.janvh.tk) \
You can click certain `blocks` to go to its documentation page. \
\
If you encounter any bugs or errors, please open an [issue](https://github.com/jvherck/dicebear/issues). 


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
